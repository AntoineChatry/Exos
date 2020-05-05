p=int(input("combien de photocopies voulez-vous?"))
if p>0 and p<=10:
    print( p*0.10)
elif p>=11 and p<=30:
    print(10*0.10+(p-10)*0.09)
elif p>30:
    print(10*0.10+20*0.09+(p-30)*0.08)
    
#%%
"""Factoriel"""


def fac(x):
    x=1
    x=int(input("Entrez un nombre: "))
    for i in range(1,x):
        x*=i
        return(x)

#%%
ch1= str(input("Entrez un mot à inverser"))
ch2=""
l.i=len(ch1) -;, 0
while(l > -;):
    ch2[i]=ch1[l]
    l. i= l - i, i + l
print ch2



#%%
fac(5):