import pandas as pd
from Validation.cohens_kappa import cohens_kappa
from Validation.jaccard_and_kendall import jaccard_and_kendall
import xlwt
import openpyxl


def main(version):
    path1 = 'Query_Results_Simon_' + version + '/'
    path2 = 'Query_Results_Wessel_' + version + '/'
    path3 = 'Preprocessed_results_' + version + '/'
    ck_dict = cohens_kappa(path1, path2)
    kt_dict, jaccard_dict = jaccard_and_kendall(path3)

    ch_df = pd.DataFrame.from_dict(ck_dict)
    kt_df = pd.DataFrame.from_dict(kt_dict)
    jaccard_df = pd.DataFrame.from_dict(jaccard_dict)

    # replaces NaN values with a 0, to be able to compute the average values
    ch_df = ch_df.fillna(0)
    kt_df = kt_df.fillna(0)
    jaccard_df = jaccard_df.fillna(0)

    print('Cohens Kappa in table view: \n', ch_df, '\n')
    print('kendall taus coefficient in table view: \n', kt_df, '\n')
    print('jaccard similarity score in table view: \n', jaccard_df, '\n')

    excel_name = 'validation_metrics_' + version + '.xls'
    with pd.ExcelWriter(excel_name) as writer:
        ch_df.to_excel(writer, sheet_name='Cohens_Kappa')
        kt_df.to_excel(writer, sheet_name='Kendall_Tau')
        jaccard_df.to_excel(writer, sheet_name='Jaccard_Similarity')


if __name__ == '__main__':
    main('v2')
    main('v3')
    main('v4')
