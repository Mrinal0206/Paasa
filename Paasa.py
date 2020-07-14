import random

min = 1

max = 6

while True:

    print('Mitr kya aap mujhse paasa fekwana chahte hai?')

    answer = input()

    if answer.lower() == 'haa' or answer.lower() == 'y':

      paasa_fek = random.randint(min, max)

      print(f'''

Aapka ank hai ...

{paasa_fek}

      ''')

    elif answer.lower() == 'nahi' or answer.lower() == 'n':

      print('accha...')

      break

    else:

      print('Sahi Sahi jawab dijiye mitr...')