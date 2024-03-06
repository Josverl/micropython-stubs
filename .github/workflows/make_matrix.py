import os, json

# GITHUB_OUTPUT is set by github actions
matrix = {}
# matrix['version'] = ["1"]
matrix['board']=["RPI_PICO", "RPI_PICO_w"]
# output the matrix to a file
if os.getenv('GITHUB_OUTPUT'):
    with open(os.getenv('GITHUB_OUTPUT'), 'a') as file:   #  type: ignore
        file.write(f"boards={json.dumps(matrix)}")
else:
    print(f"boards={json.dumps(matrix)}")
