# Task 1 & 2
with open("example.txt","w") as file:
 file.write("I am writing in a text file\n")
 file.write("How are you\n")
  
with open("example.txt","r") as file:
 f=file.read()
 print(f)
 file.seek(0)

 line_count=0
 word_count=0
 for line in file:
   
   line_count+=1
   
   
   words=line.split()
   word_count += len(words)
   
print(line_count)#
print(word_count)

