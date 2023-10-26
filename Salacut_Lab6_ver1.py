
#Simple Parity Check
def SPC(): 
    senderData = input()
    recieverData = input()

    ### sender side ###
    if senderData.count("1")%2 == 0:
        senderData+="0"
    else:
        senderData+="1"
    print("Codeword: " + senderData)

    ### reciever side ###
    print("Dataword: ", end="")
    if recieverData.count("1")%2 == 0:
        print(recieverData[:-1])
    else:
        print("Discarded")

def TDPRC():
    print("Two-dimensional Parity Check")

def CS():
    print("Checksum")

def CRC():
    print("Cyclic Redundancy Check")

def userInput():
    switch = {
        1:SPC,
        2:TDPRC,
        3:CS,
        4:CRC
    }
    
    ## Assuming there will be no errors in input
    switch[int(input())]()
def main():
    userInput()

main()