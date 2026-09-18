#features: study hours, attendance, midterm, assignments_submitted
#label: passed
#calculating the average of study hours, attendance, midterm, assignments_submitted of
#students that passed and students that didn't pass

import csv

INPUT_FILE = "student_data.csv"

def read_file(file):
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

def main():

    study_hours_passed = 0
    attendance_passed = 0
    midterm_passed = 0
    assignments_submitted_passed = 0

    study_hours_fail = 0
    attendance_fail = 0
    midterm_fail = 0
    assignments_submitted_fail = 0

    passed = 0
    fail = 0


    students = read_file(INPUT_FILE)
    for student in students:
        if student["passed"] == "1":
            study_hours_passed += float(student["study_hours"])
            attendance_passed += float(student["attendance_rate"])
            midterm_passed += float(student["midterm_score"])
            assignments_submitted_passed += float(student["assignments_submitted"])
            passed += 1

        else:
            study_hours_fail += float(student["study_hours"])
            attendance_fail += float(student["attendance_rate"])
            midterm_fail += float(student["midterm_score"])
            assignments_submitted_fail += float(student["assignments_submitted"])
            fail += 1
    
    print(f"Average rate for study_hours of student who passed: {study_hours_passed/passed}")
    print(f"Average rate for attendance rate of student who passed: {attendance_passed/passed}")
    print(f"Average rate for midterm of student who passed: {midterm_passed/passed}")
    print(f"Average rate for assignments submitted of student who passed: {assignments_submitted_passed/passed}")
    print()
    print(f"Average rate for study_hours of student who fail: {study_hours_fail/fail}")
    print(f"Average rate for attendance rate of student who fail: {attendance_fail/fail}")
    print(f"Average rate for midterm of student who fail: {midterm_fail/fail}")
    print(f"Average rate for assignments submitted of student who fail: {assignments_submitted_fail/fail}")

main()