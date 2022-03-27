#!/usr/bin/env python3

import sys
import os
import functions

# import mimetypes

# load in the name of the file.
filename = sys.argv[1]
# set name of the temporary directory to extract to.
tempdir = "Embedded"

# list of accepted filetypes.
accepted_types = [".doc", ".docx"]

file_valid = functions.fileValid(filename, accepted_types)


if not file_valid:
    print("Aborting...")
elif os.path.exists(tempdir):
    print("it seems like the operation has already been completed. Aborting...")
else:
    functions.extractEmbeddedFiles(filename, tempdir)
    functions.flattenEmbeddedFiles(tempdir)
    functions.removeExtractionfiles(tempdir)
    print("complete!")
