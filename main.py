the_string = input("Type something: ")
string_size = len(the_string)
the_string2 = the_string[0:int(string_size/2)] 
string_size = int(len(the_string2) - 2) 
the_string3 = the_string2[string_size:string_size +2]
print(the_string2)
print(the_string3)

#in this exercise i had to cut a world in half print it and then get the last two letters and print it