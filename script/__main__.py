from analyzer import Analyzer

file_name = "../dataset.csv"
analyzer = Analyzer(file_name=file_name)
command = ""

while command != "quit":
    command = input()
    analyzer.command_dispatcher(command)


