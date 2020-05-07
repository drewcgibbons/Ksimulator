import random


# decides the pitch
def makepitch():
    i = random.randint(1, 100)

    if i < 40:
        return FourSeam()
    elif i < 60:
        return TwoSeam()
    elif i < 75:
        return Slider()
    elif i < 90:
        return Changeup()
    elif i < 95:
        return Cutter()
    elif i < 98:
        return Splitter()
    else:
        return Forkball()


# Pitch definitions
class Pitch:
    def __init__(self, minspeed, maxspeed):
        self._speed = random.randint(minspeed, maxspeed)


class FourSeam(Pitch):
    _type = "Fastball"

    def __init__(self):
        Pitch.__init__(self, 90, 103)


class TwoSeam(Pitch):
    _type = "Sinker"

    def __init__(self):
        super().__init__(85, 95)


class Cutter(Pitch):
    _type = "Cutter"

    def __init__(self):
        super().__init__(82, 94)


class Splitter(Pitch):
    _type = "Splitter"

    def __init__(self):
        super().__init__(75, 95)


class Forkball(Pitch):
    _type = "Forkball"

    def __init__(self):
        super().__init__(70, 90)


class Slider(Pitch):
    _type = "Slider"

    def __init__(self):
        super().__init__(80, 95)


class Changeup(Pitch):
    _type = "Changeup"

    def __init__(self):
        super().__init__(70, 85)