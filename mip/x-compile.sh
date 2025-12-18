#!/bin/bash

# Save current directory and change to script location
savedDir="$(pwd)"
cd "$(dirname "$0")"

# Run mpy-cross commands
mpy-cross typing.py -O3
mpy-cross typing_extensions.py -O3

for f in *.mpy; do
    echo "Compiled: $f Size: $(stat -c%s "$f" 2>/dev/null || stat -f%z "$f") bytes"
done

# Change back to the saved directory
cd "$savedDir"
