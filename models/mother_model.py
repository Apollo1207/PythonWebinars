from abc import ABC, abstractmethod


class AbstractParent(ABC):
    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError


class Mother:
    def __init__(self, age=0):
        self.age = age
        print("mother consctructor")

    def do_work(self):
        print("I'm working")

    def do_house_work(self):
        print("listening music")

    def hello_friend(self):
        print("hello friend(mother)")


class Father(AbstractParent):
    def __init__(self):
        print("father consctructor")

    def play_guitar(self):
        print("play guitar")

    def do_house_work(self):
        print("sitting on the sofa and drink beer")


class Daugther(Mother, Father):

    def __init__(self, age=0):
        Mother.__init__(self)
        Father.__init__(self)

    def hello_friend(self):
        print("hello friend(daugther)")

    # ===

    def do_work(self):
        print("I'm working like a horse")


class Friend():
    pass


def greet_mother(mother: Mother):
    print("hello mother")
    mother.do_work()


def greet_father(father: Father):
    print("time for beer")
    father.play_guitar()


if __name__ == "__main__":
    daughter = Daugther()
    # daughter.do_work()

    # change object class
    # daughter.__class__ = Friend

    greet_mother(daughter)
    greet_father(daughter)
    daughter.hello_friend()
    daughter.do_house_work()

    for x in [daughter]:
        x.do_house_work()

    # list
    povtorka_list = ["math", "programming", "superprise"]

    # tuple
    vasian_tuple = ("11 years", 12, 3.14, daughter)

    # set
    my_set = {23, 11, 54, 23, 23, "call", daughter}

    # frozenset

    another_frozenset = frozenset(["di", "mi", "do"])
    print(another_frozenset)

    # dict

    other_dict = {"name": "Illya", "Age": "18", (1, 2, 3): "tuple_as_a_key"}
    print(other_dict["name"])
