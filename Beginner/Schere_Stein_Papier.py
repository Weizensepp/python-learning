#!/usr/bin/env python3

"""
Number guessing Game.
Author: Your Name
Date: 20.05.2025
"""

import random
import sys

def main():
    
    list=["schere", "stein", "papier",]
    wiederholung = True
    zaehlerUser = 0
    zaehlerComputer = 0
        
    while zaehlerComputer<5 and zaehlerUser <5:
        
        while wiederholung:
            
            eingabe = input("Stein, Schere, Papier oder Ende eingeben: \n")
            eingabe = eingabe.lower()
            
            if eingabe == "ende":
                sys.exit()
            
            if eingabe in list:
                
                computerAuswahl=random.choice(list)
                print(f"Auswahl User: {eingabe} \nAuswahl Computer:{computerAuswahl}")
            
                if eingabe == computerAuswahl:
                    print("Keiner Gewinnt, Unentschieden")
                    
                else:
                    if eingabe == "schere":
                        if computerAuswahl == "stein":
                            print ("Computer gewinnt")
                            zaehlerComputer+=1
                        elif computerAuswahl == "papier":
                            print ("User gewinnt")
                            zaehlerUser+=1
                    elif eingabe == "stein":
                        if computerAuswahl == "papier":
                            print ("Computer gewinnt")
                            zaehlerComputer+=1
                        elif computerAuswahl == "schere":
                            print ("User gewinnt")
                            zaehlerUser+=1
                    elif eingabe == "papier":
                        if computerAuswahl == "schere":
                            print ("Computer gewinnt")
                            zaehlerComputer+=1
                        elif computerAuswahl == "stein":
                            print ("User gewinnt")
                            zaehlerUser+=1
                            
                if zaehlerComputer == 5 or zaehlerUser == 5:            
                    wiederholung = False   
                    
                print ("Zaehlerstand User:", zaehlerUser, "\nZaehlerstand Computer:" ,zaehlerComputer,)    
            else:
                print ("Bitte Stein, Schere, Papier oder Ende wählen")
                wiederholung = True
            
main()