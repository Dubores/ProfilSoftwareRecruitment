from analyzer import Analyzer
from database import insert_data_into_db

#not needed, getting data from API
#file_name = "../dataset.csv"

insert_data_into_db()
analyzer = Analyzer()
command = ""

print("Welcome to Matura exam data analyzer. Type 'help' for list of available commands.")
while command != "quit":
    command = input()
    analyzer.command_dispatcher(command)


