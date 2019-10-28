#encoding: UTF-8

import getpass
#Import the python files needed for each function in the menu
import encoder
import decoder
import frecuencias

USER = getpass.getuser()
#Calls the coding function on the "encoder.py" file
def coder():
    encoder.main()

#Calls the decoding function on te "decoder.py file
def deCoder():
    decoder.main()


def main():
    print("---------------------------------------------------")
    print("Welcome %s" %USER)
    print("---------------------------------------------------")
    inputMenu = int(input("Welcome to the Caesar code encoder/decoder.\n"
                      "Please enter the desired interaction on the menu:\n"
                      "1. Encoder.\n"
                      "2. Decoder.\n"
                      "-1. Exit.\n"
                      "Your option: "))
    print("---------------------------------------------------")
    while(inputMenu != -1):
        if inputMenu == 1:
            coder()
        elif inputMenu == 2:
            deCoder()
        elif(inputMenu == -1):
            break
        else:
            print("ERROR!!!! Please enter a valid value.")
            print("---------------------------------------------------")
        inputMenu = int(input("Welcome to the Caesar code encoder/decoder.\n"
                          "Please enter the desired interaction on the menu:\n"
                          "1. Encoder.\n"
                          "2. Decoder.\n"
                          "-1. Exit.\n"
                          "Your option: "))
        print("---------------------------------------------------")
    else:
        print("Exiting the program...")
        print("---------------------------------------------------")


main()