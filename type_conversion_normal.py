numberInt=12
numberFloat=12.34

numNew = numberInt + numberFloat

print("Data type of numberInt :", type(numberInt))
print("Data type of numberFloat :", type(numberFloat))
print("Value of numberInt :", numberInt)
print("Value of numberFloat :", numberFloat)
print("Value of numNew",numNew)
print("Value of numNew",type(numNew))


numberInt=123
numStr="345"
print("Datatype of numStr before Type casting :",type(numStr))
numStr=int(numStr)
print("Datatype of numStr after Type casting :",type(numStr))
numSum = numberInt + numStr 
print(numSum)