#python 3.6.8
#opening file and saving it to a variable
file1=open("erg1_file.txt","r")
data=file1.readlines()
file1.close()

for line in data:
    words=line.split()

transformations=[]#list with old word and new word
biggest=['','','','','']#list with 5 biggest words
#vowels
vowels=('a','e','i','o','u','y')

#finding the 5 biggest words in the file and putting them in an array
for i in range(5):   
    for word in words:
        if len(word)>len(biggest[i]):
            biggest[i]=word
            words.remove(word)

for word in biggest:
    old_word=word
    #removing the vowels
    for x in word.lower():
        if x in vowels:
            word=word.replace(x,"")
    #reversing the word
    word=word[::-1]
    transformations.append((old_word,word))
print(transformations)