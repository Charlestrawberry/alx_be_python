class Student:
    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects

    def get_name(self):
        print(f"{self.name} is my name and I am {self.age} Yr Old!")
        print("subjects and scores")
        for subject, score in self.subjects.items():
            print(f"- {subject}: {score}")
    
    def calc_avg(self):
        scores = self.subjects.values()
        avg = sum(scores) / len(scores)
        return round(avg, 2)

my_details = Student("Charles", 37, subjects={
    "Math": 85,
    "Science": 90,
    "English": 78
})
my_details.get_name()
print(my_details.calc_avg())


def student_menu():
    print("\n STUDENT MENU ")
    print("1. Add a student")
    print("2. View all Students")
    print("3. Bye Bye")

students = []

while True:
    student_menu()

    choice = input("Choose an option 1-3: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        subjects= {}

        while True:
            subject = input("Enter subject or (done/stop): ")
            if subject.lower() == "done":
                break
            score = float(input(f"Enter score: "))
            subjects[subject] = score

        new_student = student()