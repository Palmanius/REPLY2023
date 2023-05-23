Limit = 100000 #set upper limit for Hamming numbers
HammNum = [] #initial list which will be populated with hamming numbers

def Hamming(i,j,k): #procedure to search for numbers using i,j,k as exponents
    global HammNum, Limit #ensure our procedure can access Lmit and list of numbers
    Number = 2**i * 3**j * 5**k #calculate hamming number with current exponents
    if Number < Limit: #limiting our search until value is rached
        if Number not in HammNum: #ensure no duplicate numbers are stored
            HammNum.append(Number) # adds number to the list
        #recursevely try all different combinations of exponents
        Hamming(i+1,j,k) #increase exponent i
        Hamming(i,j+1,j) #increase exponent j
        Hamming(i,j,k+1) #increase exponent k

Hamming(0,0,0) #run procedure with initial values of exponents
HammNum.sort() #sort all found numbers
print(HammNum) #print the solution