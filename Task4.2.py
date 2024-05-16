def repeat(num):
    a=1
    b=1
    i=0
    while i<num:
        print(a,end=',')
        c=a+b
        a=b
        b=c
        i+=1

n=int(input("Enter the number you want to use(no negatives allowed): "))
fib = repeat(n)
print(fib)

def main():
    morefactor = "fibonacci"
    print("\nDo you want to the Fibonacci sequence? (fibonacci or quit press <Enter>) ")
    choice = str(input("Your choice: "))
    if (choice.lower() == morefactor):
        num=int(input("Enter the number you want to use(no negatives allowed: "))
        repeat(num)
        main()
    else:
        print("Goodbye")

main()

