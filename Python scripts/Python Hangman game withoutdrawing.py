
# coding: utf-8

# In[1]:


import time


# In[2]:


Name = input("What is your name ?",) 
print("Hello", Name , "! It is time for a hangman game!")


# In[3]:


time.sleep(1)
print("Start guessing...")
time.sleep(0.2)


# In[4]:


word = "secretword" 
guesses = ''
turns = 13


# In[5]:


while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char),
        else:
            print('_')
            failed += 1
    if failed == 0:
        print('You won !!!')
        break
    print
    guess = input('Please give in a character,')
    guesses += guess
    if guess not in word:
        turns -= 1
        print('Wrong!')
        print('You have', turns, 'turns')
        if turns == 0:
            print('YOU LOSE!!!!!!')


