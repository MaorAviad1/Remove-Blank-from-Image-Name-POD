import os
import re

# specify your path here
path = r"add your folder full path here"

for filename in os.listdir(path):
    if filename.endswith('.png'):
        source = os.path.join(path, filename)
        # replace spaces with hyphens
        new_filename = filename.replace(' ', '-')
        # remove numbers in brackets
        new_filename = re.sub(r'\(\d+\)', '', new_filename)
        destination = os.path.join(path, new_filename)
        os.rename(source, destination)
