import pandas as pd

def load_data(file_path):
    """Loads a CSV file into a Pandas DataFrame."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def save_data(data, file_path):
    """Saves a Pandas DataFrame to a CSV file."""
    try:
        data.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to {file_path}: {e}")
