from student import Student, course
import course_function as cf

nils_nilsen = Student("Nils", "Nilsen", 22, "IT678")
Programmering1 = course("Programmering 1", "ITF10219", 10)
Webutvikling = course("Webutvikling", "ITF18275", 10)
Design = course("Innføring i Design", "ITF28122", 10)

nils_nilsen.enroll_in_course(Programmering1)
nils_nilsen.enroll_in_course(Webutvikling)
nils_nilsen.enroll_in_course(Design)

print("Med Intern Funksjon")
print(nils_nilsen.get_total_credits())


print("Med Ekstern Funksjon")
print(cf.calculate_total_points(nils_nilsen.courses))

all_courses = [Programmering1, Webutvikling, Design]
print(cf.calculate_total_points(all_courses))

print(nils_nilsen.__init__.__doc__)

print(list.append.__doc__)