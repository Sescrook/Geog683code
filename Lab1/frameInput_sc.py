# the following script takes input from the user and displays
# it in a frame based on user-defined formatting
#
# SKILLS:
#       1.decision making with if-elif-else
#       2.importing and using modules (string)
#       3.handling user input
#
# Author: Arika Ligmann-Zielinska
# date: September 10, 2006
# version 01
#
# IMPORTS --------------------------------------------------------
import string
# USER INPUT -----------------------------------------------------
raw_sentence = raw_input("Type a sentence: ")
print "-------------------------------------"
print "Format your sentence -> use the keys:"
print "<c> Capitalize"
print "<u> Upper Case"
print "<l> Lower Case"
print "-------------------------------------"

choice = raw_input("What operation would you like?")

# *********** PUT YOUR CODE HERE *********************************
# ask the user to select the format type and put it to
# a variable named format
# CHECKING FORMAT TYPE -------------------------------------------
##
##format = string.lower(format) # why do that? EXPLAIN
##

print choice

if choice == "l":
    raw_sentence = string.lower(raw_sentence)
elif choice == "u":
    raw_sentence = string.upper(raw_sentence)
elif choice == "c":
    raw_sentence = string.capitalize(raw_sentence)
else:
    print "ERROR, you entered a non-option!"

### *********** PUT YOUR CODE HERE *********************************
### Check format type selected by the user (letter)
### if 'c' then use an appropriate string function
###               to capitalize
### if 'u' then use an appropriate string function to put
###               to upper case
### if 'l' then use an appropriate string function to put
###               to lower case
### finally, if user accidentally typed something else
### then inform the user about the mistake and put the sentence
### to some default (e.g. do not user formatting)
##
### FRAME PARAMETERS -----------------------------------------------
    
sentence_length = len(raw_sentence)
frame_width = sentence_length + 6
left_margin = 10

### PUTTING SENTENCE IN A FRAME ------------------------------------
print
print " " * left_margin + "+" + "-" * frame_width + "+" # DESCRIBE: it's formatting the box for the string to go in.
print " " * left_margin + "|" + " " * frame_width + "|"
print " " * left_margin + "|   " + raw_sentence + "   |"
print " " * left_margin + "|" + " " * frame_width + "|"
print " " * left_margin + "+" + "-" * frame_width + "+"

### SENTENCE STATISTICS --------------------------------------------

print
print "Sentence length:", sentence_length
print "Checking for occurences of letters <a>,<b> and <c>"
sentence = string.lower(raw_sentence) # why do that? EXPLAIN: Because python is case sensitive, to count upper and lower case letters all should be lower.

num_a = string.count(sentence, "a")
num_b = string.count(sentence, "b")
num_c = string.count(sentence, "c")
print "There are " + str(num_a) + " letter a's, " + str(num_b) + " letter b's, and " + str(num_c) + " letter c's up in here!"


### *********** PUT YOUR CODE HERE *********************************
##a_in_sentence = # use proper string function to check how many
### times 'a' occurs in sentence, do the same for 'b' and 'c'
##
##if a_in_sentence == 0:
##    print "There is no <a> in: " + sentence
##else:
##    print "<a> occured", a_in_sentence, "times"
##
### *********** PUT YOUR CODE HERE *********************************
### write similar code for 'b' and 'c' 
