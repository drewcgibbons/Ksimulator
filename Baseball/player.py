class Player:
    def __init__(self, fname, lname, position):
        self._firstname = fname
        self._lastname = lname
        self._position = position

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def position(self):
        return self._position
