import os
from datetime import date

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
# ==============================
# TEST GROQ API KEY
# ==============================
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if api_key:
    st.success("Groq API key loaded successfully.")
else:
    st.error("GROQ_API_KEY not found. Check your .env file.")

st.set_page_config(
    page_title="Student Placement Prediction",
    page_icon="🎓",
    layout="wide"
)
# ==============================
# LOGIN PAGE
# ==============================
import streamlit as st

# Demo credentials
USERNAME = "student"
PASSWORD = "student123"

# Initialize login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login UI
if not st.session_state.logged_in:

    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #dbeafe, #eef2ff);
    }
    .login-title {
        text-align: center;
        color: #1e3a8a;
        font-size: 32px;
        font-weight: bold;
    }
    .login-subtitle {
        text-align: center;
        color: #475569;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="login-title">🎓 PlacePro</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="login-subtitle">'
        'Student Placement Analytics System'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    _, login_col, _ = st.columns([1, 1.5, 1])

    with login_col:
        st.subheader("🔐 Login to Your Account")

        with st.form("login_form"):
            username = st.text_input(
                "Username",
                placeholder="Enter your username"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            login_button = st.form_submit_button(
                "Login",
                use_container_width=True
            )

        if login_button:
            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid username or password!")

        st.caption("Demo username: student")
        st.caption("Demo password: student123")

    st.stop()

# ==============================
# LOGOUT BUTTON
# ==============================
with st.sidebar:
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

# Your existing sidebar navigation and
# Student Placement Dashboard code continues below.
# Custom styling using Streamlit's built-in Markdown
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f7fc;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("🎓 Student Placement Prediction System")
st.write(
    "Welcome! Enter your academic details and skills "
    "to estimate your placement eligibility."
)

st.divider()

# Student details section
st.header("📝 Student Information")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Student Name")
    age = st.number_input(
        "Age", min_value=18, max_value=35, value=21
    )
    gender = st.selectbox(
        "Gender",
        ["Select", "Male", "Female", "Other"]
    )
    degree = st.selectbox(
        "Degree",
        ["B.Tech", "B.E.", "BCA", "MCA", "B.Sc", "M.Tech"]
    )

with col2:
    branch = st.selectbox(
        "Department",
        [
            "Computer Science",
            "Information Technology",
            "Electronics",
            "Mechanical",
            "Civil",
            "Electrical"
        ]
    )
    cgpa = st.slider(
        "CGPA", min_value=0.0, max_value=10.0,
        value=7.0, step=0.1
    )
    internships = st.number_input(
        "Number of Internships",
        min_value=0, max_value=10, value=1
    )
    backlogs = st.number_input(
        "Number of Active Backlogs",
        min_value=0, max_value=20, value=0
    )

st.divider()

# Skills section
st.header("💻 Skills and Aptitude")

col3, col4 = st.columns(2)

with col3:
    aptitude = st.slider(
        "Aptitude Score (%)",
        min_value=0, max_value=100, value=70
    )
    communication = st.slider(
        "Communication Skills (%)",
        min_value=0, max_value=100, value=70
    )

with col4:
    technical = st.slider(
        "Technical Skills (%)",
        min_value=0, max_value=100, value=75
    )
    projects = st.number_input(
        "Number of Projects",
        min_value=0, max_value=20, value=2
    )

st.divider()

# Prediction section
st.header("🚀 Placement Prediction")

if st.button("Predict Placement", type="primary",
             use_container_width=True):

    if not name.strip():
        st.warning("Please enter the student's name.")

    elif gender == "Select":
        st.warning("Please select a gender.")

    else:
        # Illustrative rule-based prediction only.
        # Replace with a trained ML model for real predictions.
        score = (
            cgpa * 5
            + aptitude * 0.15
            + communication * 0.10
            + technical * 0.15
            + min(internships, 3) * 2
            + min(projects, 5)
            - backlogs * 5
        )

        st.subheader(f"Prediction Result for {name}")

        if score >= 75 and backlogs == 0:
            st.success("✅ Likely to be placed")
            st.write(
                "Your profile meets the illustrative "
                "placement criteria."
            )
        else:
            st.info("📘 Placement readiness needs improvement")
            st.write(
                "Focus on academic performance, technical "
                "skills, aptitude, and interview preparation."
            )

        st.caption(
            "Demo result only. This is a rule-based example, "
            "not a trained machine-learning prediction."
        )

st.divider()

st.caption("Student Placement Prediction System | Academic Project")

st.set_page_config(
    page_title="PlacePro - Student Placement",
    page_icon="🎓",
    layout="wide"
)

# CSS - Text and background colors
st.markdown("""
<style>
.stApp {
    background-color: #f4f7fc;
    color: #1e293b;
}
h1, h2, h3, h4, h5, h6 {
    color: #172554 !important;
}
p, li, label, [data-testid="stMarkdownContainer"] {
    color: #263449 !important;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827, #243b55);
}
[data-testid="stSidebar"] * {
    color: white !important;
}
.metric-card {
    background: white;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #dce5f1;
    margin-bottom: 10px;
}
.metric-label {
    color: #52647a !important;
    font-size: 14px;
}
.metric-value {
    color: #1d4ed8 !important;
    font-size: 28px;
    font-weight: bold;
}
.stButton > button, .stFormSubmitButton > button {
    background-color: #4338ca;
    color: white !important;
    border-radius: 8px;
}
[data-testid="stExpander"] {
    background-color: white;
}
</style>
""", unsafe_allow_html=True)


# Generate sample dataset
@st.cache_data
def create_dataset():
    rng = np.random.default_rng(42)
    n = 600

    cgpa = rng.uniform(4, 10, n).round(2)
    aptitude = rng.integers(25, 101, n)
    communication = rng.integers(2, 11, n)
    internship = rng.integers(0, 2, n)

    departments = rng.choice(
        ["CSE", "ISE", "ECE", "EEE", "Mechanical"], n
    )

    score = (
        (cgpa - 5) * 0.75
        + (aptitude - 40) * 0.025
        + (communication - 4) * 0.20
        + internship * 0.65
        + rng.normal(0, 0.9, n)
    )

    placement = (score > 2.45).astype(int)

    package = np.where(
        placement == 1,
        rng.uniform(3, 12, n)
        + np.maximum(cgpa - 8, 0) * 1.5,
        0
    ).round(2)

    return pd.DataFrame({
        "CGPA": cgpa,
        "Aptitude": aptitude,
        "Communication": communication,
        "Internship": internship,
        "Department": departments,
        "Placement": placement,
        "Package_LPA": package
    })


df = create_dataset()

FEATURES = [
    "CGPA", "Aptitude", "Communication", "Internship"
]


# Train machine learning model
@st.cache_resource
def train_model():
    data = create_dataset()
    X = data[FEATURES]
    y = data["Placement"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=150,
        max_depth=8,
        random_state=42,
        class_weight="balanced"
    )

    model.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(X_test))

    return model, accuracy


model, accuracy = train_model()


# Metric card
def metric_card(label, value, note):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-label">{note}</div>
    </div>
    """, unsafe_allow_html=True)
    


# Sidebar navigation

# ---------------- SIDEBAR NAVIGATION ----------------
with st.sidebar:

    st.title("🎓 PlacePro")
    st.caption("STUDENT PLACEMENT ANALYTICS")

    st.divider()

    page = st.radio(
        "📌 MAIN NAVIGATION",
        [
            "📝 Student Information",
            "📊 Dashboard",
            "📁 Student Dataset",
            "ℹ️ About Project",
            "Aptitude Practice",
             "🤖 AI Chatbot"   
        ],
        key="main_navigation"
    )

    st.divider()

    st.markdown("### 🤖 Model Information")
    st.write("Algorithm: Random Forest")
    st.write("Features: 4")
    st.write("Framework: Streamlit")

    st.divider()

    st.markdown("### 📌 Quick Stats")
    st.metric("Total Students", len(df))
    st.metric(
        "Placed Students",
        int(df["Placement"].sum())
    )

    st.divider()

    st.caption("Developed using Python & Machine Learning")

# DASHBOARD PAGE
if page == "📊 Dashboard":
    st.title("📊 Placement Analytics Dashboard")
    st.write("Student performance and placement overview.")

    total = len(df)
    placed = int(df["Placement"].sum())
    not_placed = total - placed
    rate = placed / total * 100

    avg_package = df.loc[
        df["Placement"] == 1, "Package_LPA"
    ].mean()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("Total Students", total, "Demo records")
    with c2:
        metric_card("Placed Students", placed, "Sample data")
    with c3:
        metric_card("Placement Rate", f"{rate:.1f}%", "Demo rate")
    with c4:
        metric_card(
            "Average Package",
            f"{avg_package:.2f} LPA",
            "Placed demo records"
        )

    st.subheader("Placement Overview")
    left, right = st.columns(2)

    with left:
        counts = pd.DataFrame({
            "Status": ["Placed", "Not Placed"],
            "Students": [placed, not_placed]
        })

        fig = px.pie(
            counts,
            names="Status",
            values="Students",
            hole=0.6,
            color="Status",
            color_discrete_map={
                "Placed": "#4f46e5",
                "Not Placed": "#f59e0b"
            },
            title="Placement Distribution"
        )
        fig.update_layout(
            paper_bgcolor="white",
            font_color="#172554"
        )
        st.plotly_chart(fig, use_container_width=True)

    with right:
        dept = (
            df.groupby("Department")["Placement"]
            .mean().mul(100)
            .reset_index(name="Placement Rate")
        )

        fig = px.bar(
            dept,
            x="Department",
            y="Placement Rate",
            color="Placement Rate",
            text_auto=".1f",
            color_continuous_scale="Blues",
            title="Placement by Department"
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            font_color="#172554",
            coloraxis_showscale=False
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Academic Performance")
    left, right = st.columns(2)

    with left:
        fig = px.histogram(
            df, x="CGPA", color="Placement",
            nbins=20, barmode="overlay",
            title="CGPA Distribution",
            color_discrete_map={
                0: "#f59e0b", 1: "#4f46e5"
            }
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            font_color="#172554"
        )
        st.plotly_chart(fig, use_container_width=True)

    with right:
        fig = px.scatter(
            df, x="CGPA", y="Aptitude",
            color="Placement", size="Communication",
            hover_data=["Department", "Internship"],
            title="CGPA vs Aptitude",
            color_discrete_map={
                0: "#f59e0b", 1: "#4f46e5"
            }
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            font_color="#172554"
        )
        st.plotly_chart(fig, width="stretch")

    st.info("Charts use synthetic demo data, not actual college results.")
    
    # DATASET PAGE
elif page == "📁 Student Dataset":
    st.title("📁 Student Dataset Explorer")
    st.write("View and download student demo records.")

    status = st.selectbox(
        "Filter Placement Status",
        ["All", "Placed", "Not Placed"]
    )

    filtered = df.copy()

    if status == "Placed":
        filtered = filtered[filtered["Placement"] == 1]
    elif status == "Not Placed":
        filtered = filtered[filtered["Placement"] == 0]

    display_df = filtered.copy()

    display_df["Placement"] = display_df["Placement"].map({
        1: "Placed", 0: "Not Placed"
    })
    display_df["Internship"] = display_df["Internship"].map({
        1: "Yes", 0: "No"
    })

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    csv = display_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download CSV",
        data=csv,
        file_name="student_placement_demo.csv",
        mime="text/csv"
    )


# ABOUT PROJECT PAGE
elif page == "ℹ️ About Project":
    st.title("🎓 About Our Project")
    st.subheader("Student Placement Prediction using Machine Learning")

    st.divider()

    st.header("📌 Project Overview")
    st.write("""
    The Student Placement Prediction System is a machine learning
    web application developed using Python and Streamlit.

    It predicts whether a student is likely to get placed based on
    academic performance and skill-related information.
    Interactive charts help users explore student placement data.
    """)

    st.header("🎯 Project Objectives")
    st.markdown("""
    - Predict student placement outcomes.
    - Analyze academic performance.
    - Understand aptitude and communication skills.
    - Display placement statistics through interactive charts.
    - Provide a simple, user-friendly dashboard.
    """)

    st.header("🛠️ Technologies Used")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.info("🐍 Python\n\nProgramming Language")
    with c2:
        st.info("🤖 Scikit-learn\n\nMachine Learning")
    with c3:
        st.info("📊 Streamlit + Plotly\n\nDashboard and Charts")

    st.header("📥 Input Features")
    st.markdown("""
    - **CGPA:** Student academic performance.
    - **Aptitude Score:** Problem-solving and reasoning score.
    - **Communication Skills:** Communication skill rating.
    - **Internship Experience:** Previous internship experience.
    """)

    st.header("⚙️ Project Modules")

    with st.expander("1. Dashboard Module"):
        st.write(
            "Displays placement statistics, department comparisons "
            "and academic performance charts."
        )

    with st.expander("2. Prediction Module"):
        st.write(
            "Uses a Random Forest Classifier to predict a student's "
            "placement outcome from the entered details."
        )

    with st.expander("3. Dataset Explorer Module"):
        st.write(
            "Displays student records, filters placement status "
            "and allows CSV downloads."
        )

    st.header("🌟 Advantages")
    st.markdown("""
    - Easy-to-use interface.
    - Fast model predictions.
    - Interactive data visualization.
    - Demonstrates machine learning concepts.
    """)

    st.header("🚀 Future Enhancements")
    st.markdown("""
    - Integrate real college placement data.
    - Add student and administrator login.
    - Add salary package prediction.
    - Generate downloadable reports.
    - Evaluate the model with real-world test data.
    """)

    st.header("👩‍💻 Project Information")
    st.write("**Project Title:** Student Placement Prediction")
    st.write("**Domain:** Machine Learning")
    st.write("**Algorithm:** Random Forest Classifier")
    st.write("**Frontend:** Streamlit")
    st.write("**Programming Language:** Python")

    st.success("About Project page loaded successfully!")

    st.caption(
        "This project uses synthetic demonstration data. "
        "Predictions are not actual placement outcomes."
    )

# ---------- APTITUDE PRACTICE ----------

elif page == "Aptitude Practice":

    st.title("🧠 Aptitude Practice Quiz")

    questions = [
        {
            "q": "A number increases from 80 to 100. What is the percentage increase?",
            "options": ["20%", "25%", "30%", "15%"],
            "answer": "25%",
            "explain": "Increase is 20. Therefore, 20 / 80 × 100 = 25%."
        },
        {
            "q": "Find the next number: 3, 6, 12, 24, ...",
            "options": ["36", "42", "48", "30"],
            "answer": "48",
            "explain": "Each number is multiplied by 2."
        },
        {
            "q": "Five workers finish a task in 12 days. How many worker-days?",
            "options": ["17", "60", "30", "7"],
            "answer": "60",
            "explain": "5 workers × 12 days = 60 worker-days."
        }
    ]

    answers = {}

    with st.form("aptitude_quiz"):

        for i, question in enumerate(questions):
            answers[i] = st.radio(
                question["q"],
                question["options"],
                key=f"question_{i}"
            )

        submitted = st.form_submit_button("Submit Answers")

    if submitted:

        score = sum(
            answers[i] == q["answer"]
            for i, q in enumerate(questions)
        )

        st.metric("Your Score", f"{score}/{len(questions)}")

        for i, question in enumerate(questions):
            st.write(
                f"Question {i+1}: Correct answer: "
                f"{question['answer']}. {question['explain']}"
            )

# ==============================
# AI CHATBOT PAGE
# ==============================

elif page == "🤖 AI Chatbot":

    st.title("🤖 PlacePro AI Assistant")
    st.write(
        "Ask questions about placements, interview preparation, "
        "aptitude, CGPA, technical skills, and career guidance."
    )

    st.divider()

    # Load Groq API key
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        st.error(
            "Groq API key not found. Please add GROQ_API_KEY "
            "to your .env file and restart the application."
        )
        st.stop()

    # Create Groq client
    client = Groq(api_key=api_key)

    # Initialize chat history
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {
                "role": "assistant",
                "content": (
                    "Hello! 👋 Welcome to PlacePro AI Assistant.\n\n"
                    "I can help you with:\n"
                    "- Student placement preparation\n"
                    "- Resume and interview tips\n"
                    "- Aptitude practice\n"
                    "- Technical skills and projects\n"
                    "- CGPA and placement readiness\n\n"
                    "How can I help you today?"
                )
            }
        ]

    # Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_messages = [
            {
                "role": "assistant",
                "content": (
                    "Hello! 👋 I'm your PlacePro AI Assistant. "
                    "What would you like to learn today?"
                )
            }
        ]
        st.rerun()

    # Display previous messages
    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    user_prompt = st.chat_input(
        "Ask me about placements, aptitude, or interviews..."
    )

    if user_prompt:
        # Display and store the user's message
        st.session_state.chat_messages.append(
            {
                "role": "user",
                "content": user_prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(user_prompt)

        # Generate the AI response
        with st.chat_message("assistant"):
            with st.spinner("PlacePro AI is thinking..."):
                try:
                    system_prompt = """
                    You are PlacePro AI Assistant, a helpful career
                    and placement guidance chatbot for college students.

                    Your responsibilities:
                    1. Explain student placement preparation.
                    2. Give resume-building and interview tips.
                    3. Help students practice aptitude questions.
                    4. Recommend technical skills and projects.
                    5. Explain CGPA, internships, and placement readiness.
                    6. Provide professional communication advice.
                    7. Give clear, friendly, actionable answers.

                    Use simple English and organized bullet points.
                    For aptitude questions, explain the solution step
                    by step.

                    Do not claim to know actual placement results,
                    college statistics, or student records unless
                    reliable data is explicitly provided.

                    The application uses synthetic demonstration data.
                    Never present its model predictions as guarantees
                    of actual employment or salary.
                    """

                    # Send recent conversation history to Groq
                    messages = [
                        {
                            "role": "system",
                            "content": system_prompt
                        }
                    ] + st.session_state.chat_messages[-12:]

                    response = client.chat.completions.create(
                        model="openai/gpt-oss-120b",
                        messages=messages,
                        temperature=0.5,
                        max_completion_tokens=1024
                    )

                    answer = response.choices[0].message.content

                    if not answer:
                        answer = "Sorry, I couldn't generate a response."

                    st.markdown(answer)

                    # Save the assistant's reply
                    st.session_state.chat_messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )

                except Exception as e:
                    st.error(
                        "Unable to get a response from the AI service. "
                        "Please check your API key, internet connection, "
                        "and Groq model availability."
                    )
                    st.caption(f"Error details: {e}")            