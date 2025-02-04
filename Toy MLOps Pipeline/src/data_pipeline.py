import pandas as pd
from pathlib import Path

def main():
    raw_path = Path("data/raw/data.csv")
    df = pd.read_csv(raw_path)
    
    # Clean data
    df = df.dropna().reset_index(drop=True)
    
    #TODO: Process data
    #TODO: Save processed data

if __name__ == "__main__":
    main()