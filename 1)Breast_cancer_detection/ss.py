import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Example DataFrame
data = {
    'id': [842302, 842517, 84300903, 84348301],
    'Diagnosis': ['M', 'M', 'M', 'B'],  # Use the correct column name
    'radius_mean': [17.99, 20.57, 19.69, 11.42],
    'texture_mean': [10.38, 17.77, 21.25, 20.38]
    # ... (other columns)
}

dataset = pd.DataFrame(data)

# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Encode the 'Diagnosis' column
dataset['diagnosis_encoded'] = label_encoder.fit_transform(dataset['Diagnosis'])

# Print the final DataFrame
print(dataset)





