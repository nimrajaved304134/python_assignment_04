import streamlit as st
from datetime import datetime
import random

# Configure page
st.set_page_config(
    page_title="Python Quiz",
    page_icon="🐍",
    layout="centered"
)

# Quiz questions and answers
questions = [
    {
        "question": "How do you create a list in Python?",
        "options": ["list()", "[]", "array()", "{}", "()"],
        "answer": "[]"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["def", "function", "define", "func", "fn"],
        "answer": "def"
    },
    {
        "question": "What does the 'len()' function do?",
        "options": [
            "Returns the length of an object",
            "Converts to lowercase",
            "Prints to console",
            "Creates a new list",
            "Sorts a list"
        ],
        "answer": "Returns the length of an object"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["^", "**", "*", "//", "%%"],
        "answer": "**"
    },
    {
        "question": "What is the output of 'print(3 * 'hi')'?",
        "options": ["hihihi", "3hi", "Error", "hi hi hi", "hihihihi"],
        "answer": "hihihi"
    }
]

def prepare_question(question_data):
    """Randomly select 4 options including the correct answer"""
    correct = question_data["answer"]
    incorrect = [opt for opt in question_data["options"] if opt != correct]
    
    # Select 3 random incorrect options
    selected_incorrect = random.sample(incorrect, min(3, len(incorrect)))
    
    # Combine with correct answer
    options = selected_incorrect + [correct]
    
    # Shuffle the options
    random.shuffle(options)
    
    return {
        "question": question_data["question"],
        "options": options,
        "answer": correct
    }

# Initialize session state for quiz
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_completed = False
    st.session_state.user_answers = []
    st.session_state.prepared_questions = [prepare_question(q) for q in questions]

# Display header
st.title("🐍 Python Knowledge Quiz")
st.write("Test your Python knowledge with this interactive quiz!")

# Quiz progress
progress = st.progress((st.session_state.current_question) / len(questions))

# Display current question
def display_question():
    q = st.session_state.prepared_questions[st.session_state.current_question]
    st.subheader(f"Question {st.session_state.current_question + 1}")
    st.write(q["question"])
    
    # Display options as buttons
    selected_option = st.radio(
        "Select your answer:",
        q["options"],
        key=f"q{st.session_state.current_question}"
    )
    
    # Submit button
    if st.button("Submit"):
        check_answer(selected_option)

# Check answer and update state
def check_answer(selected_option):
    q = st.session_state.prepared_questions[st.session_state.current_question]
    st.session_state.user_answers.append({
        "question": q["question"],
        "user_answer": selected_option,
        "correct_answer": q["answer"],
        "is_correct": selected_option == q["answer"]
    })
    
    if selected_option == q["answer"]:
        st.session_state.score += 1
    
    # Move to next question or end quiz
    if st.session_state.current_question < len(questions) - 1:
        st.session_state.current_question += 1
    else:
        st.session_state.quiz_completed = True
    st.rerun()

# Display results
def display_results():
    st.balloons()
    st.subheader("🎉 Quiz Completed!")
    st.write(f"Your score: {st.session_state.score}/{len(questions)}")
    
    st.write("### Detailed Results:")
    for i, result in enumerate(st.session_state.user_answers):
        st.write(f"**Question {i+1}:** {result['question']}")
        if result["is_correct"]:
            st.success(f"✅ Your answer: {result['user_answer']} (Correct)")
        else:
            st.error(f"❌ Your answer: {result['user_answer']}")
            st.info(f"Correct answer: {result['correct_answer']}")
        st.write("---")
    
    # Restart quiz button
    if st.button("🔄 Take Quiz Again"):
        reset_quiz()

# Reset quiz state
def reset_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_completed = False
    st.session_state.user_answers = []
    st.session_state.prepared_questions = [prepare_question(q) for q in questions]
    st.rerun()

# Main app logic
if st.session_state.quiz_completed:
    display_results()
else:
    display_question()
    progress.progress((st.session_state.current_question + 1) / len(questions))

# Sidebar info
st.sidebar.header("About")
st.sidebar.write("This quiz tests basic Python knowledge.")
st.sidebar.write(f"Total questions: {len(questions)}")
st.sidebar.write(f"Current score: {st.session_state.score}")
st.sidebar.write(f"© {datetime.now().year} Python Quiz App")