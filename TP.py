def palindrome():
    

    string = input('Ecrivez votre mot: ')

    string = string.casefold()


    string1 = reversed(string)

    if list(string) == list(string1):
        print("Ce mot est un palindrome")
    else:
       print(" ce mot n'est pas un palindrome")
   
palindrome()

#%%
#eurodollar

def eurodollar():
    euro = 1
    dollar = 1.15
    montant = int(input("montant:"))
    choix = int(input("dollars vers euros tapez 1, euros vers dollars tapez 2:"))
    if choix == 1:
        dollars = montant / dollar
        print("{:.2f}".format(dollars))
    elif choix == 2:
        euros = montant * dollar
        print("{:.2f}".format(euros))
    
eurodollar()
#%%
n=int(input('entrez un nombre entre 1 et 15: '))
for row in range(1,n+1):
    for col in range(1,n+1):
        print(row*col)
    print()
#%%
from turtle import *
color("goldenrod")
shape("turtle")
speed(15)
pensize(5)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
