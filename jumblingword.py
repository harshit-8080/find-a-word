import random
def getword():
    l=["computer","science","windows","rainbow","punishment","pillow","mercury","switch","saturday","nailcutter","toothpaste"]
    word=random.choice(l)
    return word
def jumble(jumbleword):
    jumbleword=random.sample(jumbleword,len(jumbleword))
    jumbleword="".join(jumbleword)
    return jumbleword
#def intro():
   # player1=input("Enter Your Name Player1")
   #player2=input("Enter Your Name Player2")
def game():
    player1=input("Enter Your Name Player1")
    player2=input("Enter Your Name Player2")
    point1=0
    point2=0
    j=1
    while(j==1):   
      word=getword()
      newword=jumble(word)
      print("Q.Guess The Correct Word Of This Jumbled Word",newword,"?");
      print("---------------------------------------------------------")
      print(player1," Enter Your Guess word-")
      enterword=input()
      if enterword==word:
          print("hurrrryyy You are right-----")
          point1+=1
          print("Your Point Is=",point1)
          print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
      else:
         print("Soory your Guess Is Wrong Better luck Next Time")
         print("Your Point Is=",point1)
         print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
          
      word=getword()
      newword=jumble(word)
      print("Q.Guess The Correct Word Of This Jumbled Word",newword,"?");
      print("---------------------------------------------------------")
      print(player2," Enter Your Guess word-")
      enterword=input()
      if enterword==word:
          print("hurrrryyy You are right-----")
          point2+=1
          print("Your Point Is=",point2)
          print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
          print("Do You Want To Continue Press 1 Else Press 0-----")
          j=int(input())
          
      else:
          
         print("Soory your Guess Is Wrong Better luck Next Time")
         print("Your Point Is=",point2)
         print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
         print("Do You Want To Continue Press 1 Else Press 0-----")
         j=int(input())
         if j==0:
          if point1>point2:
             print("--------",player1," Wins The Game","---------")
          elif point2>point1:
             print("--------",player2,"Wins The Game","----------")
          else:
             print("----------SCORE IS LEVEL----------")
         
print("Welcome HERE")
x=int(input("Do You Want To Play The Game Press 1 Else Press0------"))
if x==1:
    game()
    print("Thanku You Have a Good Day----")
   
else:
    print("Thanku You Have a Good Day")
      
    
    
