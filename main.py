#User Restart Process
#Defines the entire program as its own function. Allows the user to restart the program without ever stopping the program.
def cipher():
    yes = ('yes', 'y', 'ye', 'yeah', 'yea', 'yah', 'ya', 'yep', 'yeas')
    alpha = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    ask_key = True

    #User Instructions
    if input('Would you like to view the program instructions? ') in yes:
        print("First, enter the string that you want to encrypt or decrypt using the Caesar Cipher. Then the program will ask you for a key.") #Not done, will continue
        input('\n{PRESS ENTER}')

    #User Inputs
        
    #Asks for string that the program will later shift.
    print('What would you like to encrypt/decrypt? ')
    while (string := input('')) == '':
        print('Please enter the string you would like to encrypt/decrypt. ')

    #Asks for the number by which the program will shift the letters of the string. Won't allow non-integers.
    print('What key would you like to use? ')
    while ask_key:
        key = input('')
        ask_key = False
        try:                #Found out about try and except, very useful for checking for integers.
            key = int(key)
        except ValueError:
            ask_key = True




    #Encryption/Decryption Process

    #This section doesn't require any user inputs.

    newstring = ""

    for char in string:
        try:
            if char.islower():
                alpha_num = alpha.index(char.upper())
            else:
                alpha_num = alpha.index(char)

            alpha_num = alpha_num + key

            while alpha_num < 0:
                alpha_num += 26
            while alpha_num > 25:
                alpha_num -= 26

            if char.islower():
                newchar = char.replace(char, alpha[alpha_num].lower())
            else:
                newchar = char.replace(char, alpha[alpha_num])
            newstring += newchar

        except ValueError:
            newstring += char

    print("Here is your shifted string.")
    print(newstring)

    print("Would you like to encrypt/decrypt anything else?")
    if input('') in yes:
        cipher()

cipher()