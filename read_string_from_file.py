## Function to read string from a plain text file
## This file refers the text file flying_circus_cast.txt file in the execution

def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open (filename) as f:
        for line in f:
            cast_list.append(line.split(',')[0])
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    return cast_list

c_list = create_cast_list('../python-programming/flying_circus_cast.txt')
for actor in c_list:
    print(actor)