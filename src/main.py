#Dawkins Weasel program simulation
import sys
import random

MUTATION_RATE = 0.05
COPY_LIMIT = 100

target = sys.argv[1]
if len(target) < 1:
    print 'Input at least 1 character'
    sys.exit()

characters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM '

def scoreIteration(str1, str2):
    score = 0
    for key in range(len(str1)):
        if str1[key] == str2[key]:
            score += 1
    return score

def mutate(str, mutation_rate, characters):
    str = list(str)
    for key in range(len(str)):
        if mutation_rate >= random.random():
            str[key] = characters[random.randint(0, len(characters) - 1)]
    return ''.join(str)


current = ''.join([characters[random.randint(0, len(characters) - 1)] for i in range(len(target))]) 
iterations = 0
print '%d: Target "%s", current "%s" (%d of %d)' % (iterations, target, current, scoreIteration(target, current), len(target))
while current != target:
    iterations += 1
    copies = []
    for i in range(COPY_LIMIT):
        copies.append(mutate(current, MUTATION_RATE, characters))

    copies = sorted(copies, lambda x, y: cmp(scoreIteration(target, x), scoreIteration(target, y)), reverse=True)    
    current = copies[0]
    print '%d: Target "%s", current "%s" (%d of %d)' % (iterations, target, current, scoreIteration(target, current), len(target))

