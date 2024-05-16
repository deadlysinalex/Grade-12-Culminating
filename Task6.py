#task 6

outfileName = input("Where do you want to save the data? ") #task1.txt file
outfile=open(outfileName, "a")

def classes():
    outfile=open(outfileName, "a")
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    name = str(input("Enter a name: "))
    age = float(input("Enter their average: "))
    p1 = Person(name , str(age))
    outfile.write(str("Student Identification: " + p1.name +". Their average is: " + p1.age + "\n"))
    outfile.close()
#classes()


def replacing():
    # creating a variable and storing the text 
    # that we want to search 
    search_text = input("Insert text to look for: ")
      
    # creating a variable and storing the text 
    # that we want to add 
    replace_text = input("insert text to replace it:")
      
    # Opening our text file in read only 
    # mode using the open() function 
    with open(outfileName, 'r') as outfile: 
      
        # Reading the content of the file 
        # using the read() function and storing 
        # them in a new variable 
        data = outfile.read() 
      
        # Searching and replacing the text 
        # using the replace() function 
        data = data.replace(search_text, replace_text) 
      
    # Opening our text file in write only 
    # mode to write the replaced content 
    with open(outfileName, 'w') as outfile: 
      
        # Writing the replaced data in our 
        # text file 
        outfile.write(data) 
      
    # Printing Text replaced 
    print("Text replaced") 

def details():
    outfile=open(outfileName, "a")
    classes()
    outfile.close()
    
def deleting():
    try:
        with open(outfileName, 'r') as outfiler:
            lines = outfiler.readlines()
     
            with open(outfileName, 'w') as outfilew:
                for line in lines:
                    dele = input("enter text to delete: ")
                    # find() returns -1 
                    # if no match found
                    if line.find(str(dele)) == -1:
                        outfilew.write(line)
        print("Deleted")
    except:
        print("Oops! somethings wrong")

def main():
    moreadd = "add"
    morereading = "read"
    moredelete = "delete"
    moreupdate = "update"
    moresort = "sort"
    print("\nDo you want to add details? read the data? delete someones data? update their data? or sort the file? (add/read/delete/update/sort. to quit press <Enter>)")
    choice = str(input("Your choice: "))
    if (choice.lower() == moreadd):
        details()
        main()
    elif(choice.lower() == morereading):
        read()
        main()
    elif(choice.lower() == moredelete):
        deleting()
        main()
    elif(choice.lower() == moreupdate):
        replacing()
        main()
    else:
        print("goodbye")

def read():
    outfile=open(outfileName, "r")
    reading = outfile.read()
    print(reading)

def sorting():
    outfile=open(outfileName, "r")
    data = outfile.readlines()
    data.sort()
    for i in range(len(data)):
        print(data[i])
    outfile = open(outfileName, "w")
    outfile.writelines(data)
    outfile.close()

main()
