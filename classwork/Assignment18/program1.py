import sys
import os
import time

def DirectoryFileSearch(DirName, Extension):
    Border = "-" * 50
    timestamp = time.ctime()

    LogFile = "FileSearch_%s.log" % timestamp
    LogFile = LogFile.replace(" ", "_")
    LogFile = LogFile.replace(":", "_")

    fobj = open(LogFile, "w")

    fobj.write(Border + "\n")
    fobj.write("Marvellous Directory File Search Log\n")
    fobj.write(Border + "\n")

    if os.path.exists(DirName) == False:
        fobj.write("Directory does not exist\n")
        return

    if os.path.isdir(DirName) == False:
        fobj.write("Given name is not a directory\n")
        return

    for FolderName, SubFolder, FileName in os.walk(DirName):
        for file in FileName:
            if file.endswith(Extension):
                fobj.write(file + "\n")

    fobj.write(Border + "\n")
    fobj.write("Log created at : %s\n" % timestamp)
    fobj.close()


def main():
    if len(sys.argv) != 3:
        return

    DirectoryFileSearch(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
