#!/usr/bin/env python3

import sys
import os
import zipfile
import shutil


def fileValid(file, allowed_extensions):
    """Check if a file is valid and exists.
    if not, change file_valid to false."""
    if os.path.exists(file):
        if os.path.splitext(file)[1] in allowed_extensions:
            file_valid = True
            # print("File {} has a valid extension.".format(file))

        else:
            file_valid = False
            print(
                "I do not accept {} files. only {} files. Please try again with a valid file.".format(
                    os.path.splitext(file)[1], allowed_extensions
                ),
            )
    else:
        print("file {} is not exist.".format(file))
        file_valid = False

    return file_valid


# this tool extracts the file, looking for all files that start with the
# "word/embeddings" folder structure. these individual files are then
# extracted.
def extractEmbeddedFiles(file, location):

    embeddedPath = os.path.join("word", "embeddings")
    archive = zipfile.ZipFile(file)
    counter = 0
    for obj in archive.namelist():
        if obj.startswith(embeddedPath):
            counter += 1
            print("Extracting {}".format(obj))
            archive.extract(obj, location)
    print("found {} files.".format(counter))


# TODO Given that the files still retain the original file structure, we want
# to flatten it.


def flattenEmbeddedFiles(newlocation):
    """move files in location to however many levels of depth is in the
    directory"""
    # TODO This doesnt work. need to find a solution to capture directory name
    directory = os.getcwd()
    print(directory)
    targetdir = os.path.join(directory, newlocation)
    filelocation = os.path.join(directory, newlocation, "word", "embeddings")

    print("moving files from {} to {}".format(targetdir, filelocation))

    for obj in os.listdir(filelocation):
        print(obj)
        shutil.move(os.path.join(filelocation, obj), targetdir)

    # for obj in os.listdir(location):
    #     shutil.move(obj, location)


def removeExtractionfiles(tempdir):
    tempdir = os.path.join(tempdir, "word")
    shutil.rmtree(tempdir)
