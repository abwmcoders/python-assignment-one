import csv
from datetime import datetime


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

file = "pupils.csv"



def main():
    # read compund list
    students_list = read_compound_list(file)
    print('\n\n Reading the student list ...\n\n\n')
    print(students_list)

    #lambda function 
    birthdate = lambda student_index: students_list[student_index][BIRTHDATE_INDEX]
    print('\n\n\n Reading a student birthdate ...\n\n\n\n')
    print(birthdate(0))

    # sort by birth date
    sorted_list = sorted(students_list, key= lambda s_list: s_list[BIRTHDATE_INDEX], reverse=True)
    print('\n\n\n ordering sorted list from oldest to youngest ...\n\n\n')
    print(sorted_list)
    print('\n\n\n ordering sorted list by given name ...\n\n\n')
    sorted_list = sorted(students_list, key= lambda s_list: s_list[GIVEN_NAME_INDEX])
    print(sorted_list)
    print('\n\n\n ordering sorted list by surname name additional ...\n\n\n')
    sorted_list = sorted(students_list, key= lambda s_list: s_list[SURNAME_INDEX])
    print(sorted_list)
    print('\n\n\n ordering sorted list by birth month and day ...\n\n\n')
    def splitMonthDate(student):
        split = student[BIRTHDATE_INDEX].split('-')
        return split[1] + '-' + split[2]
    #sorted_list = sorted(students_list, key= lambda s_list: datetime.strptime(s_list[BIRTHDATE_INDEX],'%Y-%m-%d'))
    sorted_list = sorted(students_list, key=splitMonthDate)
    print(sorted_list)
    
    

    # student list line by line
    com_list = read_compound_list(file)
    print('\n\n\ninitializing student list on new line\n\n\n')
    print_list(com_list)



def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list


def print_list(list_item):   
    for line in list_item:
        print(line)  


if __name__ == "__main__":
    main()