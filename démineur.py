import tkinter
import random

gameOver = False
score= 0
verification=0

def joueur():
    creer_terrainMine(terrainMine)
    fenetre= tkinter.Tk()
    configuration(fenetre)
    fenetre.mainloop()

terrainMine=[]
def creer_terrainMine(terrainMine):
    global verification
    for rangee in range(0,10):
        listeRangee =[]
        for colonne in range(0,10):
            if random.randint(1,100) <20:
                listeRangee.append(1)
            else:
                listeRangee.append(0)
                verification = verification +1
        terrainMine.append(listeRangee)
    printTerrain(terrainMine)
    
def printTerrain(terrainMine):
    for listeRangee in terrainMine:
        print(listeRangee)

def configuration(fenetre):
    for numeroRangee, listeRangee in enumerate(terrainMine):
        for numeroColonne, entreeColonne in enumerate(listeRangee):
            if random.randint(1,100) < 25:
                carre = tkinter.Label(fenetre, text = "    ", bg=  "darkgreen")
            elif random.randint(1,100) >75:
                carre= tkinter.Label(fenetre, text= "    ", bg= "seagreen")
            else:
                carre= tkinter.Label(fenetre, text= "    ", bg= "green")
            carre.grid(row = numeroRangee, column= numeroColonne)
            carre.bind("<Button-1>", clic)

def clic(event):
    global score
    global gameOver
    global verification
    carre = event.widget
    rangee= int(carre.grid_info()["row"])
    colonne = int(carre.grid_info()["column"])
    texte = carre.cget("text")
    
    if gameOver ==False:
        if terrainMine[rangee][colonne] ==1:
            gameOver = True
            carre.config(bg="red")
            print("Game Over! Tu as touché une bombe!")
            print("Ton score: ", score)
        elif texte == "    ":
            carre.config(bg = "brown")
            totalbombes= 0
            if rangee < 9:
                if terrainMine[rangee+1][colonne] ==1:
                    totalbombes = totalbombes + 1
                                        
            if rangee > 0:
                if terrainMine[rangee-1][colonne] ==1:
                    totalbombes = totalbombes + 1
                    
            if colonne > 0:
                if terrainMine[rangee][colonne-1] ==1:
                    totalbombes = totalbombes + 1
                    
            if colonne < 9:
                if terrainMine[rangee][colonne+1] ==1:
                    totalbombes = totalbombes + 1
                    
            if rangee > 0 and colonne > 0:
                if terrainMine[rangee-1][colonne-1] ==1:
                    totalbombes = totalbombes + 1
                    
            if rangee < 9 and colonne > 0:
                if terrainMine[rangee+1][colonne-1] ==1:
                    totalbombes = totalbombes + 1
                    
            if rangee > 0 and colonne < 9:
                if terrainMine[rangee-1][colonne+1] ==1:
                    totalbombes= totalbombes + 1
                    
            if rangee <9 and colonne <9:
                if terrainMine[rangee+1][colonne+1] ==1:
                    totalbombes = totalbombes + 1
                    
            carre.config(text=" "+str(totalbombes)+ " ")
            verification = verification - 1
            score = score + 1
            if verification ==0:
                gameOver = True
                print("Bravo, tu as trouvé tous les carrés non minés.")
                print("Ton score:", score)
                    


joueur()
            



