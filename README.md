# Python_Small_Games

***********************************This repo contains small games created in python using different libraries*********************************************


# Rock Paper Scissors




![Logo](https://img.freepik.com/free-vector/rock-paper-scissors-cartoon-banner-with-human-hands-playing-game-showing-fingers-gestures-friends-challenge-competition-decision-strategy-win-people-playing-fun-vector-illustration_107791-8480.jpg?w=2000)


## Intro to the Game

- User will Choose one of the options
```bash
  Choices = ['Rock','Paper','Scissors']
```
- The AI will randomly choose his choice. (using)
```bash
  import random
  AI = random.choice(Choices)
```
- If user wins then he will get a point
```bash
  User_point += 1
```
- Else the AI will get the point
```bash
  AI_Point += 1
```
- After Every Round We will Ask user if he want to play again
```bash
   a1=input("Wanna Play the Next Round press (y/n) :-")
  if (a1=='y'):
      i=0
  elif (a1=='n'):
      print ("\nOK SEE YA :)\n")
      i=1
  else :
      print ("Wrong Input\n")
      i=1
```
- Continue the Game till user presses "n" or "NO"
- At last after the User will exit we will print the Score for him if he won or lose
```bash
***************************************************************************
User won
The scores are

You Got 5
I Got 3
```


# Tic-Tac-Toe






![Logo](https://ui4free.com/storage/public/images/free-figma-game-tic-tac-toe_1635143619.jpg)


## Intro to the Game

- We Create a Dictonary of 9 positions like this
```bash
  theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
```
- We will Print our Board using the following Function
```bash
  def printBoard(board):
    print(" _"*3)
    print('|'+board['1'] + '|' + board['2'] + '|' + board['3']+"|"+"\t\t1"+'|'+'2'+'|'+'3')
    print('|-+-+-|\t\t-+-+-')
    print('|'+board['4'] + '|' + board['5'] + '|' + board['6']+"|"+'\t\t4'+'|'+'5'+'|'+'6')
    print('|-+-+-|\t\t-+-+-')
    print('|'+board['7'] + '|' + board['8'] + '|' + board['9']+'|'+'\t\t7'+'|'+'8'+'|'+'9')
    print("¯"*7)
```
- Which looks like this at the OUTPUT
```bash
 _ _ _
| | | |         1|2|3
|-+-+-|         -+-+-
| | | |         4|5|6
|-+-+-|         -+-+-
| | | |         7|8|9
¯¯¯¯¯¯¯
```
- We will Switch between the Users of :x: and :o:

- Check of will if any 3 adjecent are of :x: or :o: output looks like this
```bash
    ¯¯¯¯¯¯¯
O Turn (choose Position):- 8
 _ _ _
 _ _ _
|X|O| |         1|2|3
|-+-+-|         -+-+-
|X|O|X|         4|5|6
|-+-+-|         -+-+-
| |O| |         7|8|9
¯¯¯¯¯¯¯

Game Over.

 * O won. *
Do want to play Again?(y/n) :-

```
- Continue the Game till user presses "n" or "NO"
- At last after the User will exit we will print the Score for him if he won or lose
```bash
***************************************************************************
User won
The scores are

You Got 5
I Got 3
```

## Support

Please Give :heart: Star or Follow if you Like! :rosette: :cherry_blossom:







