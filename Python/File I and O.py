f = open("demo.txt","r")
data =f.read(20)     # 20 indicats no of words
print(data)
print(type(data))
f.close()


#Read  / Read line to a file
'''f = open("demo.txt","r")    # "r" represents read only
line1 =f.readline()
line2 =f.readline()  # for leaving space 
line3 =f.readline()
print(line1)
print(line2)
print(line3)
f.close()'''

#Write to a file
'''f = open("demo.txt","w")    #"w" represents over write whole file

f.write("hello i am learning python. its nice to see you")

f.close()'''


'''f = open("demo.txt","a")    #"a" represents that your new data is being stored next to previous data

f.write("\nhello how are you.\nI am bob")

f.close()'''


'''f=open("Hello.txt","w")     #we can create a file without creating one.
f.close()'''




'''f=open("demo.txt","r+")    #"r+" represents read and overwrite from start word to word
f.write("abcde")
print(f.read())
f.close()'''




'''f=open("demo.txt","w+")    #"w+" represents read and overwrite whole file
f.write("abcdeff")         #"a+" represents append and read 
print(f.read())f
f.close()'''


#            using Syntax"with 
'''with open("demo.txt","r") as f:
    data=f.read()
    print(data)'''

'''with open("demo.txt","w") as f:
    f.write("welcome to python learning class")'''
    

#            Deleting a file

'''import os
os.remove("sample.txt")'''


#create a new file "practice.txt" using python .Add the following DATA
#hi everyone
#we are learning Filei/o 
#using java
#i like programming java

'''with open("practice.txt","w") as f:
    f.write("Hi everyone \nwe are learning FileI/O \n")
    f.write("using Java \nI like programming Java ")'''

#WAF that replaces all occurances of "Java" with "Python" in above file
'''with open("practice.txt","r") as f:
    data = f.read()
new_data = data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)'''


#Search if the word "learning" exists in the file or not
'''word="learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not found")'''
    

'''def check_learning(word):
    word="learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not found")

check_learning()'''



#WAFto find in which line of the file does the word"learning" occur fist 
#print -1 if not found


'''def check_for_line():
    word="learning"
    data =True
    line_no =1
    with open("practice.txt","r") as f:
        while data:
            data =f.readline()
            if(word in data):
                print(line_no)
            line_no+=1
            
    return -1
print(check_for_line())'''


#from a file containing nos seperated by comma ,print the count of even nos.

'''with open("practice.txt","r") as f:
    data =f.read()
    print(data)
    
num =""
for i in range(len(data)):
    if(data[i]==","):
        print(int(num))
        num=""
    else:
        num+=data[i]'''

'''count =0 
with open("practice.txt","r") as f:
    data =f.read()
    
    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1

print(count)'''


























