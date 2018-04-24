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
assign_list ={
"assign01" : 1, "assign02" : 2, "assign03" : 3, "assign04" : 4,
"assign05" : 5, "check01a" : 6, "check01b" : 7, "check02a" : 8,
"check02b" : 9, "check03a" : 10, "check03b" : 11, "check04a" : 12,
"check04b" : 13, "check05a" : 14, "check05b" : 15, "check06a" : 16,
"check06b" : 17, "check07a" : 18, "check07b" : 19, "check08a" : 20,
"check08b" : 21, "check09a" : 22, "check09b" : 23, "check10a" : 24,
"check10b" : 25, "check11a" : 26, "check11b" : 27, "check12a" : 28,
"check12b" : 29, "check13a" : 30, "check13b" : 31, "class" : 32,
"old" : 33
}
#################################################
# TODO: read the file to be submitted
# format test: submit Hello.py /home/burtons/cs241/assign01/.
#################################################
print assign_list["assign01"];
