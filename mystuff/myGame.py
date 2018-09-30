from sys import exit
from random import randint
from textwrap import dedent

class Room(object):

    def enter(self):
        print("That means nothing without more details.")
        exit(1)


class Engine(object):

    def __init__(self, room_map):
        self.room_map = room_map

    def start(self):
        current_room = self.room_map.opening_room()
        last_room = self.room_map.next_room('success')

        while current_room != last_room:
            next_room_name = current_room.enter()
            current_room = self.room_map.next_room(next_room_name)

        # be sure to print out the last room
        current_room.enter()

class Success(Room):

    def enter(self):
        print("OK You won.")

class Death(Room):

    sentences = [
    "you idiot, you died.",
    "fucking idiot, you died.",
    "SB, you died.",
    "You are dead man now."
    ]

    def enter(self):
        print(Death.sentences[randint(0,len(self.sentences)-1)])
        exit(1)

class Door(Room):

    def enter(self):
        print(
        dedent("""You travil in a forest, suddenly you see a strange door,
        you can't help to open this door and get into this cave.
        However after you opened the door,
        a strong wind blowed up your stone axe and the axe dropped in a pool.
        Do you want to get the axe back?""")
        )
        answer = input("Yes or Not: ")
        if answer == "Yes":
            print("OK, you walk to pool and a god emerge from the water.")
            return 'axe_room'

        elif answer == 'Not':
            print("OK, you walk out of the cave and nothing happend.")
            exit(1)

        else:
            print("You do not answer the question.You done.")
            return 'death'

class AxeRoom(Room):

    def enter(self):
        print(dedent("""
            There are 3 axes in the god's hand.The god ask you which axe
            is yours,stone one, silver one or gold one?
        """))
        answer = input("Which one> ")
        if answer == "stone one":
            print(dedent("""You are a honesty guy, the god give back your stone
            axe to you, and give the gold one to you as a present. The god also
            tells you that there are more treasures in this cave. Are you
            willing to take advanture?
            """))
            answer = input("Yes or Not> ")
            if answer == "Yes":
                print("OK, you walk to another door and open it.")
                return 'math_room'

            elif answer == 'Not':
                print("You walk out of the cave and get your axe and present.")
                exit(1)

            else:
                print("You do not answer the question.You done.")
                return 'death'

        elif answer == "silver one" or answer == "gold one":
            print("You are not honesty and greedy!")
            return 'death'

        else:
            print("You don't answer the question which isn'r polite to  god")
            return 'death'

class MathRoom(Room):
    pass

class Map(object):

    rooms = {
        'success': Success(),
        'death': Death(),
        'door': Door(),
        'axe_room': AxeRoom(),
        'math_room': MathRoom(),
        # 'fight_room': FightRoom(),
        # 'promise_room':PromiseRoom(),
        # 'check_room': CheckRoom()
    }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.rooms.get(room_name)
        return val

    def opening_room(self):
        return self.next_room(self.start_room)











map = Map('door')
game = Engine(map)
game.start()
