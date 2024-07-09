import json
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def optimize_inputs(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    stop_words = set(stopwords.words('english'))

    for item in data['general_bad']:
        # Clean the input text
        cleaned_input = clean_text(item['input'])
        
        # Tokenize and remove stop words
        tokens = word_tokenize(cleaned_input)
        optimized_input = ' '.join([word for word in tokens if word not in stop_words])
        
        item['input'] = optimized_input

    output_file = 'optimized_' + json_file
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Optimized inputs saved to '{output_file}'")
    
    # Print some examples of the optimization
    print("\nOptimization Examples:")
    for i, item in enumerate(data['general_bad'][:5], 1):  # Show first 5 examples
        print(f"{i}. Original: '{item['input']}'")
        print(f"   Optimized: '{item['input']}'")
        print()

# Usage
optimize_inputs('general-bad.json')