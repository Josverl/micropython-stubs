import logging
import shutil
import subprocess
import hashlib
from pathlib import Path
from typing import List, Optional, Tuple
from typing_extensions import assert_type

import tomli
import tomli_w
from packaging.version import LegacyVersion, parse




log = logging.getLogger(__name__)
log.setLevel("INFO")


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
        stub_sources :List[Tuple[str, Path]] = []
        if stubs:
            self.stub_sources = stubs
        self.mpy_version = version.replace("_", ".") # Initial version
        # convert V1_18 to semver (Major.Minor) and use the patch level (or post release)  as version for the stubs package

    @property
    def toml_file(self) -> Path:
        return self.package_path / "pyproject.toml"

    @property
    def pkg_version(self):
        "return the version of the package"
        # read the version from the toml file
        if not self.toml_file.exists():
            return None
        with open(self.toml_file, "rb") as f:
            pyproject = tomli.load(f)
        return parse(pyproject["tool"]["poetry"]["version"])

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
            "stub_sources": [(name, path.as_posix()) for (name, path) in self.stub_sources ],
            "hashes": [],
            "toml": [] # open(self.toml_file).read().splitlines(),
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
        
        self.clean()                # Delete any previous *.py? files
        self.copy_stubs()
        self.create_pyproject()
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
                f.write(f"* {name} from {folder.as_posix()}\n")
    
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
    ):
        """
        create or update/overwrite a `pyproject.toml` file by combining a template file
        with the given parameters.
        and updating it with the pyi files included
        """

        # Do not overwrite existing pyproject.toml but read and apply changes to it
        pre_existing = (self.toml_file).exists()
        if pre_existing:
            with open(self.toml_file, "rb") as f:
                pyproject = tomli.load(f)
                # do not overwrite the version of a pre-existing file
                # clear out the packages section
                pyproject["tool"]["poetry"]["packages"] = []
        else:
            # read the template pyproject.toml file
            template_path = self.package_path / "../template"
            with open(template_path / "pyproject.toml", "rb") as f:
                pyproject = tomli.load(f)
                pyproject["tool"]["poetry"]["version"] = self.mpy_version

        # check if version number of the package matches the version number of the stubs
        ver_pkg = parse(pyproject["tool"]["poetry"]["version"])
        ver_stubs = parse(self.mpy_version)
        if isinstance(ver_stubs, LegacyVersion) or isinstance(ver_pkg, LegacyVersion):
            raise ValueError(f"Legacy version not supported: {ver_pkg} || {ver_stubs}")

        if not (ver_pkg.major == ver_stubs.major and ver_pkg.minor == ver_stubs.minor):

            log.warning(f"Package version:{ver_pkg.public} does not match the version of the stubs: {ver_stubs.public}")
            pyproject["tool"]["poetry"]["version"] = self.mpy_version

        # update the name , version and description of the package
        pyproject["tool"]["poetry"]["name"] = self.package_name
        pyproject["tool"]["poetry"]["description"] = self.description

        # add the stub files to the package

        # find packages using __init__ files
        for p in self.package_path.rglob("**/__init__.py"):
            # add the module to the package
            # fixme : only accounts for one level of packages
            pyproject["tool"]["poetry"]["packages"] += [{"include": p.parent.name}]
        # now find other stub files directly in the folder
        for p in self.package_path.glob("*.pyi"):
            pyproject["tool"]["poetry"]["packages"] += [{"include": p.name}]

        # check if the result is a valid toml file
        try:
            tomli.loads(tomli_w.dumps(pyproject))
        except tomli.TOMLDecodeError as e:
            print("Could not create a valid TOML file")
            raise (e)

        with open(self.toml_file, "wb") as output:
            tomli_w.dump(pyproject, output)
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
            # todo: Use Post release
            # # https://packaging.pypa.io/en/latest/_modules/packaging/version.html
            # # [<epoch.!]<version>[.post<build>]
            # semver = parse("v1_18.post1".replace("_", "."))
            # semver.base_version
            # semver.release
            # semver.public
            subprocess.run(["poetry", "version", "prerelease", "-s"], cwd=self.package_path, check=True)
            # subprocess.run(["poetry", "version", "patch", "-s"], cwd=package_path)
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




