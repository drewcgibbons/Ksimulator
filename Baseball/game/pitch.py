import random

class Pitcher:
    # decides the pitch
    def makepitch(self):
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


    # AI pitch
    # TODO: Make count actually impact pitch location
    def throwaipitch(self, count):
        pitch = self.makepitch()
        location = Location(count, -1, -1, ai=True)
        self.throwpitch(pitch, location)


    # User Pitch
    def throwuserpitch(self, pitchnum, location):
        pitch = None
        if pitchnum == 0:
            pitch = FourSeam()
        elif pitchnum == 1:
            pitch = TwoSeam()
        elif pitchnum == 2:
            pitch = Slider()
        elif pitchnum == 3:
            pitch = Changeup()
        elif pitchnum == 4:
            pitch = Cutter()
        elif pitchnum == 5:
            pitch = Splitter()
        elif pitchnum == 6:
            pitch = Forkball()


    # show the pitch thrown
    def showpitch(self, pitch):
        print(pitch.type, pitch.speed, "MPH")


# Pitch definitions
class Pitch:
    def __init__(self, minspeed, maxspeed):
        self._speed = random.randint(minspeed, maxspeed)

    @property
    def speed(self):
        return self._speed


class FourSeam(Pitch):
    _type = "Fastball"

    def __init__(self):
        Pitch.__init__(self, 90, 103)

    @property
    def type(self):
        return self._type


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


# x,y location of pitch (0,0 is top left) with ai flag
class Location:
    def __init__(self, count, x, y, ai):
        if not ai:
            self.x = x
            self.y = y
        else:
            self.weightlocation(count)

    # Weighs to ~60% strikes
    def weightlocation(self, count):
        rand = random.randint(1,100)
        # Throw a strike
        if rand <= 80:
            self.x = random.randint(1, 3)
            self.y = random.randint(1, 3)
        # Throw a ball
        else:
            self.x = 0 if random.randint(0, 1) == 1 else 4
            self.y = 0 if random.randint(0, 1) == 1 else 4
