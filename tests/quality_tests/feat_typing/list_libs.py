# list all libraries that can be found on sys.path
import sys
import os

print(f"{sys.path=}")
for p in sys.path:
    try:
        print(p)
        if p == ".frozen":
            print("- <not scannable>")
            continue
        for file in os.listdir(p):
            if file.endswith('.py') or file.endswith('.mpy'):
                print(f"- {p}/{file}")
    except Exception as e:
        print(f"x folder not found {e}")
