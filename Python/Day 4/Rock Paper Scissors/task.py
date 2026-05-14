
import random
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



game = [rock, paper, scissors]
user = int(input("\n0 --> rock\n1 --> paper\n2 --> scissors\nEnter your input: "))

print(game[user])
comp = random.randint(0,2)
print("computer chose")
print(game[comp])

if comp>user:
    print("comp wins")
elif user>comp:
    print("u win")
else:
    print("draw")

    #####