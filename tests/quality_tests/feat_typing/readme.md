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

