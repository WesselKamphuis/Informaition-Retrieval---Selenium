import xlrd
import pandas as pd


def load_coordinates(filename):
    wb = xlrd.open_workbook(filename)
    return wb


def book_to_table(book):
    names = book.sheet_names()
    print(names)
    tables = {}
    for name in names:
        print(name)
        tables[name] = pd.read_excel(book, sheet_name=name)
    print("the table of the pvv: \n", tables.get('PVV'))
    return tables


def main():
    filename = 'Coordinates.xlsx'
    book = load_coordinates(filename)
    tables = book_to_table(book)
    return tables


if __name__ == '__main__':
    main()
