import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Load the dataset
try:
    data = pd.read_csv("water_potability.csv")
except FileNotFoundError:
    print("Error: water_potability.csv not found. Please place the file in the same directory.")
    exit()

# Handle missing values (replace with mean for numerical columns)
numerical_cols = data.select_dtypes(include=['number']).columns
for col in numerical_cols:
    data[col].fillna(data[col].mean(), inplace=True)


# Preprocessing
X = data.drop('Potability', axis=1)
y = data['Potability']

# Encode categorical features (if any –  this dataset doesn't appear to have any directly)
# For example, if you had a categorical feature 'source' you'd use:
# le = LabelEncoder()
# X['source'] = le.fit_transform(X['source'])

# Scale numerical features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier (You can experiment with other models)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")


# --- Tkinter UI ---
def predict_potability():
    try:
        ph = float(ph_entry.get())
        Hardness = float(hardness_entry.get())
        Solids = float(solids_entry.get())
        Chloramines = float(chloramines_entry.get())
        Sulfate = float(sulfate_entry.get())
        Conductivity = float(conductivity_entry.get())
        Organic_carbon = float(organic_carbon_entry.get())
        Trihalomethanes = float(trihalomethanes_entry.get())
        Turbidity = float(turbidity_entry.get())

        input_data = [[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]]
        input_data = scaler.transform(input_data) #Important: Scale input data using the same scaler!
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            result_label.config(text="Water is potable.")
        else:
            result_label.config(text="Water is not potable.")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


root = tk.Tk()
root.title("Water Potability Predictor")

#Input fields
ph_label = ttk.Label(root, text="pH:")
ph_entry = ttk.Entry(root)
hardness_label = ttk.Label(root, text="Hardness:")
hardness_entry = ttk.Entry(root)
solids_label = ttk.Label(root, text="Solids:")
solids_entry = ttk.Entry(root)
chloramines_label = ttk.Label(root, text="Chloramines:")
chloramines_entry = ttk.Entry(root)
sulfate_label = ttk.Label(root, text="Sulfate:")
sulfate_entry = ttk.Entry(root)
conductivity_label = ttk.Label(root, text="Conductivity:")
conductivity_entry = ttk.Entry(root)
organic_carbon_label = ttk.Label(root, text="Organic Carbon:")
organic_carbon_entry = ttk.Entry(root)
trihalomethanes_label = ttk.Label(root, text="Trihalomethanes:")
trihalomethanes_entry = ttk.Entry(root)
turbidity_label = ttk.Label(root, text="Turbidity:")
turbidity_entry = ttk.Entry(root)


#Place the labels and entry fields in the UI (using grid for layout)
ph_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
ph_entry.grid(row=0, column=1, padx=5, pady=5)
hardness_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
hardness_entry.grid(row=1, column=1, padx=5, pady=5)
solids_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
solids_entry.grid(row=2, column=1, padx=5, pady=5)
chloramines_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
chloramines_entry.grid(row=3, column=1, padx=5, pady=5)
sulfate_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')
sulfate_entry.grid(row=4, column=1, padx=5, pady=5)
conductivity_label.grid(row=5, column=0, padx=5, pady=5, sticky='w')
conductivity_entry.grid(row=5, column=1, padx=5, pady=5)
organic_carbon_label.grid(row=6, column=0, padx=5, pady=5, sticky='w')
organic_carbon_entry.grid(row=6, column=1, padx=5, pady=5)
trihalomethanes_label.grid(row=7, column=0, padx=5, pady=5, sticky='w')
trihalomethanes_entry.grid(row=7, column=1, padx=5, pady=5)
turbidity_label.grid(row=8, column=0, padx=5, pady=5, sticky='w')
turbidity_entry.grid(row=8, column=1, padx=5, pady=5)


predict_button = ttk.Button(root, text="Predict", command=predict_potability)
predict_button.grid(row=9, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=10, column=0, columnspan=2)

root.mainloop()