import os;
import sys;
fileToSubmit = sys.argv[1];

print "The file to be submitted is: " , fileToSubmit;

#################################################
# Set constants for Brother burtons numbers
# and the course numbers.
#################################################
professor = 36;
course = 5;

#################################################
# TODO: read the file to be submitted
# format test: submit Hello.py /home/burtons/cs241/assign01/.
#################################################
# garbage = raw_input();
garbage = raw_input();
professer_list = ["first"];
os.system("python testSubmit.py");
while True:
    # gets the last element of the array
    if professer_list[-1] == "Enter the corresponding number:":
        break
    else :
        professer_list.append(str(raw_input()));
