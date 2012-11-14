import pymongo

conn = pymongo.Connection("mongodb://localhost")
students = conn.school.students

student_list = students.find()

for student in student_list:
    lowest_grade = None
    for score in student["scores"]:
        if (score["type"] == "homework" and 
            (lowest_grade is None or score["score"] 
                < lowest_grade["score"])):
            lowest_grade = score
    if lowest_grade is not None:
        students.update({"_id": student["_id"]}, {"$pull": {"scores": lowest_grade}})

print("Finished the task boss man!")
