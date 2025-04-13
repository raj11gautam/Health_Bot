import streamlit as st
import pandas as pd
import pickle
import pyttsx3
import threading
import random
import json

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load symptom data from CSV
symptom_data = pd.read_csv('data/symptoms.csv')

# Streamlit page configuration
st.set_page_config(page_title="HealthBot 🩺", layout="centered")

# Sidebar for history buttons
history_button = st.sidebar.button("View History")
clear_history_button = st.sidebar.button("Clear History")

# Interface Title and Introduction
st.title("🤖 HealthBot - Symptom Checker")
st.write("Enter your symptoms below:")

# List of symptom columns
symptoms_columns = ['Fever', 'Cough', 'Fatigue', 'Headache', 'Sore Throat', 'Muscle Aches', 'Loss of Appetite', 
                    'Nausea', 'Vomiting', 'Diarrhea', 'Shortness of Breath', 'Rashes', 'Dizziness', 
                    'Sweating', 'Sleep Disturbances', 'Weight Loss']

# User input for symptoms (multiselect dropdown to choose multiple symptoms)
selected_symptoms = st.multiselect("Select your symptoms:", symptoms_columns, key="symptoms_input")

# Convert selected symptoms to a binary list (1 for selected, 0 for not selected)
user_symptoms = [1 if symptom in selected_symptoms else 0 for symptom in symptoms_columns]

