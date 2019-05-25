import csv

class DataParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_rows(self, province=None, type=None, sex=None, year=None):
        rows_list = []
        with open(self.file_name) as data_file:
            csv_reader = csv.reader(data_file, delimiter=';' )
            next(csv_reader)
            for row in csv_reader:
                if (province == row[0] or province == None) and (type == row[1] or type == None) and (sex == row[2] or sex == None) and (year == int(row[3]) or year == None):
                    rows_list.append(row)
        return rows_list

    #method assumes that data for women and men come in pairs one after another
    #creates a list with elements in format: [province, type(attended or passed), "wszyscy" (string implying its a merge of men and women), year, summed number men and women]
    def merge_women_and_men(self, list):
        result_list = []
        for x in range(0, len(list), 2):
            result_list.append([list[x][0], list[x][1], "wszyscy", list[x][3], str(int(list[x][4]) + int(list[x+1][4])) ])
        return result_list

    def get_provinces(self):
        provinces_list = []
        with open(self.file_name) as data_file:
            csv_reader = csv.reader(data_file, delimiter=';' )
            next(csv_reader)
            for row in csv_reader:
                provinces_list.append(row[0])
        provinces_set = set(provinces_list)
        return provinces_set









