#encoding: UTF-8

import getpass
USER = getpass.getuser()

def encoder():
    pass


def coder():
    pass


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
            encoder()
        elif inputMenu == 2:
            coder()
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