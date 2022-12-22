import random
from Org import *

# import matlab.engine
# eng = matlab.engine.start_matlab()

def procreate(orgL,popSize,mutProb):
    '''The procreate function creates a list of new organisms
        using the replicate method and random sampling
    Inputs: list of organisms, orgL
            population size, popSize
            mutation probablity, mutpProb
    Outputs: a new list of organisms, newOrgL
    '''
    newOrgL = []
    i = 0
    while i < popSize:
        motherOrg = random.choice(orgL)
        newOrgL = newOrgL + [motherOrg.replicate(mutProb)]
        i += 1
    return newOrgL

def evoSim(popL,popSize,numGen,mutProb):
    '''The evoSim function replicates genetic drift
        by using procreate to create successive generations
    Inputs: list of organisms, popL
            population size, popSize
            number of generations, num Gen
            mutation probablity, mutpProb
    Outputs: a new list of organisms, simL
    '''
    simL = [popL]
    gen = 0
    newPop = popL
    while gen < numGen:
        newPop = procreate(newPop, popSize, mutProb)
        simL = simL + [newPop]
        gen += 1
    return simL


def evoSimSelect(popL,popSize,numGen,mutProb,fitnessD):
    '''The evoSimSelect function replicates genetic drift and natural selection
        by culling the population and then using procreate to create successive generations
    Inputs: list of organisms, popL
            population size, popSize
            number of generations, num Gen
            mutation probablity, mutpProb
            fitness dictionary, fitnessD
    Outputs: a new list of organisms, simL
    '''
    simL = [popL]
    survivorPop = cullPop(popL, fitnessD)
    gen = 0
    while gen < numGen:
        survivorPop = cullPop(survivorPop, fitnessD)
        simL = simL + [procreate(survivorPop, popSize, mutProb)]
        gen += 1
    return simL