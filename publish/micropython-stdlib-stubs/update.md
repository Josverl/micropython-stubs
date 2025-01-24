This is a short description of the steps taken to create or update the stubs for the micropython-stdlib-stubs distribution.
this package is built using `uv build` and published using `uv publish`.

## There are two possible reasons to rebuild 
 1. Rebuild in order to update from the reference-stubs or ducument-stubs. This will use the same typeshed stubs, and infuse or enrich them with new information from MicroPython.
 2. Rebuild in order to update to a newer version of theof the typeshedrepo.for this you will need to manually advance the typeset repo to a newer version. Perhaps the newest versionand then rerun the update script it might be that due to the changes in the base 5 stubs that you'll need to make updates to the updatescript in order to accommodate for that.

*Steps*
 - clone the typeshed repository
    ```bash	
    cd repos
    git clone https://github.com/python/typeshed.git
    cd typeshed
    git checkout <commit-hash>
    ```
- update the version in pyproject toml to the new version ( .postnn)

- from the publish/micropython-stdlib-stubs directory
    - run `python update.py`

- update and publish the micropython-stdlib-stubs package
    ```bash
    uv publish
    ```

- commit the changes to the micropython-stdlib-stubs repository
    






