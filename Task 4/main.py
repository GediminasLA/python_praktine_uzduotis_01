# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 

class Movie:
    def __init__(self, title: str, director: str, budget: int):
        self.title = title
        self.director = director
        self.budget = budget

    def printStuff(self):
        print(self.title, self.director, self.budget, sep="\n")

    def wasExpensive(self):
        if self.budget > 100000000:
            return True
        else:
            return False

movie1 = Movie("Something awesome", "someone", 150000000)
movie2 = Movie("Something less awesome", "def not me", 500)

movie1.printStuff()
print(movie1.wasExpensive())

print('\n')

movie2.printStuff()
print(movie2.wasExpensive())

