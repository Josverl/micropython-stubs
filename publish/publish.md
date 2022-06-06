

# Publishing 

Publishing is done using poetry 

reqs: 
 - poetry installed and on path
   `pip install poetry` 

 - poetry api key stored in systems secure store or in environment variable `PYPI_API_KEY`
    - **PYPI test**
        - get token from https://test.pypi.org/manage/account/token/
        - store token using `poetry config pypi-token.pypi pypi-YYYYYYYY` 
    - **PYPI Production**
        - get token from https://pypi.org/manage/account/token/
        - store token using `poetry config pypi-token.pypi pypi-XXXXXXXX` 


 - bump version 

    `poetry version prerelease` 
    `poetry version patch` 

 - poetry publish 
    `poetry publish --build -r test-pypi` 
    `poetry publish --build`


