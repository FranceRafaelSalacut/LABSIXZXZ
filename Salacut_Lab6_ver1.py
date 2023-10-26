
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

#Two-dimensional Parity Check
def TDPRC():
    data = input()
    error = [0,0]

    ## column checking
    ## Assuming the data is constantly 45 bits
    column = [
        data[0:9],
        data[9:18], 
        data[18:27], 
        data[27:36]#, 
        #data[36:45]
    ]

    ## counting affected row parities
    for x in column:
        if x[:-1].count("1")%2 != int(x[-1]):
            error[0]+=1

    ## Row checking
    ## Assuming the data is constantly 45 bits
    row = []
    temp = []
    for x in range(0,8): #(0,9)
        temp.clear()
        temp.append(data[x])
        for y in range(1,5): 
            temp.append(data[x+(9*y)])
        row.append("".join(temp))
    
    ## counting affected column parities
    for x in row:
        if x[:-1].count("1")%2 != int(x[-1]):
            error[1]+=1

    print("Error count: ", end="")
    if error[0] > 0 or error[1] > 0:
        print((error[0]+1) * (error[1]+1) -1)
    else:
        print("0")
    

def printRC(arr):
    for x in arr: 
        for y in x[:-1] :
            print(y, end=" ") 
        print(" | " + x[-1])
        
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