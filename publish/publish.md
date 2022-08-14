# Publication script : 

``` bash
python .\publish\publish_stubs.py  --help

-p, --port [stm32|esp32|esp8266|rp2]
                                  multiple:   [default: stm32, esp32, esp8266,
                                  rp2]
  -b, --board [GENERIC]           multiple:   [default: GENERIC]
  --pypi / --test-pypi            publish to PYPI or Test-PYPI
  --dry-run                       go though the motions but do not publish
  --force                         create new post release even if no changes
                                  detected
  --clean                         clean folders after processing and
                                  publishing
  -v, --verbose
  --help                          Show this message and exit.

```

# Publishing 

Publishing is done using poetry, so it should be installed

reqs: 
 - poetry installed and on path
   `pip install -r requirements.txt` 
 - poetry api key stored in systems secure store or in environment variable `PYPI_API_KEY`

## One time setup ( per host / environment) 
### PYPI test
   - add repository to poetry config
      `poetry config repositories.test-pypi https://test.pypi.org/legacy/`
   
   - get token from https://test.pypi.org/manage/account/token/
   - store token using `poetry config pypi-token.test-pypi  pypi-YYYYYYYY`
   Note: 'test-pypi' is the name of the repository

### PYPI Production
   - get token from https://pypi.org/manage/account/token/
   - store token using `poetry config pypi-token.pypi pypi-XXXXXXXX` 



  
## Bump version 

   `poetry version prerelease` 
   `poetry version patch` 
   
## Poetry Publish 
   To test 
   - `poetry publish -r test-pypi`
   
   To PyPi
   - `poetry publish --build`




python .\publish\publish_stubs.py  --pypi -V 1.19.1 