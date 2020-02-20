#python 3.6.8
import itertools #for function "combination"

#opening file and saving it to a variable
file11=open("erg11_file.txt","r")
data=file11.readlines()
file11.close()
tetrades=[]
num_comb=[]

#getting the 6 numbers
numbers = input("Enter 6 numbers splited by',':\t").split(",")

#putting file11's 4-number-combinations in a list named 'tetrades'
for line in data:
    tetrada=line.split()
    tuple_tetrada=tuple(tetrada)
    tetrades.append(tuple_tetrada)

#using function "combination" to find every possible 4-number-combination out of the 6 numbers given
# and puting them in a list named 'num_comb'
for comb in itertools.combinations(numbers, 4):#comb type:tuple
    num_comb.append(comb)

#checking availability by checking if there is a combination in num_comb that's not in tetrades already
for comb in num_comb: 
    if comb not in tetrades:
        print("available combination:")
        print(comb)
        break
    elif comb==num_comb[-1]:
        print("there aren't any available combinations")