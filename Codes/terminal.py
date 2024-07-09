# This program picks a random python file from this folder and executes that file.

import subprocess
from pathlib import Path
from random import choice

path = Path()

files = list(path.glob('*.py'))
random_file = choice(files)

print(f"Executing file: {random_file}")

subprocess.run(["py", random_file])

