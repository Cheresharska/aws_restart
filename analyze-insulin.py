import re
string = open("preproinsulin-seq.txt").read()
sub_str_arr= ["ORIGIN", "1", "61", "//"]

spl_arr= string.split()

for sub_elem in sub_str_arr:
    
    spl_arr.remove(sub_elem)
    
print("".join(spl_arr))


"""
Your module description
"""

#input file
infile = "preproinsulin-seq.txt"
#output file to write the result to
outfile = "preproinsulin-seq-clean.txt"
#for each line in the input file

delete_list = ["ORIGIN", "//", "61", "1", " ", "\n"]
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)

	#read replace the string and write to output file
	
	#open file in read mode
file = open("preproinsulin-seq-clean.txt", "r")

#read the content of file
data = file.read()

#get the length of the data
number_of_characters = len(data)

print('Number of characters in text file :', number_of_characters)

print(data)
twenty_four_char=data[0:24]
print(f'The 24 characters are:', twenty_four_char)



