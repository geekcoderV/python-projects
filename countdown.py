#import files/modules
import time
#main programming sesion
print("Put a random integer down below to count down \n")
#setting the input statement to integer only
question = int(input("Number : "))
while True:
	#while the statement is true it will repeat the process
	question = question - 1
	print(question)
	time.sleep(1)
	#when the countdown has reached zero it will end the while loop statement
	if question == 0:
		print("The countdown is over \n")
		time.sleep(2)
		break