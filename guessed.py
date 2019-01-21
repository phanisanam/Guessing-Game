exit=0;
s1=0;
s2=0;
print("Welcome  to guessing game");
print("\n");
print("RULES:");
print("-------------");
print("Here we roll the dice and players would guess the number")
print("if you guess correctly you will get 10 points");
print("if you guess wrong you lose 2 points");
print("if both are wrong each lose one point")
import random
while exit!="e":
 print("Let's Roll the Dices");
 p1=int(input("Player-1:guess your  number"))
 p2=int(input("Player-2:guess your number"))
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
    print("[       0       0      ]")
    print("[                        ]")
    print("[            0          ]")
    print("[                        ]")
    print()
 elif  number==4:
    print("[        0       0      ]")
    print("[                         ]")
    print("[                         ]")
    print("[        0       0      ]")
    print("[                         ]")
    print()
 elif  number==5:
    print("[      0         0     ]")
    print("[                        ]")
    print("[            0          ]")
    print("[                        ]")
    print("[      0         0     ]")
    print()
 else:
    print("[      0       0     ]")
    print("[                      ]")
    print("[      0       0     ]")
    print("[                      ]")
    print("[      0       0     ]")
 if number==p1:
     print("player one is correct");
     s1=s1+10;
     s2=s2-2;
     print("\n");
     print("SCORE:");
     print("\n");
     print("player-1  score is:",s1);
     print("player-2 score is:",s2);
 elif number==p2:
     print("player Two is correct");
     s2=s2+10;
     s1=s1-2;
     print("\n");
     print("SCORE:");
     print("\n");
     print("player-1  score is",s1);
     print("player-2  score is:",s2);
 else:
     print("both players are Wrong");
     s1=s1-1;
     s2=s2-1;
     print("\n");
     print("SCORE:");
     print("\n");
     print("player-1 score is:",s1);
     print("player-2 score is:",s2);
     pass
 if s1>s2:
     print("\n");
     print("player-1 is leading");
 elif s2>s1:
     print("\n");
     print("player-2 is leading");
 else:
     print("\n");
     print("both having same score ");
 print("Type  e  to exit (or) you can play again ")
 exit=input()
 if exit=="e":
     if s1>s2:
         print("\n");
         print("RESULT")
         print("\n");
         print("Congratulations!- - player-1");
         print("you are the winner");
         print("you beat your opponent by {2} points".format(s1,s2,s1-s2))
     elif s2>s1:
         print("\n");
         print("RESULT");
         print("\n");
         print("Congratulations! - - player-2");
         print("you are the winner");
         print("you beat your opponent by {2} points".format(s1,s2,s2-s1))
     else:
         print("RESULT");
         print("\n");
         print("The game is tie");
    
