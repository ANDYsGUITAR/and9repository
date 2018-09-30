class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def sing_the_first_sentence(self):
        print(self.lyrics[0])


bday_lyrics = ["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"]
happy_bday = Song(bday_lyrics)

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

print("*" * 20)
happy_bday.sing_me_a_song()
print("*" * 20)
happy_bday.sing_the_first_sentence()
print("*" * 20)
happy_bday.sing_me_a_song()
print("*" * 20)
bulls_on_parade.sing_me_a_song()
