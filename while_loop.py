#import files/modules
import time
#main programming session
#integer where to start
print("Put a random integer down below to countdown\n ")
#setting the input statement as integer only
question = int(input("Number here : "))
while True:
    #while loop statement is running 
    question = question - 1
    print(question)
    time.sleep(1)
    #if the loop statement has reached limits it will end the running process and move on to the next programmed
    if question == 0:
        print("You have reached 0")
        break