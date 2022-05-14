class LSystem:
    """Description, b#tch!"""
    def __init__(self, alphabet = [], axiom = '', rules = []):
        self.alphabet = alphabet
        self.axiom = axiom
        self.rules = rules
    
    def iterate(self, iterations):
        """Iterates system n times and returns final iteration"""
        system = self.axiom
        for n in range(iterations):
            systemNext = ''
            for symbol in system:
                for rule in self.rules:
                    isConstant = True
                    if symbol == rule[0]:
                        isConstant = False
                        systemNext += rule[1]
                        break;
                if isConstant:
                    systemNext += symbol
            system = systemNext
        return system
    
    def iterateList(self, iterations):
        """Iterates system n times and returns list of iterations"""
        system = self.axiom
        iterationsList = [system]
        for n in range(iterations):
            systemNext = ''
            for symbol in system:
                for rule in self.rules:
                    isConstant = True
                    if symbol == rule[0]:
                        isConstant = False
                        systemNext += rule[1]
                        break;
                if isConstant:
                    systemNext += symbol
            system = systemNext
            iterationsList.append(system)
        return iterationsList
