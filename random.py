from datetime import datetime

now = datetime.now().time() # time object
def decimalToBinary(n):
    return int(bin(n).replace("0b", ""))

state = decimalToBinary(int(str(now).split('.')[-1]))

result = []
for i in range(500):
    result.append(state & 1)
    newbit = (state ^ (state >> 3) ^ (state >> 12) ^ (state >> 14) ^ (state >> 15)) & 1
    state = (state >> 1) | (newbit << 15)
def binaryToDecimal(n):
    return int(n,2)

print(binaryToDecimal(''.join(map(str, result))))