#Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, 
#and print out the results to the screen. I have a .txt file for you, if you want to use it!

f = open('nameslist.txt', 'r')

reading = f.readline()
num_lines = sum(1 for line in f)
print(num_lines)
