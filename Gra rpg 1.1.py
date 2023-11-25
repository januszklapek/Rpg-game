import random
import time
from enemis import all_enemies
from characterandenemy import Character
from characterandenemy import Enemy

class Player(Character):
    def __init__(self, name, health, attack, defense, experience=0, level=1):
        super().__init__(name, health, attack, defense)
        self.experience = experience
        self.level = level
        self.alcoholism = 0

    def level_up(self):
        if self.experience >= self.level * 100:
            self.experience -= self.level * 100
            self.level += 1
            self.health += 10
            self.attack += 5
            self.defense += 2
            print(f"{self.name} wbił level {self.level}! Twoje stetystyki się zwiększyły.")

    def use_health_potion(self):
        if self.inventory["Mikstura leczenia"] > 0:
            self.health += 20
            self.inventory["Mikstura leczenia"] -= 1
            print(f"{self.name} użyto mikstury leczenia. +20 hp.")
        else:
            print("Nie masz żadnych mikstór.")

    def rest(self):
        rest_amount = random.randint(1, 15)
        self.health += rest_amount
        print(f"{self.name} wypoczoł i zdobył {rest_amount} hp.")
    
    def dance(self):
            print("Zakończ swój żywot tańcem. Który wybierasz?")
            while True:
                print("1. Belgijka")
                print("2. Makarena")
                print("3. Salsa")
                print("4. Polonez")
                print("5. Walec")
                print("6. Tango")
                print("7. Kozak")
                print("8. Springy")
                print("9. Fright Funk")
                print("10. Pump it up")
                print("11. Crabby")
                print("12. Scootin")
                print("13. Crackdown")
                print("14. Dance Moves")
                print("15. Floss")
                print("16. Fresh")
                print("17. The worm")
                print("18. Disco Fever")
                print("19. The robot")
                print("20. Best Mates")
                print("21. True Heart")
                print("22. Hype")
                print("23. Ranbunctious")
                print("24. Twist")
                print("25. Electro swing")
                print("26. T-Pose")
                print("27. Conga")
                print("28. Nᒷ⍊ᒷ∷ ⊣𝙹リᔑ ⊣╎⍊ᒷ ||𝙹⚍ ⚍!¡")
                print("29. Niechcę juz tanczyć")

                choice = input("Wpisz wybór: ")

                if choice == '1':
                    self.dance(print("Tańczysz Belgijkę "))
                elif choice == '2':
                    self.dance(print("Tańczysz Makarena "))
                elif choice == '3':
                    self.dance(print("Tańczysz Salsa "))
                elif choice == '4':
                    self.dance(print("Tańczysz Poloneza "))
                elif choice == '5':
                    self.dance(print("Tańczysz Walca "))
                elif choice == '6':
                    self.dance(print("Tańczysz Tango "))
                elif choice == '7':
                    self.dance(print("Tańczysz Kozaka "))
                elif choice == '8':
                    self.dance(print("Tańczysz Springy "))
                elif choice == '9':
                    self.dance(print("Tańczysz Fright Funk "))
                elif choice == '10':
                    self.dance(print("Tańczysz Pump it up "))
                elif choice == '11':
                    self.dance(print("Tańczysz Crabby"))
                elif choice == '12':
                    self.dance(print("Tańczysz Scootin "))
                elif choice == '13':
                    self.dance(print("Tańczysz Crackdown "))
                elif choice == '14':
                    self.dance(print("Tańczysz Dance Moves "))
                elif choice == '15':
                    self.dance(print("Tańczysz Floss "))
                elif choice == '16':
                    self.dance(print("Tańczysz Fresh "))
                elif choice == '17':
                    self.dance(print("Tańczysz The worm "))
                elif choice == '18':
                    self.dance(print("Tańczysz Disco Fever "))
                elif choice == '19':
                    self.dance(print("Tańczysz The robot "))
                elif choice == '20':
                    self.dance(print("Tańczysz Best Mates "))
                elif choice == '21':
                    self.dance(print("Tańczysz True Heart "))
                elif choice == '22':
                    self.dance(print("Tańczysz Hype "))
                elif choice == '23':
                    self.dance(print("Tańczysz Ranbunctious "))
                elif choice == '24':
                    self.dance(print("Tańczysz Twist "))
                elif choice == '25':
                    self.dance(print("Tańczysz Electro swing "))
                elif choice == '26':
                    self.dance(print("Pokazujesz dominację nad wysztkimi wrogami!! "))
                elif choice == '27':
                    self.dance(print("Tańczysz Congę"))   
                elif choice == '28':
                    self.dance(print("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))                                     
                elif choice == '29':
                    print("Opuszczasz wybór tańca")

class Shop:
    def __init__(self, player):
        self.player = player

    def enter_shop(self):
        print("\nWitaj w sklepie Bij i Zabij!")
        while True:
            print("\nPrzedmioty na stanie:")
            print("1. Kup mikstórę leczenia (10 złota)")
            print("2. Kup miecz (20 złota)")
            print("3. Kup zbroję (30 złota)")
            print("4. Kup psa (10 złota)")
            print("5. Opuść sklep")

            choice = input("Wpisz wybór: ")

            if choice == '1':
                self.buy_item("Mikstura leczenia", 10, "Mikstura leczenia")
            elif choice == '2':
                self.buy_item("Miecz", 20, "miecz")
            elif choice == '3':
                self.buy_item("Zbroja", 30, "zbroja")
            elif choice == "4":
                self.buy_item("Pies", 10, "Pies")        
            elif choice == '5':
                print("Opuszczasz sklep...")
                break
            else:
                print("Zły wybór. Wpisz poprawny.")

    def buy_item(self, item_name, cost, attribute):
        if "Złoto" in self.player.inventory and self.player.inventory["Złoto"] >= cost:
            self.player.inventory["Złoto"] -= cost
            if attribute not in self.player.inventory:
                self.player.inventory[attribute] = 1
            else:
                self.player.inventory[attribute] += 1
            print(f"Kupiłeś {item_name}!")
        else:
            print("Za mało złota.")
class Bar:
    def __init__(self, player):
        self.player = player
        self.rocknstone = True

    def enter_bar(self):
        print("\nWitaj w barze Kosmopizza!")

        while True:
            print("\nTwój chory umysł widzi takie opcje:")
            print("1. Zamów pizzę hawajską (8 złota)")
            print("2. Poproś o kufel piwa (4 złota)")
            print("3. Kup dziewczynie drinka (10 złota) *in progress*")
            print("4. Zagadaj do krasnoluda przy blacie (godność)")
            print("5. Weź flaszkę na wynos (6 złota)")
            print("6. Opuść Kosmopizzę")

            choice = input("Wpisz wybór: ")

            if choice == '1':
                if "Złoto" in self.player.inventory and self.player.inventory["Złoto"] >= 8:
                    if random.randrange(1,7) != 6:
                        print("Zjadłeś pizzę hawajską w relatywnym spokoju, +15 hp (i +10 masy, grubasie).")
                        self.player.health += 15
                    else:
                        bardamage = random.randrange(15,60)
                        print(f"Za odrażający czyn konsumpcji pizzy hawajskiej, bojownicy Frakcji Separatystycznej Ludzi pobili cię. \n - {bardamage} hp")
                        self.player.health -= bardamage
                    self.player.inventory["Złoto"] -= 8
                else:
                    print("Nie stać cię!")
            elif choice == '2':
                if "Złoto" in self.player.inventory and self.player.inventory["Złoto"] >= 4:
                    self.player.alcoholism += 1
                    print("Twe usta wypełniają się pianą a krasnolud obok kiwa głową z przyzwoleniem. \n+5hp")
                    self.player.health += 5
                    self.player.inventory["Złoto"] -= 4
                else:
                    print("Nie stać cię! \nbiedaku")
            elif choice == '3':
                print()
            elif choice == '4':
                if self.player.alcoholism >= 73 and self.rocknstone:
                    print("Krasnolud w ostatnich minutach swego życia podał ci namiary na swój skarb. \nKoroner oznajmił śmierć z zatrucia alkoholowego, \nA stan twojego portfela znaczne zadowolenie.")
                    self.player.inventory["Złoto"] += 10000
                    self.rocknstone = False
                elif not self.rocknstone:
                    print("Próba rozmowy z dawno martwym znajomym powoduje zdiagnozowanie zaawansowanej schizofrenii. \nLądujesz w szpitalu psychiatrycznym. \nKoniec gry. :(")
                    self.player.health = -500
                    break
                else:
                    print("Matka cię chyba nie nauczyła że z nieznajomymi się nie rozmawia. Nawet jeśli, on to zaraz załatwi.")
                    time.sleep(1)
                    if random.randrange(1,100) > 95:
                        print("SOAP TRUSTED YOU!")
                        time.sleep(1)
                        print("Lądujesz ze zmiażdżoną toporem głową w śmietniku. Z nieznajomymi się nie rozmawia. \nKoniec gry :(")
                        self.player.health = -500
                        break
                    else:
                        print("Łupie cię w głowe i upadasz na ziemię pod wływem grawitacji ")
            elif choice == '5':
                self.buy_item("Flaszki", 6, "Flaszki")
            elif choice == '6':
                if random.randrange(1,5) == 4:
                    bardamage = random.randrange(1,20)
                    print(f"W trakcie próby ujścia z życiem oberwałeś szklaną butelką w plecy \n Krasnolud zadał ci {bardamage} obrażeń.")
                    self.player.health -= bardamage
                else:
                    print("Wyszedłeś z baru żywy...")
                break
            else:
                print("Zły wybór. Wpisz poprawny.")
    def buy_item(self, item_name, cost, attribute):
        if "Złoto" in self.player.inventory and self.player.inventory["Złoto"] >= cost:
            self.player.inventory["Złoto"] -= cost
            if attribute not in self.player.inventory:
                self.player.inventory[attribute] = 1
            else:
                self.player.inventory[attribute] += 1
            print(f"Kupiłeś {item_name}!")
        else:
            print("Za mało złota.")
class Game:
    def __init__(self):
        self.player = None
        self.enemies = [
            Enemy(name="Szkielet Orka", health=50, attack=15, defense=5, experience=25, loot=["Złoto", "Mikstura leczenia"]),
            Enemy(name="Gromada szczórów ze wścieklizną", health=70, attack=10, defense=8, experience=30, loot=["Miecz", "Zbroja"]),
            Enemy(name="Król Michał Korybut Wiśniowiecki ", health=100, attack=20, defense=15, experience=50, loot=["Legendarny miecz"]),
            Enemy(name="Jedno oki Goblin zwny Joe", health=40, attack=12, defense=3, experience=20, loot=["Złoto"])
        ]
        self.shop = None
        self.bar = None

    def print_welcome(self):
        print("Witaj w grze RPG!")
        time.sleep(1)
        print("Twoja przygoda zaraz się zacznie...")
        time.sleep(1)

    def create_player(self):
        player_name = input("Nazwa postaci: ")
        self.player = Player(name=player_name, health=100, attack=20, defense=10)
        self.shop = Shop(self.player)
        self.bar = Bar(self.player)
    def explore(self):
        print("\nWchodzisz do lasu...")
        time.sleep(1)
        enemy = random.choice(self.enemies)
        print(f"Atakuje cie {enemy.name} !")

        if battle(self.player, enemy):
            newgold = enemy.experience//random.randrange(2,10)
            print(f"\nPokonałeś {enemy.name}! Zdobyłeś {enemy.experience} punktów doświadczenia i {newgold} złota")
            self.player.experience += enemy.experience
            self.player.level_up()
            self.player.inventory["Złoto"] += newgold
            enemy.drop_loot()
            time.sleep(1)

    def run_game(self):
        self.print_welcome()
        self.create_player()

        while self.player.is_alive():
            print("\nMenu główne:")
            print("1. Wejdź do lasu")
            print("2. Wejdź do Sklepu")
            print("3. Pokaż statystyki postaci")
            print("4. Użyj mikstury leczenia")
            print("5. Odpocznij")
            print("6. Dance")
            print("7.Wejdź do baru")
            print("8. Wyjdź z gry")

            choice = input("Wpisz wybór: ")

            if choice == '1':
                self.explore()
            elif choice == '2':
                self.shop.enter_shop()
            elif choice == '3':
                self.player.display_status()
            elif choice == '4':
                self.player.use_health_potion()
            elif choice == '5':
                self.player.rest()
            elif choice == '6':
                self.player.dance()
            elif choice == "7":
                self.bar.enter_bar()
            elif choice == '8':
            
                print("Opuszczasz grę...")
                break
            else:
                print("Zły wybór. Wpisz poprawny.")

def battle(player, enemy):
    print(f"Atakuje cię {enemy.name}!")

    while player.is_alive() and enemy.is_alive():
        print("\n" + "=" * 30)
        player.display_status()
        enemy.display_status()

        action = input("Co robisz? [a - atak, q - ucieczka]: ")

        if action.lower() == 'a':
            player_damage = max(0, player.attack - enemy.defense)
            enemy_damage = max(0, enemy.attack - player.defense)

            enemy.take_damage(player_damage)
            player.take_damage(enemy_damage)

            print(f"\nZadałeś {player_damage} obrażeń {enemy.name}. {enemy.name} zadał {enemy_damage} tobie.")

        elif action.lower() == 'q':
            print("Uciekłeś z pola walki.")
            return False  

        else:
            print("Zły wybór. Wpisz poprawny.")

    if player.is_alive():
        return True
    else:
        print(f"\n{enemy.name} pokonał ciebie. Koniec gry :( .")
        return False

game = Game()
game.run_game()
