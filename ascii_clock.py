def printTime(listOList):
    i = 0
    j = 0
    while(j<5):
        while(i<len(listOList)):
            if(i == len(listOList)-1):
                print(listOList[i][j],end = "")
            else:
                print(listOList[i][j],end = " ")
            i+=1
        print()
        j+=1
        i=0
        
am = """ A  M   M
A A MM MM
AAA M M M
A A M   M
A A M   M
"""

pm = """PPP M   M
P P MM MM
PPP M M M
P   M   M
P   M   M
"""

one = """ 1 
11 
 1 
 1 
111"""

two = """222
  2
222
2  
222"""

three = """333
  3
333
  3
333"""

four = """4 4
4 4
444
  4
  4"""

five = """555
5  
555
  5
555"""

six = """666
6  
666
6 6
666"""

seven = """777
  7
  7
  7
  7"""

eight = """888
8 8
888
8 8
888"""

nine = """999
9 9
999
  9
999"""

zero = """000
0 0
0 0
0 0
000"""

colon = """ 
:
 
:
 """
numDict = {"0":zero.split("\n"),"1":one.split("\n"),"2":two.split("\n"),"3":three.split("\n"),"4":four.split("\n"),"5":five.split("\n"),"6":six.split("\n"),"7":seven.split("\n"),"8":eight.split("\n"),"9":nine.split("\n")}
colonSplit = colon.split("\n")
amSplit = am.split("\n")
pmSplit = pm.split("\n")
cList = [zero.split("\n"),one.split("\n"),two.split("\n"),three.split("\n"),four.split("\n"),five.split("\n"),six.split("\n"),seven.split("\n"),eight.split("\n"),nine.split("\n")]

def interpretTime(time,milTime):
    timeList = time.split(":")
    combinedList = []
    if( not milTime):
        timeList[0] = int(timeList[0])
        if(timeList[0] >= 12):
            if(timeList[0]>12):
                timeList[0]-=12
                timeList[0] = str(timeList[0])
            for i in timeList:
                for j in str(i):
                    combinedList.append(numDict[j])
                combinedList.append(colonSplit)
            combinedList.pop(-1)
            combinedList.append(pmSplit)
        else:
            if(timeList[0] == 0):
                timeList[0] = 12
            timeList[0] = str(timeList[0])
            for i in timeList:
                for j in str(i):
                    combinedList.append(numDict[j])
                combinedList.append(colonSplit)
            combinedList.pop(-1)
            combinedList.append(amSplit)
    else:
        for i in timeList:
            for j in str(i):
                combinedList.append(numDict[j])
            combinedList.append(colonSplit)
        combinedList.pop(-1)
    return combinedList
        
def changeCharacter(char):
    cListIterator = 0#thru each number
    numIterator = 0#thru each row/str in number
    strIterator = 0#thru each letter
    while cListIterator < len(cList):
        while numIterator < len(cList[cListIterator]):
            combiner = ""
            while strIterator < len(cList[cListIterator][numIterator]):
                if (not cList[cListIterator][numIterator][strIterator] == " "):
                    combiner += char
                else:
                    combiner+= cList[cListIterator][numIterator][strIterator]
                strIterator+=1
            strIterator = 0
            cList[cListIterator][numIterator] = combiner
            numIterator+=1
        numIterator = 0
        cListIterator+=1
    dictIterator = 0
    while dictIterator < 10:
        numDict[str(dictIterator)] = cList[dictIterator]
        dictIterator += 1
        
    
#    for num in cList:#each number
 #       for numRow in num:#each list in number
#            for string in numRow:#each string in each list
 #               combiner = ""
  #              for letter in string:#each character in each string
   #                 if( not letter == " "):
    #                    combiner+=char
     #               else:
      #                  combiner+=letter
       #         numRow[numRow.find(string)] = combiner

inputTime = input("Enter the time: ")
clockType = input("Choose the clock type (12 or 24): ")
while((not clockType == "24") and (not clockType == "12") ):
    clockType = input("That is not a permissable clock type... try again (12 or 24)")
fillCharacter = input("Enter your preferred character: \n")#\n
while ((not fillCharacter in "abcdeghkmnopqrsuvwxyz@$&*=") and (not fillCharacter == "") ):
    fillCharacter = input("Character not permitted! Try again: \n") #\n
if (not fillCharacter == ""):               
    changeCharacter(fillCharacter)
if (clockType == "24"):
    clockTypeBoolean = True
else:
    clockTypeBoolean = False
printTime(interpretTime(inputTime, clockTypeBoolean))
                        
    
        