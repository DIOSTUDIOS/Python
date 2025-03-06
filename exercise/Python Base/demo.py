from pathlib import Path

import os


print(Path.home())

dir = os.path.join(Path.home(), 'flutter', '3.27.4')

print(dir)