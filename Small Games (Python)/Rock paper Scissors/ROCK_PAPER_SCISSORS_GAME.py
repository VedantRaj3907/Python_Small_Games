import random
i=0
sum1=0
com=0
print ("")
print("*********************WELCOME TO THE ROCK,PAPER,SCISSORS GAME :)****************\n")
list1=['PAPER','ROCK','SCISSORS']
while (i==0):
    a=input("\nR for Rock\nP for paper\nS for scissors✂✂✂\n:-")    
    b=random.choice(list1)
    print ("\nTHE COMPUTER CHOOSES.......")
    print(b)
    if (a=='p'  and b=='ROCK'):
        print ("\n****You Won this Round:)****\n")
        sum1+=1   
    elif (a=='p' and b=='SCISSORS'):
        print("\n****LOL You lost this Round XD****\n")
        com+=1
    elif (a=='p'  and b=='PAPER'):
        print ("\n****Thats A tie Round :0****\n")
    elif (a=='r'  and b=='ROCK'):
        print ("\n****Thats A tie Round :0****\n")
    elif (a=='r'  and b=='PAPER'):
        print ("\n****LOL You lost XD Round****\n")
        com+=1
    elif (a=='r'  and b=='SCISSORS'):
        print ("\n****You Won this Round :)****\n")
        sum1+=1
    elif (a=='s'  and b=='ROCK'):
        print("\n****LOL You lost this Round XD****\n")
        com+=1
    elif (a=='s'  and b=='PAPER'):
        print ("\n****You Won this Round :)****\n")
        sum1+=1
    elif (a=='s'  and b=='SCISSORS'):
        print ("\n****Thats A tie Round :0****\n")
    else :
        print ("\n****Thats a WRONG INPUT****")
    a1=input("Wanna Play the Next Round press (y/n) :-")
    if (a1=='y'):
        i=0
    elif (a1=='n'):
        print ("\nOK SEE YA :)\n")
        i=1
    else :
        print ("Wrong Input\n")
        i=1
if (com>sum1):
     print ("*"*75)
     print ("You Lost\nThe scores are")
     print ("You Got",sum1,"\nI Got",com)
elif (com==sum1):
    print ("*"*75)
    print ("Thats a Tie Game\n")
    print ("Score are same both got",sum1) 
else :
    print ("*"*75)
    print ("You won\nThe scores are\n")
    print ("You Got",sum1,"\nI Got",com)

            
        
