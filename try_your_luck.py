import random

colorDict = {
    1: "Red" ,
    2: "Black" ,
    3: "White" ,
    4: "Blue"  ,
    5: "Green" 
 }
 
print('\n\t***Welcome to Our game of Luck by Chance:***\n\n\n ||-> (Rules: Choose your color and check if it match with your luck or not)')

print("\n   1: TEST your luck\t\t\t\t2: Exit\n\n")
j = int(input('\t\t\tENTER YOUR OPTION:'))
e = 1

if j == 1:
    
    print("\n\t\t\t|| Here You Go ||")
    a = input('\n\nEnter Your name:  ')
    while e < 2:
        print('\n\t\tHello ~',a,'~ Choose your color from Below list:\n\nRed : 1    Black : 2\tWhite : 3\tBlue :4   Green : 5\n')
        b = int (input('Enter Your Input for choosing color:  '))
        print('\n',a,' You choose the color : ',colorDict.get(b))
        print('\n\n\t\t Now wait for computer to pick a color if that match with your one or not......\n\n\t\t')
        d = input('\n\t\t\tNow Press Enter to check what computer picked for you??\n\n')
        c = random.choice(list(colorDict.keys()))
        print('THE COMPUTER BABA has picked the color ',list(colorDict.values())[c-1])
        if b == c:
            print('\n\n\n\t\t\t*** HURRAY, It Matched.. ~',a,'~ you are Lucky ***\n\n')
            print('\t\t 1: Play Again\t\t\t 2: Exit\n\n')
            e = int (input('Enter Your Input:  '))
            if e ==2:
                    print("\n\n\t\t|| GoodBye ",a,"  ||\n\n")
        #if e == 1:
            #continue
        else:
            print('\n\n\n\t\t\t !!! SORRY, It is not matched.. ~',a,'~ better Luck Next Time Buddy !!!\n\n')
            print('\t\t 1: Play Again\t\t\t 2: Exit\n\n')
            e = int (input('Enter Your Input:  '))
            if e ==2:
                print("\n\n\t\t|| GoodBye ",a,"  ||\n\n")
        #if e ==2:
            #break 

elif j == 2:
    print("\n\n\t\t|| GoodBye Stranger ||\n\n")
else:
    print('\n\n\t\t Either type correctly or try not to play when you are high & Horny ;)\n\n')
    