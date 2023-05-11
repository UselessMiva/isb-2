import math
from mpmath import gammainc
#task №2.1
bin = list("01110011010101001111101001010100010100100001111001111100010001101011001111111110011100111001101110010011001111001100001100001101")
bin = [eval(i) for i in bin]


def transform(i):
    if i == 0:
        return -1
    else:
        return 1

print(bin)

bin = [transform(i) for i in bin]
print(bin)

Sum = sum(bin) / math.sqrt(128)
print(Sum)
#0.5303300858899106
P = math.erfc(Sum / math.sqrt(2))
print(P)
#0.5958830905651779>0.01
#task №2.2
share=sum(bin)/128
print(share)
#0.5234375
print(2/math.sqrt(128))
con = abs(share-0.5)<2/math.sqrt(128)
print(con)
#true
if con==False:
    P=0;

else:
    V=0;
    for i in range(len(bin)-1):
        if bin[i] != bin[i+1]:
            V+=1
    P = math.erfc(abs(V - 2 * 128 * share * (1 - share)) / (2 * math.sqrt(2 * 128) * share * (1 - share)))
print(P)
#0.05436564357634485>0.01
#task 2.3
dividedList = []
for i in range(0,16):
    dividedList.append(bin[0+8*i:8+8*i])


maxOnesLength = []
for items in dividedList:
    count = 0
    maxCount = 0
    for item in items:
        if item == 1:
            count+=1
            if count>maxCount:
                maxCount=count
        else:
            count = 0
    maxOnesLength.append(maxCount)
print(maxOnesLength)
#[3, 1, 5, 1, 1, 4, 5, 2, 2, 7, 3, 2, 2, 4, 2, 2]
vList = []
count = 0
for i in maxOnesLength:
    if i<=1:
        count+=1
vList.append(count)
count = 0
for i in maxOnesLength:
    if i == 2:
        count+=1
vList.append(count)
count=0
for i in maxOnesLength:
    if i == 3:
        count+=1
vList.append(count)
count=0
for i in maxOnesLength:
    if i>=4:
        count+=1
vList.append(count)
print(vList)
#[3, 6, 2, 5]
# Вычислим хи-квадрат:
xSquare = pow(vList[0]-16*0.2148, 2)/(16*0.2148)+pow(vList[1]-16*0.3672, 2)/(16*0.3672)+pow(vList[2]-16*0.2305, 2)/(16*0.2305)+pow(vList[3]-16*0.1875, 2)/(16*0.1875)
print(xSquare)
#2.164098096005935
Pvalue = gammainc(1.5, xSquare/2)
print(Pvalue)
#0.477724613032321>0.01
