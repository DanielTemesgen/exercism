import random, string, weakref

class Robot:
    _instances = set()

    def __init__(self):
        self.name = self._name()
        self._instances.add(weakref.ref(self))

    def _random_letters(self, num: int):
        list_of_random_letters = [random.choice(string.ascii_uppercase) for _ in range(num)]
        return list_of_random_letters
    
    def _name(self):
        a, b = self._random_letters(2)
        random_three_digit_number = random.randrange(1, 10**3)
        num_with_zeros = str(random_three_digit_number).zfill(3)
        name =  f"{a}{b}{num_with_zeros}"
        if name in self.get_names():
            name = self._name()
        return name

    def reset(self):
        self.__init__()

    def get_names(self):
        names = []
        for obj in Robot.getinstances():
            try:
                names.append(obj.name)
            except AttributeError:
                names.append(None)
        return names

    @classmethod
    def getinstances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead
        

