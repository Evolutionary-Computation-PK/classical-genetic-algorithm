import numpy as np
from typing import List

from source.genetic_algorithm.crossover.crossover import Crossover
from source.genetic_algorithm.population.individual import Individual
from source.genetic_algorithm.crossover.random_generator import RandomGenerator


class PointCrossover(Crossover):

    def __init__(self, intersection_number: int, crossover_size: int, crossover_probability=0.8):
        super().__init__(crossover_size, crossover_probability)
        self.intersection_number = intersection_number

    def cross(self, population: List[Individual]) -> list[Individual]:
        new_population = []
        chromosome_size = population[0].number_of_chromosomes
        number_of_genes = population[0].number_of_genes
        i = self.crossover_size
        while i > 0:
            individual1, individual2 = self.generate_individuals(population)
            not_crossover = np.random.rand()
            if self.crossover_probability < not_crossover:
                continue
            intersection_points = self.generate_intersection_points(self.intersection_number, number_of_genes)
            self.cross_individuals(individual1, individual2, chromosome_size, intersection_points)
            new_population.append(individual1)
            new_population.append(individual2)
            i -= 2

        return new_population[:self.crossover_size]


    def generate_intersection_points(self, intersection_number: int, number_of_genes: int) -> List[int]:
        if intersection_number == 1:
            intersection_points = RandomGenerator.generate_random_list(1, 1, number_of_genes)
            intersection_points = intersection_points + [number_of_genes]
        else:
            intersection_points = RandomGenerator.generate_random_list(2, 1, number_of_genes)
            intersection_points = sorted(intersection_points)
        return intersection_points

    def cross_individuals(self, individual1: Individual, individual2: Individual, chromosome_size: int,
                          intersection: List[int]) -> None:
        for chromosome in range(0, chromosome_size):
            self.cross_genes(chromosome, individual1, individual2, intersection[0], intersection[1])

    def cross_genes(self, index: int, individual1: Individual, individual2: Individual, start: int, end: int) -> None:
        value1 = individual1.chromosomes[index][start:end].copy()
        individual1.chromosomes[index][start:end] = individual2.chromosomes[index][start:end].copy()
        individual2.chromosomes[index][start:end] = value1
