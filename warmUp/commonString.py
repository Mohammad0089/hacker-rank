name = ["renting", "painting", "denting", "flaunting", "venting"]

#find the common suffix 

def commonString(value1 , value2):
    #find the largest value
    #since it is suffix we start from the end 
    commonStr =''
    lenOfV_1 =len(value1) - 1   # len() -1 beacuse in loop we start from 0
    lenOfV_2 =len(value2) - 1
    if (lenOfV_1 > lenOfV_2):
        j = lenOfV_1 # larger str
        for i in range(lenOfV_2,-1,-1):  #loop range is set by smaller string,  since stop point in range function is always one step before the actual number we put -1 so to iterate until 0
            if(value2[i] == value1[j]): # to start at end char of the larger val
               commonStr +=value1[j]
               j-=1
            
            else:
                j-=1
        return commonStr[::-1]
    else:
        j = lenOfV_2 # larger str
        for i in range(lenOfV_1,-1,-1):  #loop range is set by smaller string , since stop point in range function is always one step before the actual number we put -1 so to iterate until 0
            if(value1[i] == value2[j]): # to start at end char of the larger val
               commonStr +=value1[i]
               j-=1
            else:
                j-=1
        return commonStr[::-1] # to reverse the string 


commonStr1=commonString(name[0],name[1])

for val in name:
    commonStr1 = commonString(commonStr1,val)
print("common suffix is: ",commonStr1 )