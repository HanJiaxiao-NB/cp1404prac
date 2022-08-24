CURRENT_YEAR = 2017
VINTAGE_AGE = 50


class Guitar:
    """Save guitar details from guitar lessons."""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Find out how old a guitar is from CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Judging from the age of the guitar, you can tell if the guitar is an antique."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used for sorting Guitars, by year released."""
        return self.year < other.year