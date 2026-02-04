import os

def main():
    FileName = input("Enter File Name : ")

    Ret = os.path.exists(FileName)

    if Ret == True:
        print("File Exists")
    else:
        print("File not Exists")

if __name__=="__main__":
    main()
