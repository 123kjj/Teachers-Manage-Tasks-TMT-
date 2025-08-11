import streamlit as st
import random
import base64

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="TMT - Teacher Manage Tasks",
    page_icon="TMTlogo.jpeg",
    layout="centered"
)

# --- FUNCTION TO SET BG IMAGE ---
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    css = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)),
                    url(data:image/jpeg;base64,{encoded});
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');
    html, body, [class*="css"] {{
        font-family: 'Poppins', sans-serif;
    }}

    /* Titles */
    h1, h2, h3 {{
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8);
    }}

    /* Inputs & Buttons */
    .stTextInput input, .stTextArea textarea, .stNumberInput input {{
        border-radius: 10px;
        border: 1px solid #a3c2c2;
        padding: 8px;
    }}

    .stButton>button {{
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
        border: none;
        font-weight: bold;
    }}
    .stButton>button:hover {{
        background-color: #45a049;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call function to set bg
set_bg("Background.jpeg")

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
            st.rerun()

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
