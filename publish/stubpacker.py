import logging
import shutil
import subprocess
import hashlib
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import tomli
import tomli_w
from packaging.version import Version, LegacyVersion, parse


log = logging.getLogger(__name__)
log.setLevel("INFO")

# https://peps.python.org/pep-0440/
def bump_postrelease(
    current: Version,
) -> Version:
    """Increases the post release version number"""
    parts = []
    # Epoch
    if current.epoch != 0:
        parts.append(f"{current.epoch}!")
    # Release segment
    parts.append(".".join(str(x) for x in current.release))
    # Pre-release
    if current.pre is not None:
        parts.append("".join(str(x) for x in current.pre))
    # BUMP Post-release
    if current.post is not None:
        parts.append(f".post{current.post + 1}")
    else:
        parts.append(f".post{1}")
    # Development release
    if current.dev is not None:
        parts.append(f".dev{current.dev}")

    # Local version segment
    if current.local is not None:
        parts.append(f"+{current.local}")

    new = parse("".join(parts))
    if not isinstance(new, Version):
        raise ValueError(f"{new} is not a valid version")

    return new


# def calculate_checksum(filenames):
#     hash = hashlib.md5()
#     for fn in filenames:
#         if os.path.isfile(fn):
#             hash.update(open(fn, "rb").read())
#     return hash.digest()


