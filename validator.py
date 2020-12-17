# checks if two files are identical
import os
import scipy.stats as stats
import pandas as pd
import sklearn.metrics as metrics
from Validation.cohens_kappa import cohens_kappa
from Validation.jaccard_and_kendall import jaccard, jaccard_and_kendall


def main():
    path1 = 'Query_Results_Simon_v2/'
    path2 = 'Query_Results_Wessel_v2/Query_Results_Wessel_v2/'
    path3 = 'Preprocessed_results/'
    ch_dict = cohens_kappa(path1, path2)
    kt_dict, jaccard_dict = jaccard_and_kendall(path3)
    print('cohens kappa: ', ch_dict)
    print('kendall taus coefficient: ', kt_dict)
    print('jaccard similarity score: ', jaccard_dict)


if __name__ == '__main__':
    main()
