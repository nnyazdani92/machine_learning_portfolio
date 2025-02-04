from pathlib import Path

import pandas as pd
import joblib

def main():
    df = pd.read_csv("data/processed/processed_data.csv")
    
    X = df.drop('target', axis=1)
    y = df['target']
    
    #TODO: Train scikit-learn model
    
    model_path = Path("models/model.pkl")
    model_path.parent.mkdir(exist_ok=True)
    joblib.dump(model, model_path)

if __name__ == "__main__":
    main()