#Dawkins Weasel program simulation
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
s.setOutput(False)
#s.run(target)
#cProfile.run('s.run(target)')
def runtimer():
    s.run(target)
    return

number = 20
print timeit.Timer(runtimer).timeit(number=number) / number
