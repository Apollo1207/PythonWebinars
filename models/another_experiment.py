from multimethod import multimethod
import doctest


class WithStaticAndOverload:
    worker_name = "I'm working"

    @staticmethod
    def do_work():
        """
        >>> WithStaticAndOverload.do_work()
        "I'm working"
        """
        return WithStaticAndOverload.worker_name

    def sing_a_song(self):
        """
        >>> obj.sing_a_song()
        I'm working
        """
        print(WithStaticAndOverload.worker_name)

    @multimethod
    def print_data(self, first: str, second: str):
        """
        >>> obj.print_data("555", "777")
        '555777'
        """
        return str(first) + str(second)

    @multimethod
    def print_data(self, first: int, second: int):
        """
        >>> obj.print_data(555, 777)
        '1332'
        """
        return str(first + second)


if __name__ == "__main__":
    # my_object = WithStaticAndOverload()
    # my_object.print_data(23, 45)
    # my_object.print_data("first", "second")
    doctest.testmod(verbose=True, extraglobs={'obj': WithStaticAndOverload()})
