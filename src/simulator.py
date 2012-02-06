#/usr/bin/python2.7
# Simulator for Dawkins Weasel program

import random

class Simulator:
    """Dawkins Weasel program that simulates random string evolution into 
    a user generated string.  
    """
    _characters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM '
    _mutation_rate = 0.05
    _copy_limit = 1000
    _target = ''
    _suppress_output = False

    def __init__(self, characters='', mutation_rate=-1, copy_limit=-1):
        """Set custom settings on construct if you need.  """
        if characters:
            self._characters = characters
        if mutation_rate >= 0:
            self._mutation_rate = mutation_rate
        if copy_limit >= 0:
            self._copy_limit = copy_limit

    def score_iteration(self, str):
        """Compare string supplied and target and compute string score based
        on how many characters in same position match.  
        
        """
        score = 0
        for key in range(len(self._target)):
            if self._target[key] == str[key]:
                score += 1
        return score

    def mutate(self, str):
        """Mutate supplied string. Each character of the string has a 
        self.mutation_rate chance of mutating.  
        
        """
        str = list(str)
        for key in range(len(str)):
            if self._mutation_rate >= random.random():
                str[key] = self._characters[random.randint(0, 
                   len(self._characters) - 1)]
        return ''.join(str)

    def run(self, target):
        """Run a simulation with the supplied string.  """
        self._target = target
        # Generate a random string with the same length as target string
        current = ''.join([self._characters[random.randint(0, 
            len(self._characters) - 1)] for i in range(len(target))]) 
        iterations = 0
        self.__print_step(iterations, current)
        while current != target:
            iterations += 1
            copies = []
            for i in range(self._copy_limit):
                copies.append(self.mutate(current))
            current = max(copies, key=lambda x: self.score_iteration(x))    
            self.__print_step(iterations, current)
        return iterations

    def set_output(self, output=True):
        """Enable or disable output.  """
        self._suppress_output = not(output)
        return self._suppress_output

    def __print_step(self, iteration, current):
        """Print current iteration stats.  """
        if not self._suppress_output:
            print '%d: Target "%s", current "%s" (%d of %d)' % (
                    iteration, self._target, current, 
                    self.score_iteration(current), len(self._target))
