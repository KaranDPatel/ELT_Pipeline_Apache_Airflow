from scripts.get_user import get_current_user
import pandas as pd

def load_data():
    user_name = get_current_user()
    print(f"Loading data as {user_name}")

    # Load transformed data
    df = pd.read_csv('data/transformed_data.csv')

    # Save the transformed data to a new CSV file
    df.to_csv('data/output_data.csv', index=False)
    print("Data loaded successfully.")
