class student:

    def __init__(self,name,roll_number,cgpa):
        self.name = name
        self.roll_number =roll_number
        self.cgpa = cgpa

def sort_student(student_list):
    sorted_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
    return sorted_students

students = [
           student('hariharan','k111',7.8),
           student('akash','k112',9.8),
           student('sanjai','k113',8.8)
           ]

sorted_students = sort_student(students)

for student in sorted_students:
    print("name :",student.name," Student Roll number :",student.roll_number,"Student CGPA :",student.cgpa)
         
