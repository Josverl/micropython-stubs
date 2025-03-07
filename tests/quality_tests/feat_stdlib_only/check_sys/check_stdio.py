import sys

# verify if stdout and stderr acceppt bytes output 
sys.stdout.write("foofoo")
sys.stdout.write(b"bar")
sys.stdout.flush()


sys.stderr.write("foofoo")
sys.stderr.write(b"bar")
sys.stderr.flush()
