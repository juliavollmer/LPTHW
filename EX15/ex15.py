from sys import argv #imports module

script, filename = argv #assigns variables to argument

txt = open(filename) #assign variable to opened file

print "Here's your file %r:" % filename #print the name of the file
print txt.read() #print the content of file
txt.close() #close file

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
