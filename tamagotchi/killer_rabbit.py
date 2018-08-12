from random import choice  # random choice from any sequence (list, str, etc.)

from .base import Carnivore, Tamagotchi


class KillerRabbit(Carnivore, Tamagotchi):  # multi class inheritance
    """
    Killer Rabbits are furious animals living near The Cave of Caerbannog.
    """

    def play(self, game, fun=1):
        """
        Playing makes killer rabbits happy :D
        """
        print(
            "{} played {}".format(self, game)  # formatting is a bit too verbose
        )
        self.happiness += fun

    def feed(self, *args, **food):  # catch all arguments and keyword arguments
        """
        Eating makes killer rabbits less hungry
        """
        items = [
            ("yummie", arg,)  # tuples are immutable lists
            for arg in args
        ]
        items += food.items()
        for taste, nutrients in items:  # tuple unpacking in loop
            print("{} ate {} and it was {}".format(self, nutrients, taste))
        self.hunger -= 1

    def __add__(*args):
        """
        A killer rabbit + a killer rabbit = more killer rabbits :O
        """
        for rabbit in args:
            rabbit.happiness += 50
        guardian = choice(args)
        return KillerRabbit(
            name=guardian.name,
            generation=guardian.generation + 1
        )
