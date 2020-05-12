import Baseball.pitch as bp
import random


#TODO: Add Batter traits and statistic keeping
class Batter:
    def __init__(self, name):
        self.name = name

    # returns integer actint to determine what happened
    def action(self, pitch):
        actint = -10
        i = random.randint(1, 100)
        if pitch.isstrike:
            if i < 65:
                actint = self.take()
            else:
                actint = self.swing(pitch)
        else:
            if i < 75:
                actint = self.take()
            else:
                actint = self.swing(pitch)

        return actint

    def take(self):
        return 0

    # 1 - single, 2 - double
    # -1 foul
    # -2 fly out
    # -3 ground out
    # -4 lineout
    # -5 strike swinging
    def swing(self, pitch):
        print(self.name, "swings!")
        result = -10
        batterswing = Swing(-1, -1, pitch, ai=True)
        return swingresult(pitch, batterswing)


class Swing:
    def __init__(self, x, y, pitch, ai):
        self.pitch = pitch
        if not ai:
            self.x = x
            self.y = y
        else:
            self.weightlocation(pitch)

    # May modify per pitch in future
    def weightlocation(self, pitch):
        rand = random.randint(1,100)
        self.x = random.randint(pitch.location.x - 1, pitch.location.x + 1)
        self.y = random.randint(pitch.location.y - 1, pitch.location.y + 1)


# determines result of swing
def swingresult(pitch, swing):
    result = random.randint(1, 100)
    # Guaranteed Hit
    if pitch.location.x == swing.x and pitch.location.y == swing.y:
        hitresult = -10

        # single = 1, double = 2, triple = 3, HR = 4
        if result <= 40:
            return 1
        elif result <= 70:
            return 2
        elif result <= 75:
            return 3
        elif result <= 90:
            return 4
        else:
            return 5

    # -1 foul
    # -2 fly out
    # -3 ground out
    # -4 lineout
    elif pitch.location.x == swing.x and pitch.location.y < swing.y:
        if result <= 20:
            return -3
        elif result <= 35:
            return -1
        elif result <= 60:
            return -4
        elif result <= 70:
            return 1
        elif result <= 80:
            return 2
        else:
            return 5

    # 1 - single, 2 - double
    # -1 foul
    # -2 fly out
    # -3 ground out
    # -4 lineout
    elif pitch.location.x == swing.x and pitch.location.y > swing.y:
        if result <= 30:
            return -2
        elif result <= 45:
            return -1
        elif result <= 60:
            return 1
        elif result <= 70:
            return 4
        elif result <= 80:
            return 2
        else:
            return 5


    # 1 - single, 2 - double
    # -1 foul
    # -2 fly out
    # -3 ground out
    # -4 lineout
    elif pitch.location.x != swing.x and pitch.location.y == swing.y:
        if result <= 25:
            return -1
        elif result <= 50:
            return -4
        elif result <= 65:
            return 2
        elif result <= 75:
            return 1
        elif result <= 80:
            return 4
        elif result <= 81:
            return 3
        else:
            return 5

    elif pitch.location.x != swing.x and pitch.location.y != swing.y:
        if result <= 25:
            return -2
        elif result <= 40:
            return -3
        elif result <= 55:
            return -4
        elif result <= 60:
            return 1
        elif result <= 65:
            return 2
        else:
            return 5
