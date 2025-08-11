import streamlit as st
import random

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="TMT - Teacher Manage Tasks",
    page_icon="TMTlogo.jpeg",
    layout="centered"
)

# --- CUSTOM CSS FOR CUTE THEME WITH BG GRADIENT AND EMOJIS ---
cute_css = """
<style>
/* Import font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
    color: #5A4E42;
    min-height: 100vh;
    margin: 0;
}

h1, h2, h3 {
    color: #A56C6C;
    text-shadow: 1px 1px 3px #FFD9D9;
}

.stTextInput input, .stTextArea textarea, .stNumberInput input {
    border-radius: 15px;
    border: 2px solid #FFB6B9;
    padding: 10px;
    box-shadow: 1px 1px 5px #FFD6D6;
    transition: border-color 0.3s ease;
    font-size: 16px;
}

.stTextInput input:focus, .stTextArea textarea:focus, .stNumberInput input:focus {
    border-color: #FF6F91;
    outline: none;
}

.stButton>button {
    background-color: #FF6F91;
    color: white;
    border-radius: 25px;
    padding: 12px 30px;
    font-weight: 700;
    font-size: 16px;
    box-shadow: 0 4px 12px rgba(255,111,145,0.5);
    transition: background-color 0.3s ease;
    cursor: pointer;
}

.stButton>button:hover {
    background-color: #FF4C69;
    box-shadow: 0 6px 16px rgba(255,76,105,0.7);
}

.css-1d391kg {
    border-radius: 15px !important;
    border: 2px solid #FFB6B9 !important;
    box-shadow: 1px 1px 5px #FFD6D6 !important;
    padding-left: 8px !important;
    font-size: 16px !important;
}

.stAlert-success {
    background-color: #D1F2EB;
    border-left: 6px solid #1ABC9C;
    color: #117A65;
    border-radius: 15px;
    padding: 10px;
    box-shadow: 1px 1px 6px #A3E4D7;
    font-weight: 600;
    font-size: 16px;
}

.stAlert-error {
    background-color: #FADBD8;
    border-left: 6px solid #E74C3C;
    color: #C0392B;
    border-radius: 15px;
    padding: 10px;
    box-shadow: 1px 1px 6px #F1948A;
    font-weight: 600;
    font-size: 16px;
}

[data-testid="stAppViewContainer"] > .main {
    max-width: 650px;
    margin: auto;
    padding: 30px 20px 50px 20px;
}

h1::before {
    content: "🌸 ";
}
h2::before {
    content: "✨ ";
}
h3::before {
    content: "🎉 ";
}

.menu-description {
    font-style: italic;
    color: #A56C6C;
    margin-bottom: 20px;
    font-size: 18px;
}
</style>
"""

st.markdown(cute_css, unsafe_allow_html=True)

# --- APP TITLE ---
st.title("📓 Teacher Manage Tasks")

# Menu selection with emoji options
menu = st.selectbox("Choose a tool:", [
    "📝 Grade Calculator", 
    "❓ Quiz Maker", 
    "🎲 Student Picker"
])

# Show description for selected menu
if menu == "📝 Grade Calculator":
    st.markdown('<div class="menu-description">Calculates your grade from a fraction (like 18/20) to a percentage and letter grade.</div>', unsafe_allow_html=True)
elif menu == "❓ Quiz Maker":
    st.markdown('<div class="menu-description">Create quizzes by entering questions and answers, then test yourself!</div>', unsafe_allow_html=True)
elif menu == "🎲 Student Picker":
    st.markdown('<div class="menu-description">Enter student names and randomly pick one — perfect for picking students to answer questions!</div>', unsafe_allow_html=True)

# --- GRADE CALCULATOR ---
if menu == "📝 Grade Calculator":
    st.header("Grade Calculator")
    score_input = st.text_input("Enter the student's score (e.g., 18/20)")

    if st.button("Calculate Grade 🎯"):
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
            st.error("⚠️ Invalid input format. Please enter like '18/20'.")

# --- QUIZ MAKER ---
elif menu == "❓ Quiz Maker":
    st.header("Quiz Maker")

    if "quiz_data" not in st.session_state:
        st.session_state.quiz_data = []
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
    if "num_questions" not in st.session_state:
        st.session_state.num_questions = 1

    if not st.session_state.quiz_started:
        # Let user select number of questions once
        st.session_state.num_questions = st.number_input("How many questions? 🤔", min_value=1, step=1)

        # Create inputs for questions and answers with unique keys and store in session_state
        questions = []
        for i in range(st.session_state.num_questions):
            q = st.text_input(f"Question {i+1} 📝", key=f"q_{i}")
            a = st.text_input(f"Answer {i+1} ✍️", key=f"a_{i}")
            questions.append((q, a))

        if st.button("Start Quiz 🚀"):
            # Check all questions and answers are filled
            if all(q.strip() and a.strip() for q, a in questions):
                st.session_state.quiz_data = questions
                st.session_state.quiz_started = True
                st.experimental_rerun()
            else:
                st.error("Please fill out all questions and answers before starting the quiz.")

    else:
        score = 0
        for idx, (q, a) in enumerate(st.session_state.quiz_data):
            ans = st.text_input(q, key=f"answer_{idx}")
            if ans.strip().lower() == a.strip().lower():
                score += 1

        st.success(f"✅ Your score: {score}/{len(st.session_state.quiz_data)}")

        if st.button("Reset Quiz 🔄"):
            st.session_state.quiz_started = False
            st.session_state.quiz_data = []
            # Clear question inputs from session_state
            for i in range(st.session_state.num_questions):
                st.session_state.pop(f"q_{i}", None)
                st.session_state.pop(f"a_{i}", None)
            st.experimental_rerun()
# --- STUDENT PICKER ---
elif menu == "🎲 Student Picker":
    st.header("Student Picker")
    names = st.text_area("Enter student names separated by commas 👫")
    if st.button("Pick Random Student 🎉"):
        student_list = [n.strip() for n in names.split(",") if n.strip()]
        if student_list:
            chosen = random.choice(student_list)
            st.success(f"🎊 The chosen student is: {chosen}")
        else:
            st.error("❌ Please enter at least one student name.")
