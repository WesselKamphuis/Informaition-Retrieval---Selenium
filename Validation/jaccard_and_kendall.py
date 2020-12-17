import os
import scipy.stats as stats


def jaccard(file1, file2):
    intersection = len(list(set(file1).intersection(file2)))
    union = (len(file1) + len(file2)) - intersection
    return float(intersection) / union


def jaccard_and_kendall(path):
    results = os.listdir(path)
    kt_dict = {}
    jacc_dict = {}
    for sub_folder in results:
        kt_dict[sub_folder] = {}
        jacc_dict[sub_folder] = {}
        theme = path + sub_folder
        for file in os.listdir(theme):
            if file != '[Party - Municipality]':
                f1_path = theme + '/Groenlinks - Nijmegen.txt'
                f2_path = theme + '/' + file

                f1 = open(f1_path, 'r')
                f2 = open(f2_path, 'r')

                l1 = []
                l2 = []
                for line1 in f1:
                    l1.append(line1)
                for line2 in f2:
                    l2.append(line2)
                kt_dict[sub_folder][file] = stats.kendalltau(l1, l2)[0]
                jacc_dict[sub_folder][file] = jaccard(l1, l2)
    return kt_dict, jacc_dict
