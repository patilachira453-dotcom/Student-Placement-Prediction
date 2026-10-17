🎓 PlacePro – Student Placement Prediction System

PlacePro is a web-based Student Placement Prediction and Analytics System developed using Python, Streamlit, and Machine Learning. It helps students explore placement readiness, analyze academic performance, practice aptitude questions, and receive AI-powered career guidance through an integrated chatbot.

📌 Project Overview

The Student Placement Prediction System demonstrates how machine learning and interactive data visualization can be used to explore student placement outcomes.

The application includes a student information interface, placement analytics dashboard, student dataset explorer, project information page, aptitude practice quiz, and AI chatbot powered by the Groq API.

Note: The current application uses synthetic demonstration data. Its predictions are educational estimates and do not represent actual college placement results.

✨ Features
🔐 Login System: Simple login interface with demo credentials.
📝 Student Information: Enter academic details, department, CGPA, internships, backlogs, projects, and skills.
🤖 Placement Prediction: Estimate placement outcomes using a Random Forest classification model trained on synthetic data.
📊 Analytics Dashboard: Visualize placement distribution, department-wise placement rates, CGPA distribution, and academic performance.
📁 Dataset Explorer: Browse student records, filter placement status, and download CSV files.
🧠 Aptitude Practice: Answer aptitude questions, view scores, and understand solutions.
💬 AI Chatbot: Ask questions about placements, interview preparation, technical skills, resumes, and career development using the Groq API.
🎨 Interactive Interface: Responsive layout, sidebar navigation, metrics, and interactive charts.
🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Streamlit	Web application interface
Pandas	Data manipulation and analysis
NumPy	Numerical operations and synthetic data generation
Scikit-learn	Random Forest classification and model evaluation
Plotly Express	Interactive charts and visualizations
Groq API	AI-powered chatbot responses
python-dotenv	Secure environment variable configuration
📂 Project Structure
PlacePro/
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md

app.py – Main Streamlit application.
.env – Stores the Groq API key locally.
.gitignore – Excludes sensitive and unnecessary files from version control.
requirements.txt – Lists the required Python packages.
README.md – Project documentation.
⚙️ Installation and Setup
1. Clone the repository
git clone <your-github-repository-url>
cd PlacePro


Alternatively, download the project and open its folder in VS Code.

2. Create a virtual environment (recommended)
python -m venv venv


Activate it on Windows:

venv\Scripts\activate


On macOS or Linux:

source venv/bin/activate

3. Install dependencies

Create a requirements.txt file containing:

streamlit
pandas
numpy
plotly
scikit-learn
python-dotenv
groq


Install the packages:

pip install -r requirements.txt

4. Configure the Groq API key

Create a .env file in the project root directory:

GROQ_API_KEY=your_groq_api_key_here


Replace the placeholder with your own API key obtained from the Groq Console.

Keep your API key private. Never commit the .env file to a public repository.

Add the following entries to .gitignore:

.env
venv/
__pycache__/
*.pyc

5. Run the application

Start the Streamlit application:

streamlit run app.py


Open the local URL displayed in your terminal, usually:

http://localhost:8501

🔑 Demo Login Credentials

The application currently uses hardcoded demonstration credentials.

Field	Value
Username	student
Password	student123

Security note: These credentials are for demonstration purposes only. Replace the hardcoded login with a secure authentication system before deploying the application for real users.

🤖 Machine Learning Model

PlacePro uses a Random Forest Classifier from Scikit-learn to estimate student placement outcomes.

Input features
CGPA: Academic performance on a 10-point scale.
Aptitude: Aptitude score.
Communication: Communication skill rating.
Internship: Internship experience indicator.
Model workflow
Generate synthetic student data.
Select the input features and placement labels.
Split the data into training and testing sets.
Train the Random Forest classification model.
Evaluate the model using accuracy.
Use the trained model to estimate placement outcomes.

The application generates 600 synthetic student records for demonstration purposes. The model's reported accuracy measures performance on a held-out portion of that synthetic dataset; it should not be interpreted as real-world placement accuracy.

📊 Dashboard Modules
1. Student Information

Collects student profile details, academic scores, skills, internships, projects, and backlogs.

2. Placement Analytics Dashboard

Displays:

Total student records.
Number of placed students.
Overall placement rate.
Average package among synthetic placed records.
Placement distribution.
Department-wise placement rates.
CGPA distribution.
CGPA and aptitude relationships.
3. Student Dataset Explorer

Allows users to filter student records by placement status, inspect data in a table, and download the displayed records as a CSV file.

4. Aptitude Practice

Provides multiple-choice aptitude questions, automatic scoring, correct answers, and explanations.

5. AI Chatbot

Uses the Groq API to provide conversational guidance on:

Placement preparation.
Resume building.
Technical interviews.
Aptitude and reasoning.
Project suggestions.
Communication skills.
Career development.

The chatbot requires a valid API key, internet connectivity, and an available Groq model.

🔮 Future Enhancements
Integrate verified historical placement data.
Implement secure student and administrator authentication.
Improve model evaluation using real-world test data.
Add salary package prediction.
Expand the aptitude question bank.
Provide personalized student improvement recommendations.
Add downloadable PDF placement reports.
Deploy the application to a cloud hosting platform.
Add database integration to store student profiles and results.
⚠️ Limitations
The dataset is synthetic and does not represent actual student records.
The Random Forest model is intended for educational demonstration.
Model accuracy on synthetic data does not establish real-world predictive reliability.
The login system uses hardcoded demo credentials.
The AI chatbot's responses depend on the configured Groq model and API availability.
Placement predictions must not be used as guarantees of employment or as the sole basis for consequential decisions.
👩‍💻 Project Information
Project Title: Student Placement Prediction System
Application Name: PlacePro
Domain: Machine Learning and Data Analytics
Programming Language: Python
Frontend: Streamlit
Machine Learning Algorithm: Random Forest Classifier
Visualization: Plotly
AI Integration: Groq API
📜 License

This project is intended for educational and academic demonstration purposes. Add an appropriate open-source license if you plan to distribute it publicly.

PlacePro – Empowering Students Through Placement Analytics and AI Career Guidance.
