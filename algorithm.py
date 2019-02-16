from chromosome import Chromosome
import math
import sys
import random

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
            new_population.append(selected)
        
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
        print("Przeprowadzam krzyzowanie, wspolczynnik Pk = {0}".format(self.crossing_rate))
        print("------------------------------------")

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
        