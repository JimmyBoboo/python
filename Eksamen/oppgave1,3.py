
print("-----------1.1------------")
a = 4 
b = 2
c = (a + b) / b

print (c**2)


print("-----------1.2------------")
tall = []

for x in range(5):
    tall.append(x)
print (tall)

tall = []

for x in range(5):
    tall.insert(x, 0)
print (tall)


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

print("-------1.7-------")

# Alligator, cat, dodo, dog, elephant, gorilla

animals = ['elephant', 'dog', 'cat', 'gorilla', 'dodo']

animals = animals [1:3]

animals [0] = 'alligator'

animals.sort(reverse=True)

print(animals)

print("---------1.8------------")

shopping_list = {}

def add_item(item_name, quanity=1):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quanity
    else:
        shopping_list[item_name] = quanity
        
add_item("bread", 2)
add_item("Milk")
add_item("Milk", 2)
add_item("bread", 2)
add_item("eggs")
print(shopping_list)


print("------------1.9------------")

x = 0

for i in range(0, 5, 2):
    x += i

print(x)

for i in range(0, 5):
     x += i

print(x)    


print("------------1.10----------")

a = 5
b = 2
c = 0

c += a ** b
print (c)

# 25 + 1
c += a % b
print(c)

# 26 + 1 = 27
c += a - b * 2
print(c)

c //= b
print(c)

print("---------1.11--------")

class game:
    def __init__(self, name, genre, age_rating=18):
        self.name = name
        self.genre = genre
        self.age_rating = age_rating
        
    def description(self):
        return f"The game {self.name}, is of the genre {self.genre} and has an age rating of {self.age_rating}"
    
game1 = game("Hades", "Rogue-lite", 12)
game2 = game("God of War", "Action")

print(game1.age_rating)
print(game2.description())
        
        
print("-----------1.12-------------")

randomlist = [1, 'a', 2, 'b', 3]
result = 0

for entry in randomlist:
    try:
        result += int(entry)
    except ValueError:
        print("A ValueError Occured")

print(f"The sum is: {result}")

