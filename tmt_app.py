import random
from tkinter import *
from tkinter import ttk
root = Tk()

def grade_calculator():
    print("-----------------------0-Grade Calculator-0-----------------------")
    score = input("Enter the student's score (e.g., 18/20): ")

    try:
        num, den = score.split('/')
        num = int(num)
        den = int(den)
        percentage = (num / den) * 100
    except Exception as e:
        print("Invalid input format. Please enter like '18/20'.")
        return

    if percentage >= 100:
        letter = "A+"
    elif percentage >= 90:
        letter = "A"
    elif percentage >= 80:
        letter = "B"
    elif percentage >= 70:
        letter = "C"
    elif percentage >= 60:
        letter = "D"
    else:
        letter = "F"

    print(f"Percentage: {percentage:.2f}%")
    print(f"Letter Grade: {letter}")

def quiz_maker():
    print("-----------------------0-Quiz Maker-0-----------------------")
    questions = []
    num_questions = int(input("How many questions do you want to add? "))
    for i in range(num_questions):
        q = input(f"Enter question {i + 1}: ")
        a = input("Enter correct answer: ")
        questions.append((q, a))
    print("\n" * 32)

    print("-----------------------0-Quiz taker-0-----------------------")
    score = 0
    for q, a in questions:
        ans = input(q + " ")
        if ans.strip().lower() == a.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {a}")
    print(f"Your score: {score}/{num_questions}")

def student_picker():
    print("-----------------------0-Student Picker-0-----------------------")
    students = input("Enter student names separated by commas: ")
    student_list = [s.strip() for s in students.split(",") if s.strip()]

    if not student_list:
        print("No valid student names entered.")
        return

    chosen = random.choice(student_list)
    print(f"\nThe chosen student is: {chosen}\n")

while True:
    print("\nWelcome to TMT - Teacher Manage Tasks!")
    print("1. Grade Calculator")
    print("2. Quiz Maker")
    print("3.Student Picker")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        grade_calculator()
    elif choice == '2':
        quiz_maker()
    elif choice == '3':
        student_picker()
    elif choice == '4':
        print("BYEEE!")
        break
    else:
        print("Invalid choice, try again.")