# Disease details: Description, Causes, Precautions
disease_info = {
    "Flu": {
        "description": "Flu is a contagious respiratory illness caused by influenza viruses.",
        "causes": "Spread through droplets from coughs or sneezes of infected individuals.",
        "precautions": [
            "Get vaccinated annually.",
            "Stay hydrated and rest.",
            "Avoid close contact with sick individuals.",
            "Cover mouth while sneezing or coughing."
        ],
        "emoji": "🤧"
    },
    "Common Cold": {
        "description": "Common cold is a viral infection affecting the nose and throat.",
        "causes": "Spread by rhinoviruses through air droplets or contaminated surfaces.",
        "precautions": [
            "Drink plenty of fluids.",
            "Rest and sleep well.",
            "Avoid close contact with others.",
            "Gargle with salt water for throat relief."
        ],
        "emoji": "🤧" 
    },
    "COVID-19": {
        "description": "COVID-19 is a respiratory disease caused by the SARS-CoV-2 virus.",
        "causes": "Spread via respiratory droplets, especially in crowded places.",
        "precautions": [
            "Wear a mask in public places.",
            "Maintain social distancing.",
            "Wash hands frequently.",
            "Avoid crowded or enclosed spaces."
        ],
        "emoji": "😷" 
    },
    "Typhoid Fever": {
        "description": "Typhoid is a serious bacterial infection causing fever and digestive symptoms.",
        "causes": "Caused by Salmonella typhi through contaminated food or water.",
        "precautions": [
            "Drink clean, boiled or bottled water.",
            "Wash hands thoroughly before eating.",
            "Avoid street food.",
            "Get vaccinated if needed."
        ],
        "emoji": "🤒" 
    },
    "Diphtheria": {
        "description": "Diphtheria is a bacterial infection affecting throat and nose lining.",
        "causes": "Spread through respiratory droplets or contaminated items.",
        "precautions": [
            "Get DTP vaccination.",
            "Avoid sharing utensils or drinks.",
            "Practice good hygiene.",
            "Isolate if infected."
        ],
        "emoji": "🦠" 
    },
    "Adenovirus Infection": {
        "description": "Adenovirus causes respiratory, eye, and digestive tract infections.",
        "causes": "Spread via air, personal contact, or contaminated surfaces.",
        "precautions": [
            "Wash hands often.",
            "Avoid close contact with sick people.",
            "Disinfect surfaces.",
            "Cover nose and mouth while coughing or sneezing."
        ],
        "emoji": "🫁👁️" 
    },
    "Q Fever": {
        "description": "Q fever is a bacterial infection with flu-like symptoms.",
        "causes": "Caused by inhaling dust contaminated by infected animals.",
        "precautions": [
            "Avoid contact with livestock.",
            "Use protective clothing on farms.",
            "Pasteurize dairy products.",
            "Ensure animal areas are ventilated."
        ],
        "emoji": "🥵" 
    },
    "Meningitis": {
        "description": "Meningitis is inflammation of brain and spinal cord membranes.",
        "causes": "Caused by bacteria or viruses; spread via droplets.",
        "precautions": [
            "Get vaccinated.",
            "Avoid close contact with infected persons.",
            "Wash hands frequently.",
            "Maintain general hygiene."
        ],
        "emoji": "🧠" 
    },
    "COPD": {
        "description": "Chronic Obstructive Pulmonary Disease causes breathing difficulties.",
        "causes": "Mainly due to smoking or exposure to harmful gases.",
        "precautions": [
            "Avoid smoking.",
            "Use air purifiers or masks.",
            "Regular exercise under guidance.",
            "Follow medications strictly."
        ],
        "emoji": "😤🫁" 
    },
    "Diabetes Mellitus": {
        "description": "Diabetes is a chronic condition where blood sugar levels are high.",
        "causes": "Caused by insulin resistance or lack of insulin production.",
        "precautions": [
            "Eat a balanced, low-sugar diet.",
            "Exercise regularly.",
            "Monitor blood sugar levels.",
            "Take prescribed medications."
        ],
        "emoji": "🩸☝️" 
    },
    "SLE": {
        "description": "Systemic Lupus Erythematosus is an autoimmune disease.",
        "causes": "Immune system attacks healthy tissues; exact cause is unknown.",
        "precautions": [
            "Avoid sun exposure.",
            "Reduce stress.",
            "Take medications regularly.",
            "Avoid infections."
        ],
        "emoji": "🤒🫁" 
    },
    "Malaria": {
        "description": "Malaria is a mosquito-borne disease causing fever and chills.",
        "causes": "Caused by Plasmodium parasites from mosquito bites.",
        "precautions": [
            "Use mosquito nets and repellents.",
            "Avoid stagnant water.",
            "Wear long clothes.",
            "Take antimalarial tablets when prescribed."
        ],
        "emoji": "🤒🦟" 
    },
    "Ebola Virus Disease": {
        "description": "Ebola is a severe viral hemorrhagic fever.",
        "causes": "Spread through contact with body fluids of infected persons or animals.",
        "precautions": [
            "Avoid contact with infected individuals.",
            "Use protective gear.",
            "Maintain isolation protocols.",
            "Practice proper burial of the dead."
        ],
        "emoji": "🦠" 
    },
    "Tuberculosis": {
        "description": "Tuberculosis is a bacterial infection affecting the lungs.",
        "causes": "Caused by Mycobacterium tuberculosis, spread via air.",
        "precautions": [
            "Ensure good ventilation.",
            "Complete full course of treatment.",
            "Avoid crowded places if infected.",
            "Cover mouth while coughing."
        ],
        "emoji": "🫁🦠" 
    },
    "Hepatitis A": {
        "description": "Hepatitis A affects the liver and is usually short-term.",
        "causes": "Spread through contaminated food or water.",
        "precautions": [
            "Drink clean water.",
            "Wash hands before meals.",
            "Avoid raw or unclean food.",
            "Get vaccinated if needed."
        ],
        "emoji": "😬🥶" 
    }
}


# Chatbot implementation
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Function to update chat history
def update_chat(user_message, bot_response):
    st.session_state.conversation.append(f"**You**: {user_message}")
    st.session_state.conversation.append(f"**HealthBot**: {bot_response}")

