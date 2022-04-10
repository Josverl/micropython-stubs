from pathlib import Path
import subprocess
ver = "v1_18"
port = "esp32"
board = "generic"

stub_package_name = f"micropython-{port}-{board}-stubs"
dest_path = Path("./publish") / stub_package_name

# Add firmware stubs 
# copy ".\stubs\micropython-$ver-$port" "$dest_folder/firmware" -r -Force

# https://www.scivision.dev/windows-symbolic-link-permission-enable/
# Create symlink to firmware stubs
(dest_path/ "firmware").absolute().symlink_to( (Path("./stubs") / f"micropython-{ver}-{port}" ).absolute(), target_is_directory=True)


# todo: 
#  create hastable of all files/modules to include 

# - create/update pyproject.toml
# add a module from each file/folder in the hashtable 

# - create/update readme.md



# create package 
subprocess.run(["poetry", "build" ,"-vvv"], cwd=dest_path)  


subprocess.run(["poetry", "build" ,"-vvv"], cwd=dest_path)  

cd publish

# check package for validity
mypy $stub_package_name


popd 
