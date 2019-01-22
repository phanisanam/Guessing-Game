exit=0;

    

def score():
     global s1;
     global s2;
     if number==p1:
       print("{0} is correct".format(n1));
       s1=s1+10;
       s2=s2-2;
       print("\n");
       print("SCORE:");
       print("\n");
       print("{0}   score is:{1}".format(n1,s1));
       print("{0}  score is:{1} ".format(n2,s2));
     elif number==p2:
       print("player Two is correct");
       s2=s2+10;
       s1=s1-2;
       print("\n");
       print("SCORE:");
       print("\n");
       print("{0}  score is{1}".format(n1,s1));
       print("{0}  score is:{1}".format(n2,s2));
     else:
       print("both players are Wrong");
       s1=s1-1;
       s2=s2-1;
       print("\n");
       print("SCORE:");
       print("\n");
       print("{0}  score is{1}".format(n1,s1));
       print("{0}  score is:{1}".format(n2,s2));
     
       


def  summary():
    if s1>s2:
      print("SUMMARY:");
      print("\n");
      print("{0} is leading".format(n1));
    elif s2>s1:
      print("SUMMARY:");
      print("\n");
      print("{0} is leading".format(n2));
    else:
      print("SUMMARY:");
      print("\n");
      print("both having same score ");



def result():
      if s1>s2:
         print("\n");
         print("RESULT")
         print("\n");
         print("Congratulations!- - {0}".format(n1));
         print("you are the winner");
         print("you beat your opponent by {2} points".format(s1,s2,s1-s2))
      elif s2>s1:
         print("\n");
         print("RESULT");
         print("\n");
         print("Congratulations! - - {0}".format(n2));
         print("you are the winner");
         print("you beat your opponent by {2} points".format(s1,s2,s2-s1))
      else:
         print("RESULT");
         print("\n");
         print("The game is tie");
    
    
    

s1=0;
s2=0;
n=1;
print("Welcome  to guessing game");
print("\n");
print("RULES:");
print("-------------");
print("Here we roll the dice and players would guess the number")
print("if you guess correctly you will get 10 points");
print("if you guess wrong you lose 2 points");
print("if both are wrong each lose one point")
import random
n1=str(input("enter the name of player-1:"))
n2=str(input("enter the name of player-2:"))
rounds=int(input("How many rounds you want to play:"))
while exit!="e" and n<=rounds:
 print("Let's Roll the Dices");
 p1=int(input("{0}:guess your  number".format(n1)))
 p2=int(input("{0}:guess your number".format(n2)))
 number=random.choice([1,2,3,4,5,6])
 print("the number is:",number);
 if  number==1:
    print("[                       ]")
    print("[                       ]")
    print("[         0             ]")
    print("[                       ]")
    print("[                       ]")
 elif  number==2:
    print("[                        ]")
    print("[                        ]")
    print("[      0       0         ]")
    print("[                        ]")
    print("[                        ]")
    print()
 elif  number==3:
    print("[                        ]")
    print("[       0       0        ]")
    print("[                        ]")
    print("[            0           ]")
    print("[                        ]")
    print()
 elif  number==4:
    print("[        0       0        ]")
    print("[                         ]")
    print("[                         ]")
    print("[        0       0        ]")
    print("[                         ]")
    print()
 elif  number==5:
    print("[      0         0     ]")
    print("[                      ]")
    print("[            0         ]")
    print("[                      ]")
    print("[      0         0     ]")
    print()
 else:
    print("[      0       0     ]")
    print("[                    ]")
    print("[      0       0     ]")
    print("[                    ]")
    print("[      0       0     ]")
    
    
 score();
 
 summary();
 
 print("Type  e  to for emergency exit ")
 n=n+1;
 exit=input()
 if exit=="e"or n>rounds:
  
     result();
