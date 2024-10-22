from random import randint

player = input('rock (r), paper (p) or scissors (s)')

print(player, 'vs', end=' ')

chosen = randint(1, 3)
print(chosen)

if chosen == 1:
    computer = 'r'
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
  
elif chosen == 2:
    computer = 'p'
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
  
else:
    computer = 's'
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print(computer)

if player == computer:
    print('draw')

elif player == 'r' and computer == 's':
    print('player wins')

elif player == 'r' and computer == 'p':
    print('computer wins')

elif player == 'p' and computer == 'r':
    print('player wins!')

elif player == 'p' and computer == 's':
    print('computer wins')
