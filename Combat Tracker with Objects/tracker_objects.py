import json
from random import randint
from random import seed
import os.path

seed(randint(1, 100))


class Participant:

    def __init__(self, name, modifier, initiative):
        self.name = name
        self.modifier = modifier
        self.initiative = initiative

    def display_participant(self):
        if self.modifier >= 0:
            new_mod = "+" + str(self.modifier)
            print(self.initiative, ":", self.name, "( Dexterity :", new_mod, ")")
        else:
            print(self.initiative, ":", self.name, "( Dexterity :", self.modifier, ")")


class Initiative:

    def __init__(self):
        self.creatures = []
        self.amount = 0

    def update(self, creature_list):
        sorting_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                           "s", "t", "u", "v", "w", "x", "y", "z", "misc", "npcs"]
        while True:
            alph_number = input("Input the creature's alphabetical sorting letter. ---- ")
            if alph_number in sorting_letters:
                with open('' + alph_number + '.json') as data_file:
                    dictionary = json.load(data_file)
                while 'name' not in dictionary.keys():
                    hier = input("Input the creature's name. ---- ")
                    while hier not in dictionary:
                        hier = input("Such a creature doesn't exit. Try again. ---- ")
                    dictionary = dictionary['' + hier + '']
                name = dictionary["name"]
                modifier = int(dictionary["dexterity"])
                initiative = randint(1, 20) + modifier
                creature = Participant(name, modifier, initiative)
                creature_list.append(creature)
                print(creature.name, "has been added to the initiative!")
                return
            else:
                print("Such an alphabetical sorting letter doesn't exit.")

    def import_npcs(self, creature_amount):
        self.creatures.clear()
        creature_amount = int(creature_amount)
        while True:
            if creature_amount == 0:
                blank_list = []
                return blank_list
            else:
                for check in range(0, 15):
                    if creature_amount == check:
                        for i in range(0, creature_amount):
                            self.update(self.creatures)
                        return
                print("Please insert a NON-negative INTEGER from 0 to 15")

    def display_current_list(self):
        for creature in self.creatures:
            creature.display_participant()

    def import_char(self, participant):
        self.creatures.append(participant)
        print(participant.name, "has been added to the initiative!")
        self.amount += 1

    def sort_creatures(self):
        def initiative_sorter(participant):
            return participant.initiative
        self.creatures.sort(key=initiative_sorter, reverse=True)
        return self.creatures


class Player_list:

    def __init__(self):
        self.amount = 0
        self.participants = []

    def create_players(self):
        amount = int(input("How many PCs are participating? ---- "))
        index_pc = 1
        dictionary_file_name = input("What would you like to name the new players file? ---- ")
        dictionary_destination = {"amount": amount}
        while index_pc <= amount:
            value_pc = 'player%d' % index_pc
            player = {}
            player[value_pc] = {"name": "blank", "initiative": 0, "dexterity": 0}
            print("Input information of PC", index_pc)
            player[value_pc].update({"name": input("Name: ")})
            player[value_pc].update({"initiative": 10})
            player[value_pc].update({"dexterity": int(input("Dexterity Modifier: "))})
            dictionary_destination.update({value_pc: player[value_pc]})
            index_pc += 1
        with open('' + dictionary_file_name + '.json', "w") as file:
            json.dump(dictionary_destination, file, indent=2)

    def import_players(self, initiative_list):
        while True:
            dictionary_name = input("What is the name of the Players File you'd like to import? ---- ")
            dictionary_file = '' + dictionary_name + '.json'
            manager = os.path.isfile(dictionary_file)
            if manager:
                with open(dictionary_file) as data_file:
                    dictionary = json.load(data_file)
                i_pc = 1
                updated_list = []
                while i_pc <= int(dictionary["amount"]):
                    value_pc = 'player%d' % i_pc
                    name = dictionary['' + value_pc + '']["name"]
                    modifier = dictionary['' + value_pc + '']["dexterity"]
                    print(name)
                    initiative = int(input("Initiative Score: "))
                    player = Participant(name, modifier, initiative)
                    updated_list.append(player)
                    self.participants += updated_list
                    i_pc += 1
                    updated_list = []
                initiative_list.creatures += self.participants
                return
            else:
                print("Such a Players File doesn't exit.")


# ---------------------------------------------------------------------------------------------------------------------

def main():
    init = Initiative()
    players = Player_list()
    npc_number = int(input("How many NPCs are participating (0 to 15)? ---- "))
    init.import_npcs(npc_number)
    print("Would you like to create a group of players? (Otherwise you'll import an already existing one)")
    check = int(input("Answer: 1 for YES, 2 for NO ---- "))
    if check == 1:
        players.create_players()
    players.import_players(init)
    init.sort_creatures()
    init.display_current_list()


main()
