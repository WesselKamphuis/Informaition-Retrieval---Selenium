import os
import sklearn.metrics as metrics


def cohens_kappa(path1, path2):
    themes = os.listdir(path1)
    ch_dict = {}
    for sub_folder in themes:
        ch_dict[sub_folder] = {}
        results1 = os.listdir(path1 + sub_folder)
        results2 = os.listdir(path2 + sub_folder)
        # print('the current theme: ', sub_folder)
        for i in range(len(results1)):
            if results1[i] != '[Party - Municipality]':
                # print('the file name: ', results1[i])
                file1 = open(path1 + sub_folder + '/' + results1[i], 'r')
                file2 = open(path2 + sub_folder + '/' + results2[i], 'r')

                l1 = []
                l2 = []
                for line1 in file1:
                    l1.append(line1)
                for line2 in file2:
                    l2.append(line2)
                try:
                    ch_dict[sub_folder][results1[i]] = metrics.cohen_kappa_score(l1, l2)
                except ValueError:
                    print("\n Found two files of different length. The files for: ", results1[i], " in the theme: ",
                          sub_folder, ", do NOT match \n ")
    return ch_dict