# Simple NLP for conversational responses
def chatbot_response(user_message):
    user_message = user_message.lower()

    # Try to detect symptoms mentioned in the user message
    matched_symptoms = [symptom for symptom in symptoms_columns if symptom.lower() in user_message]

    if matched_symptoms:
        # Create input vector from detected symptoms
        input_vector = [1 if symptom in matched_symptoms else 0 for symptom in symptoms_columns]
        pred = model.predict([input_vector])[0]

        response = f"🧠 Based on the symptoms you mentioned ({', '.join(matched_symptoms)}), you may have: **{pred}**.\n\n"
        if pred in disease_info:
            description = disease_info[pred]['description']
            precautions = "\n".join([f"- {item}" for item in disease_info[pred]['precautions']])
            causes = disease_info[pred]['causes']

            response += f"**Description:** {description}\n\n"
            response += f"**Causes:** {causes}\n\n"
            response += f"**Precautions:**\n{precautions}"
        else:
            response += "Sorry, I don't have more info about this disease right now."

        return response

    elif "symptom" in user_message:
        return "Please let me know your symptoms to get a possible condition and treatment."
    else:
        return "I am here to assist you with symptoms and treatments."

# Text-to-speech function
engine = pyttsx3.init()
def speak(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run).start()

# User chat input box
user_message = st.text_input("Talk to HealthBot:", key="user_message_input")

if user_message:
    bot_response = chatbot_response(user_message)
    update_chat(user_message, bot_response)
    speak(bot_response) # healthBot speaks Response

# Display conversation below the input box
if st.session_state.conversation:
    for message in reversed(st.session_state.conversation[-5:]):  # Show last 5 exchanges
        st.write(message)

# Button to check possible disease based on selected symptoms
if st.button("Check Possible Disease"):
    # Create the input vector from user symptoms
    user_input_vector = user_symptoms  
    
    # Make the prediction
    pred = model.predict([user_input_vector])[0]
    pred_prob = model.predict_proba([user_input_vector])[0].max()  # Highest probability
    
    st.success(f"🧠 Based on your symptoms, you may have: **{pred}**")
    st.info(f"Probability: {pred_prob:.2f}")
    
    # Speak out the disease prediction
    speak(f"You may have {pred}.")

    # Show precautions based on predicted disease
    if pred in disease_info:
        st.subheader(f"About {disease_info[pred]['emoji']} {pred}:")
        st.markdown(f"**Description**: {disease_info[pred]['description']}")
        st.markdown(f"**Causes**: {disease_info[pred]['causes']}")
        st.markdown("**Precautions:**")
        for precaution in disease_info[pred]['precautions']:
            st.write(f"- {precaution}")
    else:
        st.write("Sorry, no detailed information available for this disease.")

# Random health tip
    health_tips = [
        "Stay hydrated throughout the day.",
        "Exercise regularly to maintain a healthy body.",
        "Ensure you get at least 7 hours of sleep every night.",
        "Eat a balanced diet with plenty of fruits and vegetables.",
        "Don't forget to wash your hands regularly."
    ]
    st.markdown(f"**Health Tip**: {random.choice(health_tips)}")

    # Display hospital information (example)
    hospital_query = "hospital near me"
    encoded_query = hospital_query.replace(" ", "+")  # Convert space to '+'
    map_link = f"https://www.google.com/maps/search/{encoded_query}"
    st.markdown(f"[📍 Find Hospitals Nearby]({map_link})")

    # Downloadable report
    report = {
        "Symptom(s)": selected_symptoms,
        "Predicted Disease": pred,
        "Precautions": disease_info[pred]["precautions"] if pred in disease_info else "Not available"
    }
    st.download_button(
        label="Download Report",
        data=json.dumps(report, indent=4),
        file_name="health_report.json",
        mime="application/json"
    )

# Clear history if button pressed
if clear_history_button:
    try:
        engine.stop()  # Bolna turant band ho jaaye
    except:
        pass  # Agar engine define nahi hua ho toh error avoid kardega
    
    st.session_state.clear()
    st.rerun()


# Styling for the Streamlit layout
st.markdown("""
    <style>
    .css-ffhzg2 {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f5f5f5;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>input {
        font-size: 16px;
        padding: 10px;
    }
    .stTextInput>div>input:focus {
        border-color: #4CAF50;
    }
    .stCheckbox>label {
        font-size: 16px;
        font-weight: 500;
    }
    .stCheckbox {
        margin-bottom: 10px;
    }
    .stSuccess>div {
        color: #4CAF50;
        font-size: 18px;
    }
    .stInfo>div {
        color: #0073e6;
    }
    </style>
""", unsafe_allow_html=True)

# Caption or Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
