import sys
import csv

#ensure argv has 2 arguments (lines filesname and required filename)
if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
if len(sys.argv) >3:
        sys.exit("Too many command-line arguments")
#check that it is a python file
elif not sys.argv[1].endswith("csv") and sys.argv[2].endswith("csv"):
        sys.exit("Not a valid csv file")
student =[]

#set the input and output files
input_filename = sys.argv[1]
output_filename = sys.argv[2]

#open input as r which is default, outout as w which is write
try:
        with open(input_filename) as file, open(output_filename, mode="x") as target:

                        reader = csv.DictReader(file)

        #setup the fieldnames for output
                        fieldnames = ["house","first","last"]
                        writer = csv.DictWriter(target, fieldnames=fieldnames)
                        #write the header, as this doesn't need to be in the loop

                        writer.writeheader()

                        for row in reader:

                        #take beforename - it has a space before it
                                full_name = row[" beforename"]
                                #split first and last names into variables
                                last,first = full_name.split(",")
                                #remove spaces
                                first = first.lstrip()
                                last = last.strip()
                                #append the details to a dictionary
                                student.append({"house": row["house"], "first": first, "last": last})
                                #write the dictionary to a csv
                                writer.writerow({"house":row["house"], "first":first, "last":last})
except FileExistsError:
       sys.exit("File already exists")
