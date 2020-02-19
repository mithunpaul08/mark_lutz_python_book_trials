class Employee:
    _name = "from outside constructor"

    def __init__(self):
        self._name = "from inside constructor"

    def setName(self, name):
        self._name = name