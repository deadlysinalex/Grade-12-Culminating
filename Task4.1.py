#task 4.1
def factor():
    num = int(input("Enter a number to learn the factorial of it: "))
    fact = 1
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,num + 1):
          fact = fact*i
          print("The factorial of",num,"is",fact)

def main():
    morefactor = "factorial"
    print("\nDo you want to factorial? (factorial or quit press <Enter>) ")
    choice = str(input("Your choice: "))
    if (choice.lower() == morefactor):
        factor()
        main()
    else:
        print("Goodbye")

main()
