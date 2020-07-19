
class Pokemon:
    
    def __init__(self, name, level, type):

        self.name = name
        self.level = level
        types = ["normal", "fighting", "flying", "electric"]
        if (type.lower() in types):
            self.type = type.lower()
        else:
            print("Warning: invalid type! This will cause errors!")
        self.max_health = level * 10
        self.current_health = self.max_health
        self.is_knocked_out = False

    #string representation method for print():
    def __repr__(self):
        return (f'{self.name} is level {self.level} and it is of {self.type} type. It has {self.max_health} health points')

    #lose_health method
    def lose_health(self, damage):
        #first check if the pokemon is already knocked_out:
        if (self.is_knocked_out == True):
            print(f'{self.name} is already knocked out and cannot be damaged.')
        #now we update the health and call knock out in case the health points reachs 0:
        else:
            self.current_health -= damage
            if (self.current_health <= 0):
                self.knock_out()
                print(f'{self.name} took {damage} points of damage and was knocked out')
            else:             
                print(f'{self.name} took {damage} points of damage! He has {self.current_health} points of health now.')

    #gain_health method
    def gain_health(self, health):
        #first check if the pokemon is knocked out:
        if (self.is_knocked_out == True):
            print(f'{self.name} is knocked out and cannot be healed.')
        #update the health points and make sure it cannot be higher than max health:
        else:
            self.current_health += health
            if (self.current_health > self.max_health):
                self.current_health = self.max_health
            print(f'{self.name} was healed for {health} points of health! He has {self.current_health} points of health now.')

    #knock_out method
    def knock_out(self):
        self.is_knocked_out = True

    #revive method
    def revive(self):
        if (self.is_knocked_out == True):
            self.is_knocked_out = False
            self.current_health = self.level * 5
            print(f'{self.name} was revived with {self.current_health} points of health!')
        else:
            print(f'{self.name} is not knocked out, therefore revive does not work...')

    #attack method
    def attack(self, opponent):
        damage = self.level * 2
        #check if the attacking pokemon is not knocked out:
        if (self.is_knocked_out == False):
            #checking the types to define if it will be super effective or not very effective:
            #normal will do the regular damage to all other types:
            if (self.type == "normal"):
                print(f'{self.name} used Headbutt!')
                opponent.lose_health(damage)
            #fighting pokemons will do double damage to electric and reduced damage to flying pokemons:
            elif(self.type == "fighting"):
                print(f'{self.name} used Mega Punch!')
                if (opponent.type == "electric"):
                    print("It is super effective!")
                    opponent.lose_health(damage * 2)
                elif(opponent.type == "flying"):
                    print("It is not very effective!")
                    opponent.lose_health(damage * 1/2)
                else:
                    opponent.lose_health(damage)
            #flying pokemons will do double damage to fighting and regular damage to the other types:
            elif(self.type == "flying"):
                print(f'{self.name} used Sky Attack!')
                if (opponent.type == "fighting"):
                    print("It is super effective!")
                    opponent.lose_health(damage * 2)
                else:
                    opponent.lose_health(damage)
            #electric pokemons will do double damage to flying pokemons and regular to the other types:
            elif(self.type == "electric"):
                print(f'{self.name} used Thunderbolt!')
                if (opponent.type == "flying"):
                    print("It is super effective!")
                    opponent.lose_health(damage * 2)
                else:
                    opponent.lose_health(damage)
        else:
            print(f'{self.name} is knocked out and cannot attack!')
class Trainer:
    #Trainer initializer:
    def __init__(self, name, pokemons, potions, revives, currently_active):
        self.name = name
        if (len(pokemons) > 6 or len(pokemons) < 1):
            print("Warning! You can't have more than six or less than 1 pokemons, this will cause errors!")
        else:
            self.pokemons = pokemons
        self.potions = potions
        self.revives = revives
        self.currently_active = currently_active
    #Trainer string represantion for print():
    def __repr__(self):
        return f'{self.name} has {len(self.pokemons)} pokemons and {self.potions} potions. He is currently using {self.pokemons[self.currently_active - 1].name}.'

    #use_potion method:
    def use_potion(self):
        print(f'{self.name} tries to use potion...')
        active_pokemon = self.pokemons[self.currently_active - 1]
        #check if there are potions avaiable and than update the health and number of potions left:
        if (self.potions < 1):
            print(f'{self.name} is out of potions, no way to heal {active_pokemon.name}')
        else:
            active_pokemon.gain_health(30)
            self.potions -= 1
            print(f'{self.name} have {self.potions} left...')

    #revive method:
    def revive(self, chosen):
        print(f'{self.name} tries to use revive...')
        #define the pokemon to use revive:
        pokemon_chosen = self.pokemons[chosen - 1]
        #check if there are revives avaiable and than update the health and number of revives left:
        if (self.revives < 1):
            print(f'{self.name} is out of revives, no way to revive {pokemon_chosen.name}')
        else:
            pokemon_chosen.revive()
            self.revives -= 1
            print(f'{self.name} have {self.revives} revives left...')

    #attack method:
    def attack(self, opponent):
        active_pokemon = self.pokemons[self.currently_active - 1]
        print(f'{self.name} commands {active_pokemon.name} to attack:')
        opponent_active_pokemon = opponent.pokemons[opponent.currently_active - 1]
        #after defining the current pokemons, call the pokemon attack method using the opponent pokemon as argument:
        active_pokemon.attack(opponent_active_pokemon)

    #switch_pokemon method:
    def switch_pokemon(self, pokemon_chosen):
        #pokemon chosen will be the number of the pokemon in the rolster
        #example ["pikachu", "machop", "farfet"] pikachu is the 1, machop is 2, farfet is 3
        if (pokemon_chosen > (len(self.pokemons) + 1) or pokemon_chosen < 1):
            print("Invalid Pokemon choice!")
        else:
            print(f'{self.name} retreats {self.pokemons[self.currently_active - 1].name}...')
            if (self.pokemons[pokemon_chosen - 1].is_knocked_out == False):
                self.currently_active = pokemon_chosen
                pokemon_to_switch = self.pokemons[self.currently_active - 1]
                print(f'{self.name} chooses {pokemon_to_switch.name} to battle!')
            else:
                print(f'{self.pokemons[pokemon_chosen - 1].name} is knocked out, try again using another choice of pokemon!')

#blue rolster:
pikachu = Pokemon("Pikachu", 20, "electric")
cleffairy = Pokemon("Cleffairy", 11, "normal")
pidgeot = Pokemon("Pidgeot", 36, "flying")
hitmonchan = Pokemon("Hitmonchan", 22, "fighting")

#red_rolster
electabuzz = Pokemon("Electabuzz", 25, "electric")
primeape = Pokemon("Primeape", 40, "fighting")
fearow = Pokemon("Fearow", 34, "flying")
jigglypuff = Pokemon("Jigglypuff", 16, "normal")

blue_rolster = [pikachu, cleffairy, pidgeot, hitmonchan]
red_rolster = [electabuzz, primeape, fearow, jigglypuff]

#create trainers
blue = Trainer("Blue", blue_rolster, 4, 2, 3)
red = Trainer("Red", red_rolster, 3, 2, 2)

#testing the classes in action!
print(blue)
print("")
print(red)
print("")
red.switch_pokemon(4)
print("")
blue.attack(red)
print("")
blue.attack(red)
print("")
blue.attack(red)
print("")
red.attack(blue)
print("")
red.switch_pokemon(1)
print("")
red.switch_pokemon(4)
print("")
red.revive(4)
print("")
red.switch_pokemon(4)
print("")
print("")




