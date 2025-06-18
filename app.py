import streamlit as st
import time
import json
from streamlit_lottie import st_lottie
import requests

# -----------------------------------------------------------------------------
#  SETUP AND CONFIGURATION
# -----------------------------------------------------------------------------

st.set_page_config(
    page_title="A Question for My Destiny ❤️",
    page_icon="💍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- CSS for Custom Styling and Animations ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Roboto:wght@300;400&display=swap');

body {
    font-family: 'Roboto', sans-serif;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
}

/* --- Animated "Proposal" Button --- */
@keyframes pulse {
    0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 223, 186, 0.7); }
    70% { transform: scale(1.05); box-shadow: 0 0 10px 20px rgba(255, 223, 186, 0); }
    100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 223, 186, 0); }
}

.stButton>button {
    background-color: #faddff;
    color: #3d2c49;
    border: 2px solid #faddff;
    border-radius: 20px;
    padding: 15px 30px;
    font-weight: bold;
    font-size: 18px;
    transition: all 0.3s;
    animation: pulse 2.5s infinite;
}
.stButton>button:hover {
    transform: scale(1.1);
    background-color: #ffffff;
    color: #3d2c49;
}

/* --- NEW: CSS class to center the button --- */
.center-button {
    display: flex;
    justify-content: center;
}

/* --- Footer Styling --- */
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.2);
    color: #f0f2f6;
    text-align: center;
    padding: 10px;
    font-family: 'Roboto', sans-serif;
}
</style>
""", unsafe_allow_html=True)


# --- Lottie Animation Functions ---
def load_lottiefile(filepath: str):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Error: Lottie file not found at {filepath}")
        return None

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_pleading_url = "https://lottie.host/972d79a2-0955-4235-8422-999c7551e16f/hD5bV9kYv8.json"
lottie_love = load_lottiefile("assets/love_emoji.json")
lottie_pleading = load_lottieurl(lottie_pleading_url)


# -----------------------------------------------------------------------------
#  PERSONALIZE YOUR MESSAGE HERE
# -----------------------------------------------------------------------------
HER_NAME = "Wania"  # Replace with your partner's name
YOUR_NAME = "Taha"


# -----------------------------------------------------------------------------
#  THE MAIN APPLICATION LOGIC
# -----------------------------------------------------------------------------

if 'accepted' not in st.session_state:
    st.session_state.accepted = False

# --- The Main Proposal Screen ---
if not st.session_state.accepted:

    st.title("A question for my destiny... 💍")

    col1, col2 = st.columns([1, 2])
    with col1:
        if lottie_pleading:
            st_lottie(lottie_pleading, speed=1, width=200, height=200, key="pleading")
    with col2:
        st.write(f"My dear {HER_NAME},")
        st.write("From the moment I met you, my world's code was rewritten. Every line, every function now points to you. You're not just a part of my life; you are my life's entire operating system.")
        st.write("You are my destiny, and I can't imagine a single day without you.")

    st.header("My `Future.py` ❤️")
    
    code_proposal = f"""
# A program for the rest of our lives.
# Executing this is the most important command.

class OurFuture:
    def __init__(self):
        self.partner_one = "{YOUR_NAME}"
        self.partner_two = "{HER_NAME}"
        self.love = float('inf')
        self.happiness = True
        self.forever = True

    def start_life_together(self):
        # This is the only future I want to compute.
        if self.partner_two == "{HER_NAME}":
            print(f"Initializing lifetime partnership between {{self.partner_one}} and {{self.partner_two}}...")
            print("Status: Awaiting the most beautiful 'Yes' in the universe.")
            return "Will you make my life complete?"
        
# Awaiting the final, most important input.
our_life = OurFuture()
our_life.start_life_together()
    """
    st.code(code_proposal, language='python')

    st.write("") 

    # --- NEW: Using a div with our CSS class to center the button ---
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    if st.button("Will You Be Mine Forever? 💖"):
        st.session_state.accepted = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- The "YES!" Screen ---
else:
    st.balloons()
    st.title("She said Yes! 🎉")
    
    if lottie_love:
        st_lottie(lottie_love, speed=1, width=300, height=300, key="love")
    
    st.success(f"A new chapter begins... {YOUR_NAME} & {HER_NAME}, forever. ✨")
    st.header("I love you more than words can say. You've made me the happiest man in the world.")

# --- The Footer ---
footer = """
<div class="footer">
  <p>Made with ❤️ by Taha</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)