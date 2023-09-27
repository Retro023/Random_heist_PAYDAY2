import random

#the heists ai and diff lists
heists = ["First_World_Bank","Heat_Street","PanicRoom","GreenBridge","Diamond_Heist","Slaughterhouse","No-Mercy","Counterfeit","Undercover","Four_Stores","Jewelry_Store","Ukrainian_Job","Mallcrasher","Bank_Heist","Nightclub","Watchdogs","Firestarter","Big_Oil","Framing_Frame","Rats","Diamond_Store","Safe_House_Nightmare","Transport_road","Transport_docks","Train_Heist","GO_Bank","Election_Day","Shadow_Raid","The_Big_Bank","Hotline-Miami","Art_Gallery","Hoxton_Breakout","White_Xmas","The_Diamond","the Bomb_Dockyard","The Bomb_Forest","Cook_Off","Car_Shop","Hoxton_Revenge","Meltdown","The_Alesso_Heist","Golden_Grin_Casino","Aftershock","Lab_Rats","Beneath_the_Mountain","Birth_of_Sky","Santa's_Workshop","Goat_Simulator","Murky_Station","Boiling_Point","The_Biker_Heist","Safe_House_Raid","Prison_Nightmare","Stealing_Xmas","Scarface_Mansion","Brooklyn 10-10","Alaskan_Deal","Cursed_Kill_Room","Brooklyn_Bank","Breakin_Feds","Henry's_Rock","Shacklethorne_Auction","Hells_Island" ,"The_White_House","Border_Crossing","Border_Crystals","San_Martín" "Bank,Breakfast_in_Tijuana","Buluc's_Mansion","Dragon_Heist","The_Ukrainian_Prisoner","Black_Cat","Mountain_Master","Midland_Ranch","Lost_In_Transit","Hostile_Takeover","Crude_Awakening"]
difficulty = ["normal","hard","very_hard","overkill","deathwish","death_sentence"]
AI = ["Yes","No"]

# printing the random choice
random_heist = random.choice(heists)
random_diff  = random.choice(difficulty)
random_ai = random.choice(AI)
# the results
print(f"Your random heist is:", random_heist,"the difficulty is", random_diff, "are you allowed ai:", random_ai)
