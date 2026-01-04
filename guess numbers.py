import random
numbers   = list(range(1,100))
while True:
    guess = random.choice(numbers)
    print(guess)
    inp   = input()
    if   inp == 'k':                              
       del numbers[numbers.index(guess):]       
    elif inp == 'b':
         del numbers[:numbers.index(guess)+1]   
    elif inp =='d':
        print('my guess is True!')
        break
