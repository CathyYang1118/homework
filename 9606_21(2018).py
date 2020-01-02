#2
'''
def StringClean(InString):
    OutString  = ''
    for i in range(0,len(InString)):
        NextChar = InString[i]
        if NextChar.lower()>='a'and NextChar<='z':
            OutSting += NextChar
    return OutString
'''

#3
'''
while True:
    ID = input('input id')
    if 1<=ID and ID<=10:
        break
    
temp = GetTemperature(ID)

if temp >= HighTemp:
    Alarm()
else:
    if Temp <= LowTemp:
        print('cold')
    else:
        print('Normal')
'''

#5
'''
f = open('ScoreDetails.txt','a')
while True:
    date = input('input the date')
    number = input('input the number')
    if number == ' ':
        break
    while True:
        score = input('input the score')
        if int(score)>=50 and int(score)<=99:
            break
    input_inf = number+date+score
    f.writefile(input_inf)
f.closefile()
'''

#6
'''
def Lighten():
    resoult = False
    for i in range(0,8):
        for j in range(0,8):
            OldValue = picture[i,j]
            NewValue = int(OldValue*1.1)
            if NewValue >= 255:
                NewValue = 255
                resoult = True
    return resoult
'''

#7
'''
def ProcessMarks(Mark):
    Highest = 0
    Total = 0
    for i in range(0,20):
        temp = int(Mark[i])
        total += temp
        if temp >= Highest:
            Highest = temp
    average = Total/20
    print('the average mark is',average,'and the highest mark is',Highest)
'''
