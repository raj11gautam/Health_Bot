import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load the data with tab-separated delimiter
symptom_data = pd.read_csv('data/symptoms.csv', delimiter='\t')

# Print columns to check if they are properly split
print(symptom_data.columns)

# Updated features based on the new dataset columns
features = ['Fever', 'Cough', 'Fatigue', 'Headache', 'Sore Throat', 'Muscle Aches', 'Loss of Appetite', 
            'Nausea', 'Vomiting', 'Diarrhea', 'Shortness of Breath', 'Rashes', 'Dizziness', 
            'Sweating', 'Sleep Disturbances', 'Weight Loss']

X = symptom_data[features]

# Target (column for disease)
y = symptom_data['Disease']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the DecisionTreeClassifier model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model training complete and saved as 'model.pkl'")
