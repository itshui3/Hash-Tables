# Implement me.

# Given a file(or set) of words
# Determine the occurrence of each word (It doesn't seem like I have to store every occurence, just determine a count)
# Using a hash table, I can set the word as key to map words to a data placement and assign a tuple with the word and a count value

# 1)I need to organize the set of words in such a way that I can iterate through each one
# 2)I need to perform a check to determine whether key already exists or not
# 3)If it exists, I can increment count
# 4)If it does not exist, I can make count = 1 and add that key value pair in the table

# 5)Iterate through the resulting object with a for in loop to map out words + occurences in hash counts