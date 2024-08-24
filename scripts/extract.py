from scripts.get_user import get_current_user
import pandas as pd

def extract_data():
    user_name = get_current_user()
    print(f"Extracting data as {user_name}")

    # Load data from a CSV file
    df = pd.read_csv('data/input_data.csv')
    df.to_csv('data/extracted_data.csv', index=False)
    print("Data extracted successfully.")
