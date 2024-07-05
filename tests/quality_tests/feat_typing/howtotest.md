

`docker run -u 1000 -v ${PWD}/flash/static:/static -v ${PWD}/flash/tests:/tests -it --rm micropython/unix:latest`

-docker run: This is the command to create and start a Docker container.
-u 1000: This sets the user ID (UID) for the process running inside the container to 1000. This is often done for security reasons and to ensure that files created or modified by the container have the expected ownership on the host system.
-v ${PWD}/flash/static:/static: This mounts a volume from your host machine to the container. ${PWD}/flash/static is the path on your host machine, and /static is the path inside the container where the host's directory will be mounted. This allows the container to access and possibly modify files in the flash/static directory of your host machine.
-v ${PWD}/flash/tests:/tests: Similar to the previous volume mount, this mounts the flash/tests directory from your host machine to /tests inside the container. This is useful for running tests that are located on your host machine inside the container.
-it: This option makes the Docker container run in interactive mode with a tty, allowing you to interact with the command line inside the container.
--rm: This option automatically removes the container when it exits. This is useful for cleanup, ensuring that you don't accumulate stopped containers.
micropython/unix:latest: This specifies the Docker image to use for the container. In this case, it's using the latest version of the micropython/unix image, which is a MicroPython environment for Unix-like systems.

## Micropython options
micropython -h
usage: micropython [<opts>] [-X <implopt>] [-c <command> | -m <module> | <filename>]
Options:
-h : print this help message
-i : enable inspection via REPL after running command/module/file
-v : verbose (trace various operations); can be multiple
-O[N] : apply bytecode optimizations of level N

Implementation specific options (-X):
  compile-only                 -- parse and compile only
  emit={bytecode,native,viper} -- set the default code emitter
  heapsize=<n>[w][K|M] -- set the heap size for the GC (default 2097152)



<!-- 
docker run -u 1000 -it --rm micropython/unix:latest
docker run -u 1000 -it --rm micropython/unix:latest micropython -h
docker run -u 1000 -v .:/code -it --rm micropython/unix:latest ls 
-->

`docker run -u 1000 -v .:/code -it --rm micropython/unix:latest micropython check_something.py`



Traceback (most recent call last):
  File "check_anycall.py", line 10, in <module>
TypeError: '_AnyCall' object isn't subscriptable
exit code 1




