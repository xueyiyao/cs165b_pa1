# Starter code for CS 165B HW2 Spring 2019
import numpy as np
import scipy.linalg as spla

def run_train_test(training_input, testing_input):
    """
    Implement the training and testing procedure here. You are permitted
    to use additional functions but DO NOT change this function definition.
    You are permitted to use the numpy library but you must write
    your own code for the linear classifier.

    Inputs:
        training_input: list form of the training file
            e.g. [[3, 5, 5, 5],[.3, .1, .4],[.3, .2, .1]...]
        testing_input: list form of the testing file

    Output:
        Dictionary of result values

        IMPORTANT: YOU MUST USE THE SAME DICTIONARY KEYS SPECIFIED

        Example:
            return {
                "tpr": #your_true_positive_rate,
                "fpr": #your_false_positive_rate,
                "error_rate": #your_error_rate,
                "accuracy": #your_accuracy,
                "precision": #your_precision
            }
    """


    # TODO: IMPLEMENT

    #point 100 of A [2.0045, 3.1438, 3.8593]
    #point 100 of B [-0.70897, -1.5211, 1.978]
    
    training_info = training_input[0]
    training_input.remove(training_info)

    T = np.array(training_input)
    A = T[:100, :]
    A_aggregate = A.sum(axis = 0)
    B = T[101:200, :]
    B_aggregate = B.sum(axis = 0)
    C = T[201:300, :]
    C_aggregate = C.sum(axis = 0)

    A_centroid = A_aggregate / 100
    B_centroid = B_aggregate / 100
    C_centroid = C_aggregate / 100
    #print('A Centroid: ', A_centroid)
    #print('B Centroid: ', B_centroid)
    #print('C Centroid: ', C_centroid)
    wAB = A_centroid - B_centroid
    pn2AB = (A_centroid + B_centroid) / 2
    tAB = np.dot(wAB,pn2AB)
    wAC = A_centroid - C_centroid
    pn2AC = (A_centroid + C_centroid) / 2
    tAC = np.dot(wAC,pn2AC)
    wBC = B_centroid - C_centroid
    pn2BC = (B_centroid + C_centroid) / 2
    tBC = np.dot(wBC,pn2BC)

    exA = np.array([2.0045, 3.1438, 3.8593])
    exB = np.array([-0.70897, -1.5211, 1.978])


    testing_info = testing_input[0]
    testing_input.remove(testing_info)
    testingT = np.array(testing_input)
    #print(testingT)
    testingA = testingT[:25, :]
    testingB = testingT[25:50, :]
    testingC = testingT[50:75, :]
    #print(testingA)
    #print(testingB)
    #print(testingC)

    truePosA = 0;
    truePosB = 0;
    truePosC = 0;
    AinB = 0;
    AinC = 0;
    BinA = 0;
    BinC = 0;
    CinA = 0;
    CinB = 0;
    trueNegA = 0;
    trueNegB = 0;
    trueNegC = 0;
    for i in range(25):
        if((np.dot(testingA[i], wAB) >= tAB) & (np.dot(testingA[i], wAC) >= tAC)):
            truePosA = truePosA + 1
        elif((np.dot(testingA[i], wAB) < tAB)):
            AinB = AinB + 1
        else:
            AinC = AinC + 1
        if((np.dot(testingB[i], wAB) < tAB) & (np.dot(testingB[i], wBC) >= tBC)):
            truePosB = truePosB + 1
        elif((np.dot(testingB[i], wAB) >= tAB)):
            BinA = BinA + 1
        else:
            BinC = BinC + 1
        if((np.dot(testingC[i], wAC) < tAC) & (np.dot(testingC[i], wBC) < tBC)):
            truePosC = truePosC + 1
        elif((np.dot(testingC[i], wAC) >= tAC)):
            CinA = CinA + 1
        else:
            CinB = CinB + 1

    trueNegA = truePosB + truePosC + BinC + CinB
    falsePosA = BinA + CinA
    falseNegA = AinB + AinC
    trueNegB = truePosA + truePosC + AinC + CinA
    falsePosB = AinB + CinB
    falseNegB = BinA + BinC
    trueNegC = truePosA + truePosB + AinB + BinA
    falsePosC = AinC + BinC
    falseNegC = CinA + CinB
    """
    print(truePosA)
    print(falsePosA)
    print(falseNegA)
    print(trueNegA)
    print(truePosB)
    print(falsePosB)
    print(falseNegB)
    print(trueNegB)
    print(truePosC)
    print(falsePosC)
    print(falseNegC)
    print(trueNegC)
    """
    TruePos = truePosA + truePosB + truePosC
    TrueNeg = trueNegA + trueNegB + trueNegC
    FalsePos = falsePosA + falsePosB + falsePosC
    FalseNeg = falseNegA + falseNegB + falseNegC
    TotalPos = TruePos + FalseNeg
    TotalNeg = TrueNeg + FalsePos
    EstPos = TruePos + FalsePos
    EstNeg = TrueNeg + FalseNeg

    return {
                "tpr": TruePos / float(TotalPos),
                "fpr": FalsePos / float(TotalNeg),
                "error_rate": (FalsePos + FalseNeg) / float(TotalNeg + TotalPos),
                "accuracy": (TruePos + TrueNeg) / float(TotalPos + TotalNeg),
                "precision": TruePos / float(EstPos)
            }
