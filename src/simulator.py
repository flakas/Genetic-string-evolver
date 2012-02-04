#Simulator for Dawkins Weasel program

import random

class Simulator:
    characters = ''
    mutation_rate = 0.05
    copy_limit = 1000
    target = ''
    suppressOutput = False

    def __init__(self, characters, mutation_rate, copy_limit):
        self.characters = characters
        self.mutation_rate = mutation_rate
        self.copy_limit = copy_limit

    def scoreIteration(self, str):
        score = 0
        for key in range(len(self.target)):
            if self.target[key] == str[key]:
                score += 1
        return score

    def mutate(self, str):
        str = list(str)
        for key in range(len(str)):
            if self.mutation_rate >= random.random():
                str[key] = self.characters[random.randint(0, 
                   len(self.characters) - 1)]
        return ''.join(str)

    def run(self, target):
        self.target = target
        current = ''.join([self.characters[random.randint(0, 
            len(self.characters) - 1)] for i in range(len(target))]) 
        iterations = 0
        self.printStep(iterations, current)
        while current != target:
            iterations += 1
            copies = []
            for i in range(self.copy_limit):
                copies.append(self.mutate(current))
            current = max(copies, key=lambda x: self.scoreIteration(x))    
            self.printStep(iterations, current)
        return iterations

    def setOutput(self, output=True):
        self.suppressOutput = not(output)
        return self.suppressOutput

    def printStep(self, iteration, current):
        if not self.suppressOutput:
            print '%d: Target "%s", current "%s" (%d of %d)' % (
                    iteration, self.target, current, 
                    self.scoreIteration(current), len(self.target))
