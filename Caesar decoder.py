#encoding: UTF-8
#comment

import getpass
#Import the python files needed for each function in the menu
import encoder
import decoder
import frecuencias

USER = getpass.getuser()
#Calls the coding function on the "encoder.py" file
def coder():
    encryptedMessage = input("Enter the encoded message: ")
    switchIndex = int(input("Enter the switch index: "))
    output = encoder.encode(encryptedMessage, switchIndex)
    return output

#Calls the decoding function on te "decoder.py file
def deCoder():
    codedMessage = input("Enter the coded message: ")
    textInput = input("Enter the text file name (with the .txt extension): ")
    decoder.decoder(codedMessage, textInput)


def bruteForce():
    textInput = input("Enter the coded message\n"
                      "WARNING! This may take a while to finish\n"
                      "Message: ")
    for i in range(1, 27):
        output = encoder.encode(textInput, i)
        if(output == textInput):
            print("ATTEMPT %i: %s (INITIAL VALUE)3" % (i, output))
        else:
            print("ATTEMPT %i: %s " %(i, output))


def main():
    print("---------------------------------------------------")
    print("Welcome %s" %USER)
    print("---------------------------------------------------")
    inputMenu = int(input("Welcome to the Caesar code encoder/decoder.\n"
                          "Please enter the desired interaction on the menu:\n"
                          "1. Encoder.\n"
                          "2. Decoder.\n"
                          "3. BRUTE FORCE DECODING\n"
                          "-1. Exit.\n"
                          "Your option: "))
    print("---------------------------------------------------")
    while(inputMenu != -1):
        if inputMenu == 1:
            print(coder())
        elif inputMenu == 2:
            deCoder()
        elif inputMenu == 3:
            bruteForce()
        elif(inputMenu == -1):
            break
        else:
            print("ERROR!!!! Please enter a valid value.")
            print("---------------------------------------------------")
        inputMenu = int(input("Welcome to the Caesar code encoder/decoder.\n"
                          "Please enter the desired interaction on the menu:\n"
                          "1. Encoder.\n"
                          "2. Decoder.\n"
                          "3. BRUTE FORCE DECODING\n"
                          "-1. Exit.\n"
                          "Your option: "))
        print("---------------------------------------------------")
    else:
        print("Exiting the program...")
        print("---------------------------------------------------")


main()