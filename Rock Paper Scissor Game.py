#Rock Paper Scissor Game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 
import random
user=int(input("What do you choose? Type 0 for Rock,1 forPaper or 2 for Scissors."))
#computer=random.randint(0,2)
computer=0
list=[rock,paper,scissors]
print(list[user])
print("\nComputer chose:\n"+list[computer])
#rules
if user==computer:
  print("Draw")
elif user==0 and computer==2 :
  print("You win!")
elif user==2 and computer==0:
  print("Computer wins")
elif user>computer:
  print("You win!")
else:
  print("Computer wins")
