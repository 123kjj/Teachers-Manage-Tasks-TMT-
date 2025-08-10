import streamlit as st
import random

st.set_page_config(page_icon="favicon_32x32.png")
st.set_page_config(
    page_icon="TMTlogo.jpeg"
) 
st.set_page_config(page_title="TMT - Teacher Manage Tasks", layout="centered")

# Title
st.title("👩‍🏫 Teacher Manage Tasks")

# Menu selection
menu = st.selectbox("Choose a tool:", ["Grade Calculator", "Quiz Maker", "Student Picker"])

# Grade Calculator
if menu == "Grade Calculator":
    st.header("Grade Calculator")
    score_input = st.text_input("Enter the student's score (e.g., 18/20)")

    if st.button("Calculate Grade"):
        try:
            num, den = score_input.split('/')
            num = int(num)
            den = int(den)
            percentage = (num / den) * 100

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

            st.success(f"Percentage: {percentage:.2f}%\nLetter Grade: {letter}")
        except:
            st.error("Invalid input format. Please enter like '18/20'.")

# Quiz Maker
elif menu == "Quiz Maker":
    st.header("Quiz Maker")
    num_questions = st.number_input("How many questions?", min_value=1, step=1)
    questions = []

    for i in range(num_questions):
        q = st.text_input(f"Question {i+1}")
        a = st.text_input(f"Answer {i+1}")
        questions.append((q, a))

    if st.button("Start Quiz"):
        score = 0
        for q, a in questions:
            ans = st.text_input(q, key=q)
            if ans.strip().lower() == a.strip().lower():
                score += 1
        st.write(f"Your score: {score}/{num_questions}")

# Student Picker
elif menu == "Student Picker":
    st.header("Student Picker")
    names = st.text_area("Enter student names separated by commas")
    if st.button("Pick Random Student"):
        student_list = [n.strip() for n in names.split(",") if n.strip()]
        if student_list:
            chosen = random.choice(student_list)
            st.success(f"🎉 The chosen student is: {chosen}")
        else:
            st.error("Please enter at least one student name.")
