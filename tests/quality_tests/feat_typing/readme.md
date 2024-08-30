This folder contains python code snippets that are used to test the quality of the type-stubs. 

base requirements:
    copy typings.py and typing_extensions.py 
    install some stubs 

    docker must be available on the system / CI 
    
create a check_xyz.py file for each of the cases that needs testing.

for each of the check_xyz.py files 

run micropython the micropython unix docker container and run the check script. 
if exit code = 0 : OK 
else : FAIL te test end report the output. 


command to run the tests: 
```bash
docker run -u 1000 -e HOME=/foo -v .:/code -v ./lib:/foo/.micropython/lib --rm micropython/unix:latest micropython check_basics.py
docker run -u 1000 -e HOME=/foo -v .:/code -v ./lib:/foo/.micropython/lib --rm micropython/unix:latest micropython check_anycall.py
docker run -u 1000 -e HOME=/foo -v .:/code -v ./lib:/foo/.micropython/lib --rm micropython/unix:latest micropython check_protocol.py
```
-c "import sys;print(sys.path);import os;print(os.listdir(sys.patch[2]))"
