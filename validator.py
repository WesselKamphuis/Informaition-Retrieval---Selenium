# checks if two files are identical
import os
import scipy.stats as stats


def main():
    results = os.listdir('Preprocessed_results')

    for sub_folder in results:
        theme = 'Preprocessed_results/' + sub_folder
        print('\n', sub_folder)
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
                print(file, ': ', stats.kendalltau(l1, l2)[0])


if __name__ == '__main__':
    main()