class sender:
    def __init__(self, codeword) -> None:
        self.codeword = codeword

    def data(self) -> str:
        return self.codeword


class receiver: 
    def __init__(self, codeword) -> None:
        self.codeword = codeword

    def data(self) -> str:
        return self.codeword
    
def getData() -> []:
    return [sender(input()), receiver(input())]


def SPC():
    print("Simple Parity Check")
    data = getData()

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