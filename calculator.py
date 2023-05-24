#import files
import time
#main programming session
def main():
    print("Choose your calculation but if you want to cancel the running project please do Ctrl + C \n + for addition \n - for subtraction \n * for multiplication \n / for division \n")
    time.sleep(1)
    question = input("-> ")
    if question == "+":
        print("Put two random integers down below to add \n")
        time.sleep(1)
        add1 = int(input("First Digit : "))
        add2 = int(input("Second Digit : "))
        equal = add1 + add2
        print("Your equal is " + str(equal))
        time.sleep(1)
        print(main())
    elif question == "-":
        print("Put two random integers down below to subtract \n")
        time.sleep(1)
        sub1 = int(input("First Digit : "))
        sub2 = int(input("Second Digit : "))
        equal1 = sub1 - sub2 
        print("Your sum is " + str(equal1))
        time.sleep(1)
        print(main())
    elif question == "*":
        print("Put two random integers down below to multiply \n")
        time.sleep(1)
        mul1 = int(input("First Digit : "))
        mul2 = int(input("Second Digit : "))
        equal2 = mul1 * mul2 
        print("Your sum is " + str(equal2))
        time.sleep(1)
        print(main())
    elif question == "/":
        print("Put two random integers down below to divide \n")
        time.sleep(1)
        div1 = int(input("First Digit : "))
        div2 = int(input("Second Digit : "))
        equal3 = div1 / div2 
        print("Your sum is " + str(equal3))
        time.sleep(1)
        print(main())
main()