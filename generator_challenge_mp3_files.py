# Create a generator that will return the complete filename including path of all mp3 files
# The generator should start at a specified directory, the start, which will be provided as
# an argument to the generator function.
# The filenames should include the full path from the specified start directory. So it will
# return a relative path
# To generalise the function, add the file extension as a parameter

import os
import fnmatch


def mp3_pathfilename_generator(start, ext):
    for path, directories, files in os.walk(start, topdown=True):
        for file in fnmatch.filter(files, f"*.{ext}"):
            # absolute_path = os.path.abspath(path)  # absolute path
            # yield os.path.join(absolute_path, file)  # using absolute path
            yield os.path.join(path)  # relative path from 'start' directory


for f in mp3_pathfilename_generator('music', "emp3"):
    print(f)


# mp3_pathfilename_generator(r"C:\Projects\Python\udemy-python-tim", "emp3")