def CheckCharacter(str):
    if(str=='a'or str=='e'or str=='i'or str=='o'or str=='u'or str=='A'or str=='E'or str=='I'or str=='O'or str=='U'):
        return True
    else:
        return False

def main():
    Ret = 0
    value = str(input("Enter character :"))
    Ret = CheckCharacter(value)

    if Ret==True:
        print("Vowel")
    else:
        print("Constant")

if __name__=="__main__":
    main()
