import random

def play():
  user=input("choose your fav 'r' for stone, 'p' for paper, 's' scerrios")
  computer=random.choice(['r','p','s'])

  if computer == user:
    print("it is a tie")

  if is_win(user,computer):
    print("you won")
  else:
    print("you loose")


#r>p p>s s>r
def is_win(player,oop):
  if(player =='r' and oop == 'p') or (player =='p' and oop =='s') or (player =='s' and oop=='r'):
       print(True)

print(play())
