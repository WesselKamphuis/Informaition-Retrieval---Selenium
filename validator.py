# checks if two files are identical
import pandas as pd
from Validation.cohens_kappa import cohens_kappa
from Validation.jaccard_and_kendall import jaccard_and_kendall
import matplotlib.pyplot as plt
plt.close('all')

def main():
    path1 = 'Query_Results_Simon_v2/'
    path2 = 'Query_Results_Wessel_v2/Query_Results_Wessel_v2/'
    path3 = 'Preprocessed_results/'
    ch_dict = cohens_kappa(path1, path2)
    kt_dict, jaccard_dict = jaccard_and_kendall(path3)

    ch_df = pd.DataFrame.from_dict(ch_dict)
    kt_df = pd.DataFrame.from_dict(kt_dict)
    jaccard_df = pd.DataFrame.from_dict(jaccard_dict)

    print('Cohens Kappa in table view: \n', ch_df, '\n')
    print('kendall taus coefficient in table view: \n', kt_df, '\n')
    print('jaccard similarity score in table view: \n', jaccard_df, '\n')


if __name__ == '__main__':
    main()
