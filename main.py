faculty_file = open("requiredCS.txt", 'r')
all_class_lines = faculty_file.readlines()
print(all_class_lines)
for class_line in all_class_lines:
        loud_line = class_line.upper()
        words = loud_line.split(" : ")
        print(words[0])
        print(words[1])
faculty_file = open("faculty.txt")
all_faculty = faculty_file.readlines()
for faculty in all_faculty:
        
