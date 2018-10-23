
# coding: utf-8

# In[17]:


# Here importing library time and setting variables
import time
word = "secretword" 
guesses = ''
turns = 13


# In[18]:


# Asking input and welcoming user 
Name = input("What is your name ? ",) 
print("Hello", Name , "! It is time for a hangman game!")


# In[19]:


# Giving time user to guess
time.sleep(1)
print("Start guessing...")
time.sleep(0.2)


# In[20]:


# This repeats if there are more turns than 0 then sets failed to 0
while turns > 0:
    failed = 0
    #This loop replaces the word and turns into underscore
    for char in word:
        if char in guesses:
            print(char),
        else:
            print('_')
            failed += 1
    # If the user gussed underscores you won !
    if failed == 0:
        print('You won !!!')
        break
    print
    
    guess = input('Please give in a character,')
    guesses += guess
    #If letter not in word subtract 1 turn
    if guess not in word:
        turns -= 1
        print('Wrong!')
        print('You have', turns, 'turns')
        # If you lost all the turns you lost
        if turns == 0:
            print('YOU LOSE!!!!!!')


