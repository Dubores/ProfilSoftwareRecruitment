from .data_parser import DataParser

class Analyzer:
    def __init__(self):
        self.parser = DataParser()

    def command_dispatcher(self, command):
        #command parsing
        split_command = command.split(" ")

        if split_command[0] == "avg":
            year = int(split_command[1])
            province = split_command[2]
            if len(split_command) == 4:
                if split_command[3] == "-F":
                    self.average_till_year(year, sex="kobiety", province=province)
                elif split_command[3] == "-M":
                    self.average_till_year(year, sex="mężczyźni", province=province)
            else:
                self.average_till_year(year, province=province)

        elif split_command[0] == "passrate":
            province = split_command[1]
            if len(split_command) == 3:
                if split_command[2] == "-F":
                    self.pass_rate_percentage_all_years(sex="kobiety", province=province)
                elif split_command[2] == "-M":
                    self.pass_rate_percentage_all_years(sex="mężczyźni", province=province)
            else:
                self.pass_rate_percentage_all_years(province=province)

        elif split_command[0] == "bestinyear":
            year = split_command[1]
            if len(split_command) == 3:
                if split_command[2] == "-F":
                    self.best_pass_rate_in_year(sex="kobiety", year=year)
                elif split_command[2] == "-M":
                    self.best_pass_rate_in_year(sex="mężczyźni", year=year)
            else:
                self.best_pass_rate_in_year(year=year)

        elif split_command[0] == "regression":
            if (len(split_command)) == 2:
                if split_command[1] == "-F":
                    self.regression_provinces(sex="kobiety")
                elif split_command[1] == "-M":
                    self.regression_provinces(sex="mężczyźni")
            else:
                self.regression_provinces()

        elif split_command[0] == "compare":
            province1 = split_command[1]
            province2 = split_command[2]
            if (len(split_command)) == 4:
                if split_command[3] == "-F":
                    self.provinces_comparison(province1=province1, province2=province2, sex="kobiety")
                elif split_command[3] == "-M":
                    self.provinces_comparison(province1=province1, province2=province2, sex="mężczyźni")
            else:
                self.provinces_comparison(province1=province1, province2=province2)

        elif split_command[0] == "help":
            print("help menu")

        else:
            print("Improper command. Type 'help' to display possible options.")

    #method returns data in form: [province, year, pass rate for that year and teritory]
    def pass_rate(self, sex=None, province=None, year=None):
        attend_list = []
        pass_list = []
        result_list = []

        attend_list.extend(self.parser.get_rows_from_db(year=year, sex=sex, type="przystąpiło", province=province))
        pass_list.extend(self.parser.get_rows_from_db(year=year, sex=sex, type="zdało", province=province))

        if sex == None:
            attend_list = self.parser.merge_women_and_men(attend_list)
            pass_list = self.parser.merge_women_and_men(pass_list)

        for x in range(0, len(attend_list)):
            result_list.append([pass_list[x][0], pass_list[x][3], int(pass_list[x][4]) / int(attend_list[x][4])])

        return result_list

    def average_till_year(self, year, sex=None, province=None):
        list = []
        no_years = int(year) - 2010 + 1
        sum = 0

        #get all rows from particular years, province, and of particular sex(if specified)
        for x in range(2010, year + 1):
            list.extend(self.parser.get_rows_from_csv(year=x, sex=sex, type="przystąpiło", province=province))
        print(list)

        #sum number of people from all acquired rows
        for x in list:
            sum = sum + int(x[4])

        average = sum/no_years
        print("Average number of people per year who attended Matura exam from 2010 to {0} in {1}: {2}".format(year, province, average))

    def pass_rate_percentage_all_years(self, sex=None, province=None):
        result_list = []

        for x in range(2010, 2019):
            result_list.extend(self.pass_rate(sex=sex, province=province, year=x))

        for x in range(2010, 2019):
            print("Pass rate for {0} in year {1}: {2:.1%}".format(province, x, result_list[x-2010][2]))

    def best_pass_rate_in_year(self, year=None, sex=None):
        result_list = []
        result_list.extend(self.pass_rate(year=int(year), sex=sex))

        result_list.sort(key=lambda x: x[2], reverse=True)

        print("Province with the best pass rate in {0}: {1}".format(year, result_list[0][0]))

    def regression_provinces(self, sex=None):
        provinces_passrate_list = []
        results_list = []
        provinces_set = self.parser.get_provinces()

        for x in provinces_set:
            provinces_passrate_list.append(self.pass_rate(sex=sex, province=x))

        #provinces_passrate_list consists of lists, one for each province which have 9 elements (one for each year) in format: [province, year, pass_rate]
        #sort by years from 2010 to 2018
        for x in provinces_passrate_list:
            x.sort(key=lambda y: y[1])

        for x in provinces_passrate_list:
            for y in range(0, 8):
                if x[y][2] > x[y+1][2]:
                    results_list.append([x[0][0], x[y][1], x[y+1][1]])

        print("Provinces that noted a regression in consecutive years:")
        for x in results_list:
            print("{0}: {1} -> {2}".format(x[0], x[1], x[2]))

    def provinces_comparison(self, province1, province2, sex=None):
        compare_list = []
        result_list =[]

        compare_list.extend(self.pass_rate(sex=sex, province=province1))
        compare_list.extend(self.pass_rate(sex=sex, province=province2))

        compare_list.sort(key=lambda x: x[1])

        for x in range(0, len(compare_list), 2):
            if compare_list[x][2] > compare_list[x+1][2]:
                result_list.append([compare_list[x][1], compare_list[x][0]])
            else:
                result_list.append([compare_list[x][1], compare_list[x+1][0]])

        print("Comparison of pass rate in provinces {0} and {1} over the years:".format(province1, province2))
        for x in result_list:
            print("{0} -> {1}".format(x[0], x[1]))












