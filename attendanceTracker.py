import csv

original_class_file = input("Enter original class filename:") #add .csv extension
attendance_file = input("Enter attendance filename:") #add .csv extension

attendance_list = []
class_list = []
present = []
absent = []

with open(attendance_file, 'r') as file1:
    reader = csv.reader(file1)
    for row in reader:
        attendance_list.append(row)

with open(original_class_file, 'r') as file2:
    read = csv.reader(file2)
    for each in read:
        class_list.append(each)

#sorting the files taking just the names from them

sorted_class_list = []
sorted_attendance_list = []

for i in range(len(class_list)) :
    sorted_class_list.append(class_list[i][1]) #class list names are present in second column

for i in range(len(attendance_list)):
    sorted_attendance_list.append(attendance_list[i][0]) #attendance list names are present in first column

length = len(sorted_class_list)

i = 0

while (i < length):

    if sorted_class_list[i] in sorted_attendance_list:
        present.append(sorted_class_list[i])
        i += 1

    else:
        absent.append(sorted_class_list[i])
        i += 1


#print("Presentees are: ")  #Uncomment these two to print presentees list
#print(present)
print("No. Present: " + str(len(present)))
print("Absentees are: ")
print(absent)
print("No. Absent: " + str(len(absent)))
