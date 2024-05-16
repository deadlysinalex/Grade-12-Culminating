outfileName = input("Where do you want to add and save the data? (must be same file) ") #task5.2.txt file
outfile=open(outfileName, "a")
def write():
    outfile=open(outfileName, "a")
    n = input("Enter a message or line of text ")
    s = (n + "\n")
    outfile.write(str(s))
    outfile.close()
    print("Text successfully inserted")

def main():
    moredata = "add"
    moreread = "read"
    print("\nDo you want to add more or read? (add/read to quit press <Enter>) ")
    choice = str(input("Your choice: "))
    if (choice.lower() == moredata):
        write()
        main()
    elif (choice.lower() == moreread):
        read()
        main()
    else:
        print("goodbye")

def read():
    outfile=open(outfileName, "r")
    reading = outfile.read()
    print(reading)

main()
