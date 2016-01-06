# word = "Things"
# # print word[0:len(word)]
#
# word+= "j"
# print word
# print repr("hello world") #this will print it with surrounding quotes.

#backticks are also helpful when printing numbers
# temp = 42
# print "the temp is " + `temp`
#or use repr()
# print "the temp is " + repr(temp)

#long strings
print ''' this will go on
for oh so long
over so many lines
cucumber'''
#without the triple quotes, this would error. it prints with th eline breaks.
print "hello \
world"
#that \ breaks the line break, so it returns inline
#even here
print 3 + 5 \
+ 4 +\
4

# \n will add a line break. if your string contains \n (as in not a line break)
# break the line break like so \\n

print "line \\n break"
