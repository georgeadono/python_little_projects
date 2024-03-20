#icsd16007, Antonopoulos Georgios

import random

#dialegw random word mesa apo to words.txt
with open("words.txt") as word_file:
    words = word_file.read().split() 
word = random.choice(words)

#gia emfanish 1/3 grammatwn
num =len(word)/3 
if num<=2:
    print("Hint ! Letters of the word:")
    letter=random.choice(word)
    print(letter)

else:
    print("Hint ! Letters of the word:")
    letter=random.choice(word)
    print(letter)
    letter=random.choice(word)
    print(letter)



tries = 0
guess = '_'*len(word)

while (guess != word) and (tries < 5):
    # input apo player
    s = input('Now: "' + guess + '"; Player can guess: ')

    # an o paixths plhktrologhsei panw apo ena xarakthra ton rwtame an vrhke th leksh 
    #an th vrhke kerdizei alliws exei mia prospatheia ligoterh
    if len(s) > 1:
        original = input("If you think you found it type the word:")
        if(original == word):
           break
        else:
            tries += 1

    # an vriskei gramma to vazoume sth leksh 
    guess = ''.join(s if word[i] == s else guess[i] for i in range(len(word)))

    # elegxos an vrethike kapoio gramma alliws mia prospatheia ligoterh 
    if not any(word[i] == s for i in range(len(word))):
        tries+=1

#apotelesma
print('Player {}: word was {}'.format('WINS' if tries < 2 else 'LOSES', word))