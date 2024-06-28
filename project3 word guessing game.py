# word guessing game

import random
def Word_guess():
    words=("Apple","Banana", "mengo", "orange")
    random_word= random.choice(words)
    user_word= ""
    word_index =0
    print(random_word)
    game_finished= False


    while not game_finished is True:
        if (random_word==user_word):
            print(f"game is finished! \n The guessed word is {user_word}")
            game_finished= True
        else:
            latter = input("guess the latter:")
            if (latter ==random_word[word_index]):
                user_word+=latter
                word_index+=1
                print(user_word)
        
        
        


Word_guess()

