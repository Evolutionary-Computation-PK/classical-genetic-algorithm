import random
from source.selection.selection_strategy import SelectionStrategy
from source.population.individual import Individual


class TournamentSelection(SelectionStrategy):
    def select(self, individuals: list[Individual], fitness_function, tournament_size: int = 3,
               **kwargs) -> list[Individual]:
        """
        Selects individuals using tournament selection.

        :param individuals: List of individuals in the population.
        :param fitness_function: Fitness function to evaluate individuals.
        :param tournament_size: Number of individuals in each tournament.
        :return: List of selected individuals.
        """
        if tournament_size > len(individuals):
            raise ValueError("Tournament size cannot be greater than the number of individuals.")

        if len(individuals) % tournament_size != 0:
            raise ValueError("The number of individuals must be divisible by the tournament size.")

        selected_individuals = []
        random.shuffle(individuals)  # Shuffle individuals to ensure random grouping

        # Split individuals into groups of tournament_size
        groups = [individuals[i:i + tournament_size] for i in range(0, len(individuals), tournament_size)]

        for group in groups:
            winner = max(group, key=lambda ind: ind.count_fitness_function(fitness_function))
            selected_individuals.append(winner)

        return selected_individuals