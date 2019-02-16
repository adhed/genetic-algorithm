from algorithm import Algorithm
from function import Function


def ask_for_number(question):
    try:
        point = int(input(question))
    except:
        print("Czy aby na pewno podałeś numer?")

    return point

def ask_for_float(question):
    try:
        point = float(input(question))
    except:
        print("Czy aby na pewno podałeś numer?")

    return point
        
def ask_for_function():
    print("Najpierw podaj wspolczynniki funkcji.")
    a = ask_for_number("a = ")
    b = ask_for_number("b = ")
    c = ask_for_number("c = ")
    d = ask_for_number("d = ")
    function = Function(a, b, c, d)
    return function

def main():
    print("Witaj w algorytmie genetycznym!")
    function = ask_for_function()
    chromosomes = ask_for_number("Podaj liczbe chromosomow: ")
    iterations = ask_for_number("Podaj liczbe iteracji do przeprowadzenia: ")
    crossing_rate = ask_for_float("Podaj wspolczynnik krzyzowania: ")
    mutation_rate = ask_for_float("Podaj wspolczynnik mutacji: ")
    algorithm = Algorithm(chromosomes, iterations, function, crossing_rate, mutation_rate)
    algorithm.generate()

if __name__ == "__main__":
    main()