#Simple Parity Check
def SPC(): 
    senderData = input()
    recieverData = input()

    ## sender side
    if senderData.count("1")%2 == 0:
        senderData+="0"
    else:
        senderData+="1"
    print("Codeword:" + senderData)

    ## reciever side 
    print("Dataword: ", end="")
    if recieverData.count("1")%2 == 0:
        print("Accepted")
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

#CheckSum       
def CS():
    data = input().replace(" ","")

    ## Using python's libraries int() and bin()
    ## Converting binary to decimal and 
    dataWords = [
        int(data[0:8], 2),
        int(data[8:16],2),
        int(data[16:24],2),
        int(data[24:32],2),
        int(data[32:40],2)
    ]

    ## Getting the Sum of all the datawords then converting it back to binary
    netSum = bin(sum(dataWords))
    ## removing the '0b' added by the bin() function
    netSum = str(netSum)[2:]
    
    ##checking if the new len is greater than 8 bits and doing redoing the same process above
    if len(netSum) > 8:
        bound = len(netSum) - 8
        temp = int(netSum[0: bound],2)
        netSum = int(netSum[bound:], 2)
        netSum = bin(temp+netSum)[2:]
    
    ## Checking if all are 1's
    if str(netSum).count("0") == 0:
        print("Accept data")
    else:
        print("Checksum error detected.")

#Cyclic Redundancy Check
def CRC():
    print("not yet")
    ## Using python's libraries int() and bin()

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