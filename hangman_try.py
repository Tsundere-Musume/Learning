import random

#List of words to choose from
words = ['apple', 'banana','orange', 'executioner']

#Choose a word from above list
word = random.choice(words)

#Count number of letters
l = len(word)

#Convert the chosen word into list
word_list = list(word)

count = 0

disability = ['Legs cutted', 'Hands cutted', 'Ears eaten by dogs', 'Nose stretched','Eyeballs taken out', 'Hanged - Dead']

blank = '-' * l

# Converting '-'s into list
blank_list = list(blank)

chance = 6

txt = ''

while chance > 0:
    check_letter = 0

    #Ask user for a letter
    letter = input("Guess a letter: ")

    if letter in word:
        while check_letter < l:
            if letter == word_list[check_letter]: 
                blank_list[check_letter] = letter 
                check_letter += 1
            else:
                check_letter +=1
        
        txt = ''.join(blank_list)
        chance = 6
    else:
        a = disability[count]
        print(a)
        if a == 'Hanged - Dead':
            break
        count += 1
        chance -= 1
    print(txt, '\n')
    if txt == word: #End program if the chosen word is guessed correctly
        break
