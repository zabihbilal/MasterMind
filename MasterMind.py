# Name: Zabih Bilal


import random	#import the random library to generate random numbers in password by computer

def generatePassword():
#This function generates password automatically for the user to guess
	a=[]	#Empty list to add values
	
	#loop creates list of 5 digits each digit between 0 to 9
	while len(a) < 5:
		rand_num = random.randint(1,9)
		
		#checks if the generated value exists in list regenerate a value and store in list
		''' To avoid duplicate values'''
		if rand_num not in a:	
			a.append(rand_num)

	#returns the list to main
	return (a)
	
def getUserGuess():
#This function ask for input from user with spaces
	x=input(f">  ")	#Ask from user for input
	fn = x.replace(" ","")	#Deletes the space between string input
	
	#returns the user input as a list of int to main
	return list(fn)
	
def reportResult(p,pg):
#This function takes in 2 lists:
	#Password computer generated(As a list)
	#Password user input (As a list)
	''' Compare both the passwords and process'''
	
	cor = 0	#Counter for number of correct numbers guessed in password
	loc = 0	#Counter for number of correct locations of the guessed numbers in the password
	
	#for loop to check every value of guessed password from computer generated password
	for i in range (0,5):
		#if guessed number is present in password add 1 to correct counter
		if pg[i] in p:
			cor += 1
		#if location of guessed number same as number in password add 1 to location counter
		if pg[i] == p[i]:
			loc += 1
	#If location is 5 it means password is correct hence print msg	
	print (f"{cor} of 5 correct digits.\n{loc} of 5 correct location.\n")
	
	
	if loc == 5:
		return True	#if location counter is 5 return bool val true to main 
	else:
		return False #if location counter is not yet 5 return bool val false to main
			
		
def main():
#This Function controls the flow of program

	cnt = 10	#Counter for 10 prompts from user
	print ("\nI've set my password, enter 5 digits in the range [1-9] (e.g. 9 3 2 4 7):\n")

	#Call function generatePassword and store returned value in variable
	passcode = generatePassword()
	
	#while loop for 10 prompts from user to guess and check input
	while cnt > 0:	
		print(f"{cnt} guesses remaining.")
		
		#Call function getUserGuess and store returned value in variable
		passwordguess = getUserGuess()
		
		#converting string elements to int
		for i in range (0,5):
			passwordguess[i]=int(passwordguess[i])
		
		#Calling and passing comp generated passcode and guessed passcode to
		#reportResult and storing the returned bool value in variable
		y=reportResult(passcode,passwordguess)
		
		#if returned value of reportResult is true print msg and ask for playing again
		if y == True:
			print("Drat! You guessed my password! The treasure is yours...")
			
			#ask user to play again store in variable loop
			loop = input("\nWould you like to play again? (y/n): ")
			
			#if loop ans other than y/n keep printing msg
			while loop != 'y' and loop != 'n':
				loop = input("\nWould you like to play again? (y/n): ")
			
			#if loop is y than regnerate another passcode and reset counter to 10
			if loop == 'y':
				print ("\nI've set my password, enter 5 digits in the range [1-9] (e.g. 9 3 2 4 7):\n")
				passcode = generatePassword()
				cnt = 11
			
			#if loop is n than print exit msg and put counter to 0 to break
			elif loop == 'n':
				print("Thanks for playing.")
				break
				cnt = 0
		#Decrement counter of all unsucessful tries
		cnt -= 1
		
		#if counter is 0 print msgs
		if cnt == 0:
			#check y
			#if true it means correct pssword guessed
			if y == True:
				print("Drat! You guessed my password! The treasure is yours...")
			else: #Incorrect password guesses and 0 tries left
				z=' '.join(map(str, passcode)) #convert the comp gen list to string to print in msg
				print(f"You'll never get my treasure! The password was {z}.")
			
			#again ask for playing again store in loop1
			loop1 = input("\nWould you like to play again? (y/n): ")
			
			while loop1 != 'y' and loop1 != 'n':
				loop1 = input("\nWould you like to play again? (y/n): ")
			
			#if loop1 is y than regnerate another passcode and reset counter to 10
			if loop1 == 'y':
				print ("\nI've set my password, enter 5 digits in the range [1-9] (e.g. 9 3 2 4 7):\n")
				passcode = generatePassword()
				cnt = 10
				
			#if loop1 is n than print exit msg and put counter to 0 to break
			elif loop1 == 'n':
				print("Thanks for playing.")
				break
				cnt = 0
			
#Call main to start game
main()