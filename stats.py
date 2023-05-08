from scipy.stats import mannwhitneyu

seg3_gen1 = [0.1015225571, 0.03959743532, 0.4841933672, 1.226476481, 0.05380792647, 0.02486603242, 0.06428163675, 0.5576403075, -0.3535230612]
seg4_gen1 = [-1.288243034, -1.462333419, -1.791035763, -2.291196377, -1.620514932, -0.5507917839, -1.514052131, -2.144056488, -0.9964500957, -1.203322232, -1.288243034]

seg3_gen200 = [-0.994039762, -1.023867135, -1.60183642, -1.123495789, -1.101276431, -0.7256849013, -1.02768712, -1.098612096, -0.3395070353, -0.8133859422]
seg4_gen200 = [-0.9684575587, -1.145829145, -0.8828304544, -1.526075062, -0.9375034762, -1.00397796, -1.34155856, -0.1054697576, -0.6819930568, -1.446478347]




U1, p = mannwhitneyu(seg3_gen1, seg4_gen1)
print("Parent generation 1: U1 = " + str(U1) + " p = " + str(p))
U1, p = mannwhitneyu(seg3_gen200, seg4_gen200)
print("Parent generation 200: U1 = " + str(U1) + " p = " + str(p))