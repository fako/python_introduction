import inflect  # non-standard library for basic natural language formatting


class Tamagotchi(object):

    hunger = None
    happiness = None

    def __str__(self):  # called when formatting to string
        """
        Returns the full name of the Killer Rabbit
        """
        generation = self._inflect.ordinal(self.generation)
        return "{} The {}".format(self.name, generation)

    def __init__(self, name, hunger=20, happiness=30, generation=1):  # constructor
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.generation = generation
        self._inflect = inflect.engine()

    def live(self):
        """
        As killer rabbits grow older they get hungry and sad
        """
        self.hunger += 1
        self.happiness -= 1
        if self.hunger >= 99:
            self.ask_attention()

    def ask_attention(self):
        print("\a")

    def to_record(self):
        """
        Returns all data about a KillerRabbit for population control
        """
        return {
            attr: value
            for attr, value in self.__dict__.items()
            if not attr.startswith("_") and not callable(attr)
        }


class Carnivore(object):

    def ask_attention(self):
        print("Arrrghhh")
        print("\a")
