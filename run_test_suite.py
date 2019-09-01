import os

files = os.listdir()

for f in files:
    if f.startswith("test_"):
        os.system("python3 -m pytest -v " + f + " --durations=0")

