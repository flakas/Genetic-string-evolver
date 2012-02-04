#Simulator for Dawkins Weasel program

import random

class Simulator:
    characters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM '
    mutation_rate = 0.05
    copy_limit = 1000
    target = ''
    suppressOutput = False

    def __init__(self, characters = '', mutation_rate = -1, copy_limit = -1):
        """Set custom settings on construct if you need"""
        if len(characters) > 1:
            self.characters = characters
        if mutation_rate >= 0:
            self.mutation_rate = mutation_rate
        if copy_limit >= 0:
            self.copy_limit = copy_limit

    def scoreIteration(self, str):
        """Compare string supplied and target and compute string score based
        on how many characters in same position match."""
        score = 0
        for key in range(len(self.target)):
            if self.target[key] == str[key]:
                score += 1
        return score

    def mutate(self, str):
        """Mutate supplied string. Each character of the string has a 
        self.mutation_rate chance of mutating"""
        str = list(str)
        for key in range(len(str)):
            if self.mutation_rate >= random.random():
                str[key] = self.characters[random.randint(0, 
                   len(self.characters) - 1)]
        return ''.join(str)

    def run(self, target):
        """Run a simulation with the supplied string"""
        self.target = target
        #Generate a random string with the same length as target string
        current = ''.join([self.characters[random.randint(0, 
            len(self.characters) - 1)] for i in range(len(target))]) 
        iterations = 0
        self.__printStep(iterations, current)
        while current != target:
            iterations += 1
            copies = []
            for i in range(self.copy_limit):
                copies.append(self.mutate(current))
            current = max(copies, key=lambda x: self.scoreIteration(x))    
            self.__printStep(iterations, current)
        return iterations

    def setOutput(self, output=True):
        """Enable or disable output"""
        self.suppressOutput = not(output)
        return self.suppressOutput

    def __printStep(self, iteration, current):
        """Print current iteration stats"""
        if not self.suppressOutput:
            print '%d: Target "%s", current "%s" (%d of %d)' % (
                    iteration, self.target, current, 
                    self.scoreIteration(current), len(self.target))
