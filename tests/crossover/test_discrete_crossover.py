from source.genetic_algorithm.crossover.discrete_crossover import DiscreteCrossover
from source.genetic_algorithm.population.individual import Individual
import numpy as np


def test_cross_when_probability_is_max():
    discrete_crossover = DiscreteCrossover(2)
    discrete_crossover.crossover_probability = 1
    chromosomes_zero = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    chromosomes_ones = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes = chromosomes_zero.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes = chromosomes_ones.copy()

    chromosome = discrete_crossover.generate_chromosome(individual1, individual2, 3, 10)

    np.testing.assert_array_equal(chromosome, chromosomes_zero)



def test_cross_when_probability_is_min():
    discrete_crossover = DiscreteCrossover(2)
    discrete_crossover.crossover_probability = 0
    chromosomes_zero = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    chromosomes_ones = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes = chromosomes_zero.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes = chromosomes_ones.copy()

    chromosome = discrete_crossover.generate_chromosome(individual1, individual2, 3, 10)

    np.testing.assert_array_equal(chromosome, chromosomes_ones)


def test_cross():
    discrete_crossover = DiscreteCrossover(2)
    chromosomes_first = np.array([[0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
                                 [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                                 [1, 0, 0, 0, 1, 0, 0, 1, 1, 1]])

    chromosomes_second = np.array([[1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
                                 [1, 0, 1, 1, 0, 1, 1, 0, 1, 0],
                                 [0, 0, 0, 0, 1, 1, 0, 1, 0, 0]])
    individual1 = Individual(0, 0, 0, 0, False)
    individual1.chromosomes = chromosomes_first.copy()
    individual2 = Individual(0, 0, 0, 0, False)
    individual2.chromosomes = chromosomes_second.copy()

    population = discrete_crossover.cross([individual1, individual2])

    assert not np.array_equal(population[0].chromosomes, [chromosomes_first,chromosomes_second])
    assert not np.array_equal(population[1].chromosomes, [chromosomes_first, chromosomes_second])
    assert len(population) == 2
