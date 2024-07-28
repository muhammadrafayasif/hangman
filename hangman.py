import random, words
word,lives=random.choice(words.words),5
print(word)
guess=['_' for i in word]
incorrect_guesses=[]
while '_' in guess:
    if lives==0: print("You lost! The word was",word.upper())
    print('\n'+str(guess).replace('\'',' ').replace(',',''))
    letter=input("Guess a letter: ").lower()
    if letter in incorrect_guesses or letter in guess or len(letter)!=1: continue
    for n,j in enumerate(word):
        if letter==j: 
            guess[n]=j
    if letter not in guess: 
        lives-=1
        incorrect_guesses.append(letter.lower())
        print(f"\nYou have {lives} lives remaining!\nIncorrect guesses: {incorrect_guesses}\n")
        if lives==0: print("\nYou lost all your lives!\nThe word was:",word.upper()); break
if '_' not in guess: print(f"\n\nThe word was {word.upper()}\n\nCongratulations! You guessed the correct word!\nYou got it with {len(incorrect_guesses)} incorrect guess(es)!")