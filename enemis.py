from characterandenemy import Character
from characterandenemy import Enemy
all_enemies = [
    Enemy(name="Szkielet Orka", 
          health=50, 
          attack=15, 
          defense=5, 
          experience=25, 
          loot=["Złoto", "Mikstura leczenia"]),

    Enemy(name="Gromada szczórów ze wścieklizną", 
          health=70, 
          attack=10, 
          defense=8, 
          experience=30, 
          loot=["Miecz", "Zbroja"]),

    Enemy(name="Król Michał Korybut Wiśniowiecki ", 
          health=100, 
          attack=20, 
          defense=15, 
          experience=50, 
          loot=["Legendarny miec"]),

    Enemy(name="Jedno oki Goblin zwny Joe", 
          health=40, 
          attack=12, 
          defense=3, 
          experience=20, 
          loot=["Złoto"])]
