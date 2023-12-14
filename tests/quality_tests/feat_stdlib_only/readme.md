This folder contains python code snippets that are used to test the quality of the type-stubs. 


The checks are specifically for the micropython-stdlib-stub distribution
that is used as a dependency in most other micropython-*-stubs .

The checks are run against the micropython-stdlib-stub distribution itself, 
and should contain no reference to any other micropython-*-stubs distribution. 

Please avoid references to `umodules` or modules such as `micropython` and `machine` in the snippets here.