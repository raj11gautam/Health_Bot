# Health_Bot
# 🤖 HealthBot - Smart Symptom Checker using Machine Learning 🩺

HealthBot is a user-friendly medical assistant app built using **Streamlit** and **Machine Learning**.  
It helps users predict possible diseases based on symptoms, gives information like causes, description, precautions, health tips, and can even talk back!

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

