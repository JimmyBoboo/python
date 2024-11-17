print("-----------1.3------------")
class course:
    def __init__(self, name, numbers_of_students, study_points=10):
        self.name = name
        self.numbers_of_students = numbers_of_students
        self.study_points = study_points
        
    def get_description(self):
        return f"The course {self.name} has {self.numbers_of_students} students" \
            f" and {self.study_points} study points"
                
                
programmering_1 = course("Programmering 1", 215)
print(programmering_1.get_description())

print("-------------1.4--------------------")

dyre_i_parken = {"honey badger": 2, "ape": 15, "zebra": 6, "giraffe": 4}

for dyr in dyre_i_parken:
    if dyre_i_parken[dyr] < 5:
        print(dyr.title())
        
        
print("----------------1.5-------------------------")

numbers = [5, 2, 3, 2, 4, 1]

sum_av_numbers = 0
for number in numbers:
    if number <= 2:
        sum_av_numbers += number
    else:
        sum_av_numbers += 1

print(sum_av_numbers)

print("--------1.6------")

dyr = ["honey badger", "giraffe", "ape", "zebra"]

dyr[1] = "elephant"

dyr.sort()

dyr = dyr[:2]

for dyrer in dyr:
    print (dyrer)
