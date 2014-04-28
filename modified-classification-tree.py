"Tree data structure"

class Node(object):
    def __init__(self, variable, parents):
        self.variable = variable
        self.children = []
        self.parents = parents

    def add_child(self, variable):
        new_parents = self.parents[:]
        new_parents.append(self)
        child = Node(variable, new_parents)
        self.children.append(child)
        


"To create a tree, start with the root: T = Node(1) for a root with value 1."
"To add chilren, write T.add_child(2) to add a child with value 2."
"Identify children by T.children[2].children[0] for the first child of T's third child, etc."

"Research paper data structure"

"This is a disease and a list of lists; each list consists of a set of variables examined together."
"For example: if a study compares the heart disease rates of white females with gene variant X"
"and white females without, then the subsets are (white, female, X) and (white, female, notX)"
"Each variableset has a rate of the disease."

class Study(object):
    def __init__(self, disease, name, variablesets):
        self.name = name
        self.disease = disease
        for s in variablesets:
            self.variablesets.append(s)

    def add_variableset(self, s):
        self.variablesets.append(s)


class Variableset(object):
    def __init__(self, frequency, size, variables):
        self.frequency = frequency
        self.size = size
        for v in variables:
            self.variables.append(s)

"Variables and disease are character strings; frequency is a numerical variable."


def gini_impurity(study, variable, constants):
    yes = []
    no = []
    for s in study.variablesets:
        if (c in s.variables for c in constants) and (variable in s.variables):
           yes = yes.append(s)
        if (c in s.variables for c in constants) and (variable not in s.variables):
            no = no.append(s)
    if no == [] or yes ==[]:
        return None
    f_yes = sum(s.size * s.frequency for s in yes)/sum(s.size for s in yes)
    f_no = sum(s.size * s.frequency for s in no)/sum(s.size for s in no)
    gini_yes = 2* f_yes * (1-f_yes)
    gini_no = 2*f_no * (1-f_no)
    gini_impurity = gini_yes + gini_no
    return gini_impurity

"This provides a measure of the 'purity' resulting from dividing the data into two categories,"
"given the variables to be held constant.  Gini impurity is lower the closer that split"
"is to dividing the data into all sick and all healthy."
    

def choose_variable(studies, variables, constants):
    "of all the variables in a permissible set, given a set of fixed variables, which variable best separates the data?"
    varoptions = {}
    for variable in variables:
        studyoptions = {} 
        for study in studies:
            if gini_impurity != None:
                studyoptions[study.name] = gini_impurity(study, variable, constants)
        varoptions[variable] = studyoptions
        
    meangini = {}
    for variable in variables:
        studies = varoptions[variable]
        meangini[variable] = sum(studies.values())/len(studies)
    bestvariable = min(meangini, key = meangini.get)
    return bestvariable

"this is what happens when you hit a new node"

def NodeUpdate(studies, variables, node):
    parents = node.parents
    constants = [parent.variable for parent in parents]
    variable = choose_variable(studies, variables, constants)
    node.add_child(variable)
    node.add_child("not "variable)
    variables = variables.remove(variable)
    variables = variables.remove("not"variable)
    while variables != []:
        for n in node.children:
            NodeUpdate(studies, variables, n)
    
    
            
    
