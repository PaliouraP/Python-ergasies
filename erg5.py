#python 3.6.8
#opening file and saving it to a variable
file5=open("erg5_file.txt","r")
data=file5.readlines()
file5.close()
transformations=[]
for line in data:
    words=line.split()
    #check if word has more than 3 characters for each word in the file
    for word in words:
        if len(word)>3:
            #remove the first character from the word and add it to the end with 'ay'
            new_word=word[1:]+word[0]+"ay"
            transformations.append((word,new_word))
print(transformations)