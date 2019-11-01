#encoding: UTF-8
import getpass
#Import the python files needed for each function in the menu
import createTables
import encoder
import decoder
import frecuencias
import terminaltables

import jiCuadrada

USER = getpass.getuser()
#Calls the coding function on the "encoder.py" file
def coder():
    encryptedMessage = input("Enter the encoded message: ")
    switchIndex = int(input("Enter the switch index: "))
    output = encoder.encode(encryptedMessage, switchIndex)
    return output

#Calls the decoding function on te "decoder.py file
def deCoder():
    textInput = input("Enter the coded text: ")
    output = decoder.decoder(textInput)
    customTable = createTables.createCustomTable(textInput)
    print(customTable)
    return output


if __name__ == '__main__':
    print(" ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗     ███████╗███╗   ██╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗ ")
    print("██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    ██╔════╝████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗")
    print("██║     ███████║█████╗  ███████╗███████║██████╔╝    █████╗  ██╔██╗ ██║██║     ██║   ██║██║  ██║█████╗  ██████╔╝")
    print("██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗    ██╔══╝  ██║╚██╗██║██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗")
    print("╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║    ███████╗██║ ╚████║╚██████╗╚██████╔╝██████╔╝███████╗██║  ██    v1.0.0" )
    print("By: Man-Go, Zexceed7, tndr7, RicoVevo & R4$PUT1N")
    print("---------------------------------------------------")
    print("Welcome %s" %USER)
    print("---------------------------------------------------")
    #Input menu
    inputMenu = int(input("Welcome to the Caesar code encoder/decoder.\n"
                      "Please enter the desired interaction on the menu:\n"
                      "1. Encoder.\n"
                      "2. Decoder (Desde el archivo 'toDecode.txt').\n"
                      "3. Brute Force Decoder.\n"
                      "4. Ji Cuadrada. \n"
                      "0. Exit.\n"
                      "Your option: "))
    print("---------------------------------------------------")

    #While cycle: processes the value given in "inputMenu" and sends it to the according function
    while(inputMenu != 0):
        if inputMenu == 1:
            encodedMessage = coder()
            print("Encoded message: %s" % encodedMessage)
        elif inputMenu == 2:
            decodedMessage = deCoder()
            #Creates a table that shows the char average in a text
            sampleTable = createTables.createSampleTable()
            #print(sampleTable)
            print("---------------------------------------------------\n"
                  "%s\n" #decoded message with the swap index
                  "---------------------------------------------------" % decodedMessage)
        elif inputMenu == 3:
            textInput = input("Enter the coded text: ")
            decoder.decode_BruteForce(textInput)
        elif inputMenu == 4:
            textInput = input("Enter the coded text: ")
            jiCuadrada.computeJiSquared(textInput)
        else:
            print("ERROR!!!! Please enter a valid value.")
            print("---------------------------------------------------")
        inputMenu = int(input("Welcome to the Caesar code encoder/decoder.\n"
                          "Please enter the desired interaction on the menu:\n"
                          "1. Encoder.\n"
                          "2. Decoder.\n"
                          "3. Brute Force Decoder.\n"
                          "4. Ji Cuadrada. \n"
                          "0. Exit.\n"
                          "Your option: "))
        print("---------------------------------------------------")


    print("see you soon", USER)
    print("Exiting the program...")
    print("---------------------------------------------------")