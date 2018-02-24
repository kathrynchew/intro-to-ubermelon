log_file = open("um-server-01.txt")
# open text file with all sales data, assign contents to variable "log_file"


def sales_reports(log_file):
# define a function that takes the log_file variable as an argument
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Tue":
            print line
# create a for loop that will iterate through the log_file contents line-by-line
# for each iteration (line), strip any white space from the right side of the line
# for each iteration (line), set the values in indices [0:3] (characters in a string) equal to the variable "day"
# check the value assigned to "day"; if it matches the sequence "Tue", print that line.


sales_reports(log_file)
# call the function using the imported text file
