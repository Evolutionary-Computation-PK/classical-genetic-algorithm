from typing import List

from source.crossover.random_generator import RandomGenerator
from source.population.individual import Individual
from abc import ABC, abstractmethod

class Crossover(ABC):

    def __init__(self, crossover_size: int, crossover_probability: float):
        self.crossover_size = crossover_size
        self.crossover_probability = crossover_probability


    @abstractmethod
    def cross(self, population: List[Individual]) -> list[Individual]:
        pass

    def generate_individuals(self, population: List[Individual]):
        population_size = len(population)
        individuals_index = RandomGenerator.generate_random_list(2, 0, population_size)
        individual1 = population[individuals_index[0]]
        individual2 = population[individuals_index[1]]
        return individual1, individual2