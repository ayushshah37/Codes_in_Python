print("Enter 10 numbers")
List1 = list()
fileWrite = open("trial1.txt", "w")
for i in range(10):
    List1.append(int(input("Enter number : ")))
    fileWrite.write(str(List1[i]))
    fileWrite.write("\n")
fileWrite.close()
fileRead = open("trial1.txt", "r")
print(fileRead)
#read from the file
# fileRead = open("file1.txt", "r")
List = list()
# print(fileRead)
for line in fileRead:
    List.append(int(line))
List.sort()
print(List)
fileWrite1 = open("file2.txt", "w")
for i in range(len(List)):
    fileWrite1.write(str(List[i]))
    fileWrite1.write("\n")
