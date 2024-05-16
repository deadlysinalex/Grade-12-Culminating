def sorting():
    txt = input("Enter numbers seperated by a space: ")
    x = txt.split(" ")
    x.sort()
    print(x)
#sorting()

def main():
    moreyes = "yes"
    choice = input("Want to sort more numbers? (yes/no): ")
    if(choice.lower() == moreyes):
        sorting()
        main()
    else:
        print("goodbye")

main()
