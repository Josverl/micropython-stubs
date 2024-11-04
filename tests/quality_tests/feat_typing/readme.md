## Run time tests for `typing` module 

This folder contains python code snippets that are used to test the quality of the type-stubs. 

Base requirements:
    copy typings.py and typing_extensions.py to the lib folder ( This is done automatically by the test function) 
    docker must be available on the system / CI
    the 'micropython/unix:{mp_version}' will be used to run micropython. 
    This means that the validation scripts can use only modules that are avaialble on the micropython unix port.
    
Create a check_xyz.py file for each of the cases that needs testing.

for each of the check_xyz.py files 
    run micropython the micropython unix docker container and run the check script. 
    if exit code = 0 : OK 
    else : FAIL the test end report the output. 


The `manual_run.ipynb` notebook allows a quick manual verification and can be used to develop additional checks.


Note:
Docker on Windows/WSL2 is unable to mount folders from a [REFS filesystem](https://learn.microsoft.com/en-us/windows-server/storage/refs/refs-overview).  (nov'24) 


