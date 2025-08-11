import streamlit as st
import random

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="TMT - Teacher Manage Tasks",
    page_icon="TMTlogo.jpeg",
    layout="centered"
)

# --- CUSTOM CSS FOR CUTE THEME ---
cute_css = """
<style>
/* Import font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background-color: #FFF8F0;
    color: #5A4E42;
}

/* Title */
h1, h2, h3 {
    color: #A56C6C;
    text-shadow: 1px 1px 3px #FFD9D9;
}

/* Inputs & TextAreas */
.stTextInput input, .stTextArea textarea, .stNumberInput input {
    border-radius: 15px;
    border: 2px solid #FFB6B9;
    padding: 10px;
    box-shadow: 1px 1px 5px #FFD6D6;
    transition: border-color 0.3s ease;
}

.stTextInput input:focus, .stTextArea textarea:focus, .stNumberInput input:focus {
    border-color: #FF6F91;
    outline: none;
}

/* Buttons */
.stButton>button {
    background-color: #FF6F91;
    color: white;
    border-radius: 20px;
    padding: 10px 25px;
    font-weight: 600;
    box-shadow: 0 4px 8px rgba(255,111,145,0.4);
    transition: background-color 0.3s ease;
}

.stButton>button:hover {
    background-color: #FF4C69;
    box-shadow: 0 6px 12px rgba(255,76,105,0.6);
}

/* Selectbox */
.css-1d391kg {
    border-radius: 15px !important;
    border: 2px solid #FFB6B9 !important;
    box-shadow: 1px 1px 5px #FFD6D6 !important;
    padding-left: 8px !important;
}

/* Success and error messages */
.stAlert-success {
    background-color: #D1F2EB;
    border-left: 6px solid #1ABC9C;
    color: #117A65;
    border-radius: 15px;
    padding: 10px;
    box-shadow: 1px 1px 6px #A3E4D7;
}

.stAlert-error {
    background-color: #FADBD8;
    border-left: 6px solid #E74C3C;
    color: #C0392B;
    border-radius: 15px;
    padding: 10px;
    box-shadow: 1px 1px 6px #F1948A;
}
</style>
"""

st.markdown(cute_css, unsafe_allow_html=True)

# --- APP TITLE ---
st.title("📓 Teacher Manage Tasks")

# Menu selection
menu = st.selectbox("Choose a tool:", ["Grade Calculator", "Quiz Maker", "Student Picker"])

# --- GRADE CALCULATOR ---
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

            st.success(f"📊 Percentage: {percentage:.2f}%\n🏆 Letter Grade: {letter}")
        except:
            st.error("Invalid input format. Please enter like '18/20'.")

# --- QUIZ MAKER ---
elif menu == "Quiz Maker":
    st.header("Quiz Maker")

    if "quiz_data" not in st.session_state:
        st.session_state.quiz_data = []
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False

    if not st.session_state.quiz_started:
        num_questions = st.number_input("How many questions?", min_value=1, step=1)
        questions = []

        for i in range(num_questions):
            q = st.text_input(f"Question {i+1}")
            a = st.text_input(f"Answer {i+1}")
            questions.append((q, a))

        if st.button("Start Quiz"):
            st.session_state.quiz_data = questions
            st.session_state.quiz_started = True
            st.experimental_rerun()

    else:
        score = 0
        for idx, (q, a) in enumerate(st.session_state.quiz_data):
            ans = st.text_input(q, key=f"answer_{idx}")
            if ans.strip().lower() == a.strip().lower():
                score += 1

        st.success(f"✅ Your score: {score}/{len(st.session_state.quiz_data)}")

# --- STUDENT PICKER ---
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
