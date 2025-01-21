#!/usr/bin/env python3

import argparse
import sys
import os
import subprocess


def changeFileName(fileName):
    fileName, fileExtension = os.path.splitext(fileName)
    fileName = fileName + ".mp4"
    return fileName


def convert(fileNameOldFormat, fileNameNewFormat):
    print(f"[INFO] ffmpeg starting")
    command = [
        "ffmpeg",
        "-i", fileNameOldFormat,
        "-c:v", "libx265",
        "-vtag", "hvc1",
        "-c:a", "copy",
        fileNameNewFormat
    ]

    subprocess.run(command, check=True)


def removeOldFile(fileName):
    print(f"[INFO] removing {fileName}")
    os.remove(fileName)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help="file name")
    args = parser.parse_args()

    fileNameOld = args.file
    fileNameNew = changeFileName(fileNameOld)

    print(f"[INFO] converting {fileNameOld} to {fileNameNew}")

    convert(fileNameOld, fileNameNew)
    removeOldFile(fileNameOld)
