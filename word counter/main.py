#import csv and string
import csv
import string
#assign variable to take the string 
translator = str.maketrans('','', string.punctuation )

#make an array var
word_count = {}

#open and read in the text document
text = open('sample.TXT').read()
#assign variable to split the text 
words = text.split()

#itterate over words 
for word in words :

#assign var for translate to lower 
    word = word.translate(translator).lower()
#assign var to get word count 
    count = word_count.get(word, 0)
#incrament count count
    count+=1
#make word count with  array of word equal to count 
    word_count[word] = count
#make a variable to store the sorted list containeing wird_count key is word count.get, reverse is true 
word_count_list = sorted(word_count, key=word_count.get, reverse=True)

#itterate through word in word count list 
for word in word_count_list[:20]:
#print word word count with array of word 
    print(word, word_count[word])
#var for output file to be opened and write to it 

output = open("output.txt" , 'w')
#var for writer to write the output file
writer = csv.writer(output) 

#assign rows for word and count
writer.writerow(['word' , 'count']) 

#for word in word count list 
for word in word_count_list:

#write row word word count with array of word
    writer.writerow([word, word_count[word]])