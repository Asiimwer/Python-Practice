#Pulling and reading files
#with makes sure the file is opened and closed safely,"r" puts it in reader mode
#.read reads the file.
#"file" is a varibale
 
# with open("myfile.txt", 'a') as file:
#   content = file.write('\nthis is the fourth line')
 
# with open('myfile.txt', 'r') as file:
#  content = file.read()
#  print(content)
 #"w" writes or overwrites a file LOOK OUT FOR THE "\N" for a new line
with open('myfile2.txt', 'r') as new_file:
   content_2 = new_file.read()
with open('myfile2.txt', 'r') as new_file:
   print(new_file.read())
 
with open('test.txt','w') as text:
    statement = text.write('Hello Word')
with open('text.txt','r') as text:
    print(text.read())
