#Couple holding hands

def minSwapsCouples(row) -> int:
    #observation: if len(row) = 2N.  len of row is even.  
    #one swap will fix at least one wrong order
    #worst case scenario N wrong seats will take N times of swap.
    #we also know each couple has to sit at 2j ad 2j+1 for all couples to fit in there
    #seems like a key value pair problem.  The key is the seat and value is the couple number.

    N = len(row)
    rowDict ={}
    counter = 0
    
    for i in range(N):
        rowDict[row[i]] = i
    
    for i in range(0,N,2):
        #find couple position
        if row[i]%2 == 0: 
            spouse = row[i] + 1
        else:
            spouse = row[i] - 1

        spouseFinalseat = i + 1
        spouseCurrentseat = rowDict[spouse]

        #switch position:
        if spouseCurrentseat != spouseFinalseat:
            row[spouseCurrentseat] = row[spouseFinalseat]
            row[spouseFinalseat] = spouse            

            rowDict[row[spouseCurrentseat]] = spouseCurrentseat
            rowDict[spouse] = spouseFinalseat

            counter +=1

    return counter     
        
    
print(minSwapsCouples([3,2,0,1]))
        

        

