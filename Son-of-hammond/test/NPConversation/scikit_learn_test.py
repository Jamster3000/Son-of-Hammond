import random
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.calibration import CalibratedClassifierCV

class NPCInteractionModel:
    def __init__(self, json_file):
        self.intent_vectorizer = TfidfVectorizer()
        self.intent_classifier = CalibratedClassifierCV(LinearSVC(dual=False))
        self.load_data(json_file)

    def load_data(self, json_file):
        with open(json_file, 'r') as file:
            self.data = json.load(file)
        self.responses = {}
        self.intent_data = []
        for item in self.data['general_bad']:
            self.responses[item['category']] = item['responses']
            self.intent_data.append({"text": item['input'], "intent": item['category']})

    def train(self):
        X = [item['text'] for item in self.intent_data]
        y = [item['intent'] for item in self.intent_data]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        X_train_vectorized = self.intent_vectorizer.fit_transform(X_train)
        X_test_vectorized = self.intent_vectorizer.transform(X_test)
        
        self.intent_classifier.fit(X_train_vectorized, y_train)
        
        y_pred = self.intent_classifier.predict(X_test_vectorized)
        
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        
        print(f"Model Accuracy: {accuracy:.2f}")
        print("\nClassification Report:")
        print(report)

    def predict_intent(self, user_input):
        vectorized_input = self.intent_vectorizer.transform([user_input])
        intent = self.intent_classifier.predict(vectorized_input)[0]
        confidence = np.max(self.intent_classifier.predict_proba(vectorized_input))
        return intent, confidence

    def get_response(self, intent):
        if intent in self.responses:
            return random.choice(self.responses[intent])
        else:
            return "I don't have time for this nonsense."

    def process_input(self, user_input):
        intent, confidence = self.predict_intent(user_input)
        response = self.get_response(intent)
        return response, intent, confidence

# Example usage
if __name__ == "__main__":
    npc_model = NPCInteractionModel('general-bad.json')
    npc_model.train()

    print("\nNPC is ready. Type 'quit' to exit.")
    while True:
        user_input = input("Player: ")
        if user_input.lower() == 'quit':
            break
        response, intent, confidence = npc_model.process_input(user_input)
        print(f"NPC: {response}")
        print(f"Detected Intent: {intent}")
        print(f"Confidence: {confidence:.2f}")