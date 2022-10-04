class Parameters:
    """Class collects parameters entered by user."""
    def __init__(self, mass, mi, rounds, no_stones):
        """
        Parameterized constructor.
        :param mass: Mass of the stone entered by user.
        :param mi: Substrate friction coefficient entered by user.
        :param rounds: Number of rounds in game entered by user.
        :param stones: Number of stones for each player in one round entered by user.
        """
        self.mass = mass
        self.mi = mi * 0.01  #value passed is 100x bigger.
        self.rounds = rounds
        self.no_stones = no_stones

    def __str__(self):
        """
        Test method.
        :return: (string) All parameters written.
        """
        return "Mass: " + str(self.mass) +"Mi: "+ str(self.mi) +"No. of rounds: "+ str(self.rounds) +"No. of stones: "+ str(self.no_stones)