exam_passed = {"Мария", "Ксения"}
is_subset = exam_passed.issubset(all_students)
is_superset = all_students.issubset(exam_passed)
print("Множество exam_passed является подмножеством all_students:", is_subset)
print("Множество all_students является подмножеством exam_passed:", is_superset)
