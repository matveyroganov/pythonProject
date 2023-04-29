class Hero:

    def go_right(self, metr, long="метров"):
        print(f"Я иду {metr} {long} направо")

    def go_left(self, metr, long="метров"):
        print(f"Я иду {metr} {long} налево")

    def observe(self):
        print("Я осматриваюсь")


hero = Hero()

hero.go_right(50)
hero.go_left(30)
hero.observe()
