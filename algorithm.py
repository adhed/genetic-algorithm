from chromosome import Chromosome
import math
import sys
import random
import copy

class Algorithm:
    def __init__(self, chromosomes_number, iterations, function, crossing_rate, mutation_rate):
        self.chromosomes = []
        self.iterations = iterations
        self.crossing_rate = crossing_rate
        self.mutation_rate = mutation_rate
        self.function = function
        self.create_chromosomes(chromosomes_number)

    def create_chromosomes(self, chromosomes):
        print("---------------------------------------------")
        print("Tworze chromosomy:")
        print("---------------------------------------------")
        for index in range(chromosomes):
            self.chromosomes.append(Chromosome(index))
        print("---------------------------------------------")        

    def generate(self):
        for index in range(self.iterations):
            print("---------------------------------------------") 
            print("Iteracja nr {0}".format(index + 1))
            print("---------------------------------------------") 
            self.calculate_adaptations()
            self.select_by_roulette()
            self.apply_crossings()
            self.apply_mutations()
        
        self.print_final()

    def print_final(self):
        print("------------------------------------")
        print("Finalna populacja:")
        print("------------------------------------")
        for chromosome in self.chromosomes:
            chromosome.print()

    def calculate_adaptations(self):
        for chromosome in self.chromosomes:
            score = self.function.calculate(chromosome.phenotype)
            chromosome.set_score(score)
            chromosome.print()

    def select_by_roulette(self):
        print("------------------------------------")
        print("Selekcja poprzez kolo ruletki...")
        print("------------------------------------")

        total = 0
        for chromosome in self.chromosomes:
            total += chromosome.score

        picks = random.sample(range(1, 100), len(self.chromosomes))
        new_population = []

        for pick in picks:
            print("Wylosowana liczba to: {0}".format(pick))
            selected = self.get_selected_individual(pick, total)
            new_population.append(copy.deepcopy(selected))
        
        self.chromosomes = new_population.copy()
        print("------------------------------------")
        print("Nowa populacja po losowaniu to:")
        print("------------------------------------")
        self.calculate_adaptations()

    def get_selected_individual(self, picked_number, total):
        already_used = 0
        for chromosome in self.chromosomes:
            chromosome_probability = chromosome.score / total * 100
            chromosome_range = already_used + chromosome.score / total * 100
            already_used += chromosome_probability
            if (picked_number <= chromosome_range):
                print("Odpowiada ona chromosomowi: {0}".format(chromosome.id))
                return chromosome

    def apply_crossings(self):
        print("------------------------------------")
        print("Probuje przeprowadzic krzyzowanie, wspolczynnik Pk = {0}".format(self.crossing_rate))
        print("------------------------------------")
        pairs = []
        while len(self.chromosomes):
            random1 = self.pop_random()
            random2 = self.pop_random()
            pair = random1, random2
            pairs.append(pair)
        
        for pair in pairs:
            print("{0} i {1}".format(pair[0].id, pair[1].id))

        print("------------------------------------")
        print("Dla kazdej pary losuje liczbe z przedzialu [0,1] i sprawdzam czy zajdzie krzyzowanie")
        print("------------------------------------")

        for pair in pairs:
            crossing_random = random.uniform(0.0, 1.0)
            print("Dla pary {0} i {1}, liczba = {2}".format(pair[0].id, pair[1].id, crossing_random))

            if crossing_random <= self.crossing_rate:
                print("Przeprowadzam krzyzowanie")
                locus = random.randint(1, 4)
                print("Losuje liczbe z przedzialu [1, 4] oznaczajaca miejsce krzyzowania: {0}".format(locus))
                temporary = pair[0]
                pair[0].cross_genes(pair[1], locus)
                pair[1].cross_genes(temporary, locus)
            else:
                print("Krzyzowanie nie zajdzie...")
            
            self.chromosomes.append(pair[0])
            self.chromosomes.append(pair[1])

    def apply_mutations(self):
        print("------------------------------------")
        print("Probuje aplikowac mutacje, wspolcznik Pm = {0}".format(self.mutation_rate))
        print("------------------------------------")

        for chromosome in self.chromosomes:
            mutation_probability = random.uniform(0.0, 1.0)
            print("Dla chromosomu nr {0}, wylosowalem liczbe = {1}".format(chromosome.id, mutation_probability))
            if (mutation_probability <= self.mutation_rate):
                chromosome.mutate()
            else:
                print("Nie przeprowadzam mutacji...")
        
    def pop_random(self):
        idx = random.randint(0, len(self.chromosomes) - 1)
        return self.chromosomes.pop(idx)