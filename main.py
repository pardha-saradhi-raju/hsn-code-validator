import pandas as pd

# Load the dataset
df = pd.read_excel("HSN_Master_Data.xlsx", engine="openpyxl")

def validate_hsn(params):
    hsn_codes = params["hsn_code"]
    results = []

    for code in hsn_codes:
        if not code.isdigit() or len(code) not in [2, 4, 6, 8]:
            results.append(f"{code} ❌ Invalid format (must be numeric and 2/4/6/8 digits)")
            continue

        match = df[df["HSNCode"].astype(str) == code]
        if not match.empty:
            desc = match.iloc[0]["Description"]
            results.append(f"{code} ✅ Valid: {desc}")
        else:
            results.append(f"{code} ❌ Invalid: Not found in database")
    
    return {"messages": [{"text": "\n".join(results)}]}
