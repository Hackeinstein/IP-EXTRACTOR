# importing the module
import re
print('IP EXTRACTOR 1.0 BY DARKWEBDEITY')

filename=input("Input list name :  ")
# opening and reading the file
with open(filename) as fh:
   fstring = fh.readlines()
 
# declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
 
# displaying the extracted IP addresses
for index, line in enumerate(fstring):
    number=("{}".format( line.strip()))
    check=(pattern.search(number)[0])
    f = open("ipextracted.txt", "a")
    f.write(check+"\n")
    f.close()

