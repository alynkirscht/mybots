from scipy.stats import mannwhitneyu
import numpy
"""
Conducts the Mann Whitney U Test for the matrices (matrixNx.npy)
"""

a_first = []
a_last = []
b_first = []
b_last = []

fitnessMatrixA1 = numpy.load("matrixA1.npy")
fitnessMatrixB1 = numpy.load("matrixB1.npy")
fitnessMatrixA2 = numpy.load("matrixA2.npy")
fitnessMatrixB2 = numpy.load("matrixB2.npy")
fitnessMatrixA3 = numpy.load("matrixA3.npy")
fitnessMatrixB3 = numpy.load("matrixB3.npy")
fitnessMatrixA4 = numpy.load("matrixA4.npy")
fitnessMatrixB4 = numpy.load("matrixB4.npy")
fitnessMatrixA5 = numpy.load("matrixA5.npy")
fitnessMatrixB5 = numpy.load("matrixB5.npy")

for matrix in [fitnessMatrixA1, fitnessMatrixA2, fitnessMatrixA3, fitnessMatrixA4, fitnessMatrixA5]:
    a_first += list(matrix[:, 0])
    a_last += list(matrix[:, -1])

for matrix in [fitnessMatrixB1, fitnessMatrixB2, fitnessMatrixB3, fitnessMatrixB4, fitnessMatrixB5]:
    b_first += list(matrix[:, 0])
    b_last += list(matrix[:, -1])


U1, p = mannwhitneyu(a_first, a_last)
print("Evolution in variant A: " + str(U1) + " p = " + str(p))
U1, p = mannwhitneyu(b_first, b_last)
print("Evolution in variant B: " + str(U1) + " p = " + str(p))

U1, p = mannwhitneyu(a_first, b_first)
print("Fair test? " + str(U1) + " p = " + str(p))

U1, p = mannwhitneyu(a_last, b_last)
print("Significant different? " + str(U1) + " p = " + str(p))