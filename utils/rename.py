"""
Renames files to README.md so that they can be seen on Github without entering.

This is one-time script. It is left here for reference.
"""

import os
import shutil

for path, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.md'):
            new_file_name = os.path.join(path, 'README.md')
            old_file_name = os.path.join(path, f)
            shutil.move(old_file_name, new_file_name)