class StubPackage:
    """
    Create a stub-only package for a specific version of micropython
        - version
        - port
        - board
    """

    def __init__(
        self,
        package_path: Path,
        package_name: str,
        version: str = "0.0.1",
        description: str = "MicroPython stubs",
        stubs: Optional[List[Tuple[str, Path]]] = None,
    ):
        # create the package folder
        package_path.mkdir(parents=True, exist_ok=True)
        # store essentials
        self.package_path = package_path
        self.package_name = package_name
        self.description = description
        # save the stub sources
        stub_sources: List[Tuple[str, Path]] = []
        if stubs:
            self.stub_sources = stubs
        # normalise the version to semver
        self.mpy_version = str(parse(version.replace("_", ".")))  # Initial version
        # convert V1_18 to semver (Major.Minor) and use the patch level (or post release)  as version for the stubs package

    @property
    def toml_file(self) -> Path:
        return self.package_path / "pyproject.toml"

    # -----------------------------------------------
    @property
    def pkg_version(self) -> str:
        "return the version of the package"
        # read the version from the toml file
        if not self.toml_file.exists():
            self.mpy_version
        with open(self.toml_file, "rb") as f:
            pyproject = tomli.load(f)
        return str(parse(pyproject["tool"]["poetry"]["version"]))

    @pkg_version.setter
    def pkg_version(self, version):
        "set the version of the package"
        # read the current file
        with open(self.toml_file, "rb") as f:
            pyproject = tomli.load(f)
        pyproject["tool"]["poetry"]["version"] = version

        # update the version in the toml file
        with open(self.toml_file, "wb") as output:
            tomli_w.dump(pyproject, output)

    # -----------------------------------------------
    @property
    def pyproject(self) -> Union[Dict[str, Any], None]:
        "parsed pyproject.toml or None"
        pyproject = None
        if self.toml_file.exists():
            with open(self.toml_file, "rb") as f:
                pyproject = tomli.load(f)
        return pyproject

    @pyproject.setter
    def pyproject(self, pyproject):
        # check if the result is a valid toml file
        try:
            tomli.loads(tomli_w.dumps(pyproject))
        except tomli.TOMLDecodeError as e:
            print("Could not create a valid TOML file")
            raise (e)
        with open(self.toml_file, "wb") as output:
            tomli_w.dump(pyproject, output)

    # -----------------------------------------------

    # package_version = property(get_package_version)

    def to_json(self):
        """return the package as json

        need to simplify some of the Objects to allow serialisation to json
        - the paths to posix paths
        - the version (semver) to a string
        - toml file to list of lines

        """
        return {
            "name": self.package_name,
            "mpy_version": self.mpy_version,
            "publish": True,
            "pkg_version": str(self.pkg_version),
            "path": self.package_path.as_posix(),
            "stub_sources": [(name, Path(path).as_posix()) for (name, path) in self.stub_sources],
            "description": self.description,
            "hashes": [],
            "pyproject": open(self.toml_file).read().splitlines(),
        }

    def update_package_files(
        self,
    ):
        """
        Update the stub-only package for a specific version of micropython
        copies the stubs from the  list of stubs.

        """
        # create the package folder
        self.package_path.mkdir(parents=True, exist_ok=True)

        self.clean()  # Delete any previous *.py? files
        self.copy_stubs()
        # self.create_pyproject()
        self.create_readme()
        self.create_license()

    def copy_stubs(self):
        """
        Copy the stubs to the package folder
        """
        # Copy  the stubs to the package, directly in the package folder (no folders)
        for name, folder in self.stub_sources:
            print(f"Copying {name} from {folder}")
            # shutil.copytree(folder, package_path / folder.name, symlinks=True, dirs_exist_ok=True)
            shutil.copytree(folder, self.package_path, symlinks=True, dirs_exist_ok=True)

    def create_readme(self):
        """
        Create a readme file for the package
        """
        # read the readme file and update the version and description
        with open(self.package_path / "../template/README.md", "r") as f:
            TEMPLATE_README = f.read()

        # add a readme with the names of the stubs

        # Prettify this by merging with template text
        with open(self.package_path / "README.md", "w") as f:
            f.write(f"# {self.package_name}\n\n")
            f.write(TEMPLATE_README)
            f.write(f"Included stubs:\n")
            for name, folder in self.stub_sources:
                f.write(f"* {name} from {Path(folder).as_posix()}\n")

    def create_license(self):
        """
        Create a license file for the package
        """
        # copy the license file from the template  to the package
        # copy the license file from the template  to the package
        # todo: append other license files
        shutil.copy(self.package_path / "../template/LICENSE.md", self.package_path)

    def create_pyproject(
        self,
        pyproject_data: Optional[List[str]] = None,
    ):
        """
        create or update/overwrite a `pyproject.toml` file by combining a template file
        with the given parameters.
        and updating it with the pyi files included
        """

        # Do not overwrite existing pyproject.toml but read and apply changes to it
        # 1) recreate from database, if provided
        # 2) read from disk , if exists
        # 3) create from template, in all other cases
        on_disk = (self.toml_file).exists()
        if pyproject_data:
            # pyproject has been read from the database
            # write the pyproject toml file
            with open(self.toml_file, "w") as output:
                output.writelines("\n".join(pyproject_data))

            _pyproject = self.pyproject
        elif on_disk:
            # do not overwrite the version of a pre-existing file
            _pyproject = self.pyproject
            assert _pyproject is not None
            # clear out the packages section
            _pyproject["tool"]["poetry"]["packages"] = []

        else:
            # read the template pyproject.toml file
            template_path = self.package_path / "../template"
            with open(template_path / "pyproject.toml", "rb") as f:
                _pyproject = tomli.load(f)
            _pyproject["tool"]["poetry"]["version"] = self.mpy_version

        # check if version number of the package matches the version number of the stubs
        ver_pkg = parse(_pyproject["tool"]["poetry"]["version"])
        ver_stubs = parse(self.mpy_version)
        if isinstance(ver_stubs, LegacyVersion) or isinstance(ver_pkg, LegacyVersion):
            raise ValueError(f"Legacy version not supported: {ver_pkg} || {ver_stubs}")

        if not (ver_pkg.major == ver_stubs.major and ver_pkg.minor == ver_stubs.minor):

            log.warning(f"Package version:{ver_pkg.public} does not match the version of the stubs: {ver_stubs.public}")
            _pyproject["tool"]["poetry"]["version"] = self.mpy_version

        # update the name , version and description of the package
        _pyproject["tool"]["poetry"]["name"] = self.package_name
        _pyproject["tool"]["poetry"]["description"] = self.description
        # write out the pyproject.toml file
        self.pyproject = _pyproject

    def update_included_stubs(self):
        "Add the stub files to the pyproject.toml file"
        _pyproject = self.pyproject
        # find packages using __init__ files
        for p in self.package_path.rglob("**/__init__.py"):
            # add the module to the package
            # fixme : only accounts for one level of packages
            _pyproject["tool"]["poetry"]["packages"] += [{"include": p.parent.name}]
        # now find other stub files directly in the folder
        for p in self.package_path.glob("*.pyi"):
            _pyproject["tool"]["poetry"]["packages"] += [{"include": p.name}]
        # write out the pyproject.toml file
        self.pyproject = _pyproject

        # OK

    def clean(self):
        """
        Remove the stub files from the package folder

        This is used before update the stub package, to avoid lingering stub files,
        and after the package has been built, to avoid needing to store files multiple times.

        `.gitignore` cannot be used as this will prevent poetry from processing the files.

        """
        # remove all *.py and *.pyi files in the folder
        for wc in ["*.py", "*.pyi", "modules.json"]:
            for f in self.package_path.rglob(wc):
                f.unlink()

    def check(self) -> bool:
        "check if the package is valid"
        try:
            subprocess.run(["poetry", "check", "-vvv"], cwd=self.package_path)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            return False
        return True

    def bump(self):
        "bump the version of the package"
        try:
            # read the pyproject.toml file
            with open(self.toml_file, "rb") as f:
                pyproject = tomli.load(f)

            current = parse(pyproject["tool"]["poetry"]["version"])
            assert isinstance(current, Version)
            # bump the version
            new = bump_postrelease(current)
            pyproject["tool"]["poetry"]["version"] = str(new)
            # write the pyproject.toml file
            # check if the result is a valid toml file
            try:
                tomli.loads(tomli_w.dumps(pyproject))
            except tomli.TOMLDecodeError as e:
                print("Could not create a valid TOML file")
                raise (e)

            with open(self.toml_file, "wb") as output:
                tomli_w.dump(pyproject, output)

        except Exception as e:
            log.error(f"Error: {e}")
            return False
        return True

    def build(self):
        # BUG: does not detect errors in the build
        try:
            # create package
            subprocess.run(["poetry", "build", "-vvv"], cwd=self.package_path, check=True)
        except Exception as e:
            log.error(f"Error: {e}")
            return False
        return True

    def publish(self):
        # BUG: does not detect errors in publishing
        try:
            # Publish to test
            subprocess.run(["poetry", "publish", "-r", "test-pypi"], cwd=self.package_path, check=True)
        except Exception as e:
            log.error(f"Error: {e}")
            return False
        return True
