from LSystemClass import LSystem

seaweed = LSystem(['A', 'B'], 'A', [['A', 'AB'], ['B', 'A']])
# seaweed.alphabet = ['A', 'B']
# seaweed.axiom = 'A'
# seaweed.rules =  [['A', 'AB'], ['B', 'A']]
res = seaweed.iterateList(4)

print(res)

fractalTree = LSystem()
fractalTree.alphabet = ['0', '1', '[', ']']
fractalTree.axiom = '0'
fractalTree.rules = [['1', '11'], ['0', '1[0]0']]
res = fractalTree.iterateList(3)
print(res)
