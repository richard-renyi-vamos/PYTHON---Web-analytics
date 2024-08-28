import pandas as pd

def analyze_website_usage(log_file):
    # Load the log file into a DataFrame
    df = pd.read_csv(log_file)
    
    # Assuming the log file has a 'user_id' column for unique users
    if 'user_id' in df.columns:
        unique_users = df['user_id'].nunique()
        print(f"Number of unique users: {unique_users}")
    
    # Assuming the log file has a 'timestamp' column for visit times
    if 'timestamp' in df.columns:
        total_visits = df['timestamp'].count()
        print(f"Total number of visits: {total_visits}")
    
    # Example: Counting visits per day
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        visits_per_day = df.groupby(df['timestamp'].dt.date).size()
        print("Visits per day:")
        print(visits_per_day)

# Usage
log_file_path = 'path_to_your_log_file.csv'
analyze_website_usage(log_file_path)
