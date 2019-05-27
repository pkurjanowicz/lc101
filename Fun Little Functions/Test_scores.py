def is_alpha(word):
    for letter in word:
        new_word = ''.join([letter for letter in word if letter.isalpha()])
    return new_word

def main():

    students = []

    # Use a space to allow for the while check below
    new_student = " "

    # Get student names
    while (new_student != ""):
        new_student = input("Student's name (or press ENTER to finish)")
        if new_student != "":
            if new_student == new_student.isalpha:
                students.append(new_student)
            else:
                students.append(is_alpha(new_student))

    # Get student grades
    grades = [0]*len(students)
    for idx, student in enumerate(students):
        new_grade = float(input("Grade for " + student + ": "))
        grades[idx] = new_grade
        
    dictionary = dict(zip(students, grades))
    print("\nClass roster:")
    for students in dictionary:
        print (students, "("+ str(dictionary[students])+ ")")
    avg = sum(grades) / len(grades)
    print("\nAverage grade: " + str(avg))

main()