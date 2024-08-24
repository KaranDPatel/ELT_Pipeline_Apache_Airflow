from scripts.get_user import get_current_user
import pandas as pd

def transform_data():
    user_name = get_current_user()
    print(f"Transforming data as {user_name}")

    # Load extracted data
    df = pd.read_csv('data/extracted_data.csv')

    # Perform basic transformations, e.g., filtering and aggregation
    df_filtered = df[df['value'] > 10]
    df_aggregated = df_filtered.groupby('category').sum().reset_index()

    df_aggregated.to_csv('data/transformed_data.csv', index=False)
    print("Data transformed successfully.")
