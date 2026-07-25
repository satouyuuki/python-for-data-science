from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __repr__(self) -> str:
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})>"

    def __str__(self) -> str:
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})>"

    def die(self):
        super().die()


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __repr__(self) -> str:
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})>"

    def __str__(self) -> str:
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})>"

    def die(self):
        super().die()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
