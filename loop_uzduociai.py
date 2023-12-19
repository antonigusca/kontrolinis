number_of_students = int(input("Enter the number of students: "))   #praso ivest studentu kieki
students_list = []  #saugomi studentu vardai
student_grade_sum = 0   #laikina kintamaji kuri laiko studentu pazymu suma
student_average = []    #kintamaji kuri laiko vidutini studentu pazymejima
student_name_and_grade_dict = {}    #zodynas kuris laiko studentu ir pazymejimus

for i in range(number_of_students):
    one_student = input("Enter Student name: ")     #prasymas ivest studento varda
    students_list.append(one_student)   #prideda studento varda i lista

    for x in range(3):
        grades = int(input(f"Enter grade {students_list[i]} (0-100) staudents: "))    #prasymas ivest studento pazymejima
        student_grade_sum += grades     #sumuojamos studento pazymejimus
    student_average.append(student_grade_sum/3)     #skaiciuojama studento vidurkis
    student_grade_sum = 0   #resetina studento pazymejimu suma kad apskaiciuoti kito studento pazymejimu suma

student_name_and_grade_dict = dict(zip(students_list, student_average))     #sujungiama studentu ir vidurkiu sarasus ir daromas zodymas
for student_name, grades in student_name_and_grade_dict.items():
    print(f"Average grade for {student_name}: {grades}")    #spausdinamas zodymas

#deja nepavyko man padaryti if'o kad tikrintu ar ivesta pazyma maziau 0 ar daugiau 100