# How to use the Micro:bit v2 stubs


The [micro:bit type stubs](https://github.com/microbit-foundation/micropython-microbit-stubs) are independently maintained by the microbit foundation and are not part of the micropython-stubs project. Their stubs are currently not published to PyPI, so you will need to clone the repository and set up a sparse clone to get the typing files you need.  
I just want to make it easier to use them with vscode and pylance; below is a process to get you started.__**


Assuming you are using vscode and pylance the below setup should get you started by setting up a sparse clone of just (one of) the typing folder(s) in this repo:

Assuming you have a folder for you project called:  **project_foo**
 
### Create and navigate to the typings directory:

- Open your terminal.
- Navigate to your project_foo folder 
- Create the typings directory if it doesn't exist and navigate into it
- Initialize a new git repository

```
cd project_foo
mkdir typings
cd typings
git init
```

### Add the remote repository:

- Enable sparse-checkout:
- Create a file in .git/info/sparse-checkout and add the path of the folder you want to clone:
- I am assuming you want to clone the lang/en folder. 
  If you want to clone a different folder, replace lang/en with the path of the folder you want to clone.
```
# in the project_foo/typings folder  
git remote add -f origin https://github.com/microbit-foundation/micropython-microbit-stubs.git
git config core.sparseCheckout true
echo "lang/en" >> .git/info/sparse-checkout
```

### Pull from the remote repository:
```
# in the project_foo/typings folder  
git pull origin main
```

## Start VScode
```
cd ..
code .
```

<!-- TODO: may need a setting to allow pylance to look deep into the sparse checked out folder tree  -->