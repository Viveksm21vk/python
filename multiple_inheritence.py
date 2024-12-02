class Singer:
    def sing(self):
        print("Sing a song.")
    def walk(self):
        print("Singer walking.")
class Painter:
    def paint(self):
        print("Paint a scenery.")
    def walk(self):
        print("Painter walking.")
class Artist(Painter, Singer):
    pass

a = Artist()
a.paint()
a.sing()
a.walk()