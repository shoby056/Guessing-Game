import streamlit as st
import random

# Custom CSS for background styling
st.markdown(
    """
    <style>
    body {
        background-color:#fff;
        color: white;
        font-family: Arial, sans-serif;
    }
    .stApp {
      background: linear-gradient(135deg, #11998E, #38EF7D);

;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
    }
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Session state me secret number store karne ke liye
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 10)
    st.session_state.message = ""
    st.session_state.attempts = 0

st.markdown("<h1 class='title'>🎮 Guess the Number Game 🎲</h1>", unsafe_allow_html=True)
st.subheader("Can you guess the secret number? 🔢")
st.write("The game has started! Guess any number between 1 and 10 and try to win! 🎯")

# User input
guess = st.number_input("Enter your Guess number:", min_value=1, max_value=10, step=1)

if st.button("🔍 Check Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.secret_number:
        st.session_state.message = f"📉 Too low! Try again. (Attempts: {st.session_state.attempts})"
    elif guess > st.session_state.secret_number:
        st.session_state.message = f"📈 Too high! Try again. (Attempts: {st.session_state.attempts})"
    else:
        st.session_state.message = f"🎉 Congratulations! You guessed the correct number in {st.session_state.attempts} attempts! 🎊"
        st.session_state.secret_number = random.randint(1, 10)  # Naya number generate karna taake game continue ho
        st.session_state.attempts = 0  # Attempts reset karein

# Game UI enhancements
st.write("\n")
st.write(st.session_state.message)

st.button("🔄 Restart Game", on_click=lambda: (setattr(st.session_state, 'secret_number', random.randint(1, 10)), setattr(st.session_state, 'attempts', 0), setattr(st.session_state, 'message', "")))
