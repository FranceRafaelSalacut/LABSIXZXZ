def SPC():
    print("Simple Parity Check")
    
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