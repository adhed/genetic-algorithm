import random
import constants

class Chromosome:
    alleles = (0, 1)

    def __init__(self, id):
        self.id = id
        self.phenotype = None
        self.score = None
        self.genes = [
            random.choice(self.alleles),
            random.choice(self.alleles),
            random.choice(self.alleles),
            random.choice(self.alleles),
            random.choice(self.alleles),
        ]
        self.calculate_phenotype()
        self.print()

    def print(self):
        print("Chromosom {0} {1}, fenotyp x = {2}, funkcja przystosowania F = {3}".format(self.id, self.genes, self.phenotype, self.score))

    def calculate_phenotype(self):
        self.phenotype = 0

        if (self.genes[0]):
            self.phenotype += 16
        if (self.genes[1]):
            self.phenotype += 8
        if (self.genes[2]):
            self.phenotype += 4
        if (self.genes[3]):
            self.phenotype += 2
        if (self.genes[4]):
            self.phenotype += 1

    def set_score(self, score):
        self.score = score

    def mutate(self):
        gene = random.randint(0, 4)
        print("Przeprowadzam mutacje...")
        print("Wylosowalem gen o numerze: {0}".format(gene + 1))
        print("Przed mutacja: {0}".format(self.genes))
        
        self.genes[gene] = 0 if self.genes[gene] else 1

        print("Po mutacji: {0}".format(self.genes))

        self.calculate_phenotype()
