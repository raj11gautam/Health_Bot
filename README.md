# Health_Bot
# 🤖 HealthBot - Smart Symptom Checker using Machine Learning 🩺

Project Overview: HealthBot - Symptom Checker and Health Assistant
HealthBot is an AI-powered chatbot designed to help users identify potential diseases based on symptoms they input. It also offers additional features like providing disease descriptions, causes, precautions, health tips, text-to-speech functionality, and hospital information. The project is built using Streamlit for the user interface and scikit-learn for disease prediction.

Key Features:
1. Disease Prediction: Based on user-entered symptoms, the bot predicts possible diseases and displays the probability of the diagnosis.
2. Disease Information: Provides descriptions, causes, and precautions for each predicted disease.
3. Text-to-Speech: Uses pyttsx3 to speak the diagnosis and recommendations aloud.
4. Downloadable Report: Users can download a detailed PDF report containing their symptoms, predicted disease, and treatment advice.
5. Random Health Tip: A health tip is displayed every time the user interacts with the bot.
6. Hospital Information: Offers information on nearby hospitals or clinics.
7. History Tracking: Tracks and displays the user's past interactions, with the ability to clear history.
8. Emoji-based Display: Uses emojis to visually represent diseases for a fun and engaging experience.
9. Minimal Dark Theme: The interface uses a minimal dark theme for better user experience.

Technologies Used:
1. Streamlit: For building the web interface.
2. scikit-learn: For the disease prediction model.
3. pyttsx3: For text-to-speech functionality.
4. pandas: For handling the symptom and disease dataset.
5. pickle: For loading the pre-trained machine learning model.
6. geopy: For hospital location features.

How it Works:
1. Input Symptoms: Users enter their symptoms.
2. Disease Prediction: The bot predicts the most likely disease based on the symptoms.
3. Information Display: The bot provides detailed information about the disease (description, causes, precautions).
4. Text-to-Speech: The bot speaks the information out loud.
5. Other Features: Users can download a report, get health tips, or find nearby hospitals.

---

## 🚀 Features

✅ Disease prediction using ML  
✅ Probability-based predictions  
✅ Description, causes, and precautions of diseases  
✅ Chatbot to talk with users  
✅ Text-to-Speech (TTS) – HealthBot speaks!  
✅ Random health tips for awareness  
✅ Google Maps Hospital Search  
✅ Downloadable PDF report  
✅ Emoji-based disease display  
✅ Dark mode inspired styling  
✅ History tracking & Clear Chat option

---

## 🧠 Tech Stack

- **Python 3.9+**
- **Streamlit**
- **Pandas**
- **Scikit-learn (for ML Model)**
- **pyttsx3** (for TTS)
- **Pickle** (for model loading)
- **HTML/CSS** for custom styling

---

## Project Structure
HealthBot/
│
├── app.py                # Main application file
├── model.pkl             # Trained ML model
├── data/
│   └── symptoms.csv      # Symptom input data
├── requirements.txt      # Python packages
└── README.md             # You're reading it 😉


## ⚙️ How to Run

1. Clone the repo or download ZIP  
2. Install dependencies:

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

