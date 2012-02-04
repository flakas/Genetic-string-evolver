# Dawkins Weasel program simulation. Simulates evolution of random strings
# to user supplied strings
import sys
import cProfile
import timeit

import simulator

characters = 'QWERTYUIOPASDFGHJKLZXCVBNM '
MUTATION_RATE = 0.05
COPY_LIMIT = 100

target = sys.argv[1]
if len(target) < 1:
    print 'Input at least 1 character'
    sys.exit()

s = simulator.Simulator(characters, MUTATION_RATE, COPY_LIMIT)
print 'Numder of iterations: %d' % s.run(target)

