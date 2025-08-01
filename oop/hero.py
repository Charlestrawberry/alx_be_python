class Hero:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.battery = 100

    def hero_health(self):
        
        if self.battery > 10:
            print("Super still got life")
        else:
            print("Battery is empty")


    
    def attack(self):
        print(f"\n{self.name}'s power using:{self.power}")
        self.battery -= 30
        if self.battery == self.health:
            print("Hahahah... I am Ba3 full")
        
        print(f"{self.name}'s battery after attack: {self.battery}")
        self.hero_health()

    def fight_mode(self, opponent):
        damage = 20
        if self.battery <= 0:
            print(f"{self.name} is defeated!!")
            return
        
        print(f"\n {self.name} attacks {opponent.name} with {self.power}")
        opponent.health -= damage
        self.battery -= 90
        
        print(f"{opponent.name}'s health is now {opponent.health}")
        print(f"{self.name}'s battery is now {self.battery}")

        if opponent.health <= 0:
            print(f"{opponent.name} is defeated!")

# subclass for IronMan
class IronMan(Hero):
    def fire_blaster(self):
        print("IronMan is flying with jet boosters!")
# subclass of Panther
class PinkPanther(Hero):
    def mortal_kombat(self):
        print("Pink panther ready to finish any misogynistic guy out there")





# creating Hero objects
Thor = Hero("Thor", 97, "Thor Hammer SMASH!")
Hulk = Hero("Hulk", 98, "HULK Punch SMASH!")
Spiderman = Hero("Spidy", 99, "Spidey web tricks")
PantherPro = PinkPanther("\n PinkyPanther", 89, "Booming with lightray")
CaptainMarvel = Hero("CM", 67, "Lets get to war smash")
# BlackPanther = Hero( "BP", 89, "Got magic powder")
Ironman_Pro = IronMan("IronOre", 91, "Destroying evil")



Thor.fight_mode(Hulk)       # Thor attacks Hulk
Hulk.fight_mode(Thor)       # Hulk attacks back
Spiderman.fight_mode(Thor)  # Spiderman attacks Thor

Ironman_Pro.attack()
Ironman_Pro.fire_blaster()
PantherPro.attack()
PantherPro.mortal_kombat()
print("\nlets print others too")
Thor.attack()
Hulk.attack()
Spiderman.attack()
CaptainMarvel.attack()






