# 📦 HSN Code Validation Agent (ADK-Style + Streamlit)

This project is a conceptual implementation of an **HSN Code Validation Agent** using the **ADK (Agent Developer Kit) architecture**. It allows users to validate HSN codes from a master Excel dataset using a friendly chatbot interface built with Streamlit.

---

## 🧠 Agent Design (Using ADK Framework)

### ✅ Overall Architecture

The agent follows a modular ADK-style design:

| Component       | Description |
|----------------|-------------|
| **Agent**       | `hsn-validation-agent` – central controller |
| **Intent**      | `validate_hsn` – triggered to validate one or more HSN codes |
| **Entity**      | `hsn_code` – a string or list of strings (e.g., `0101`, `01011010`) |
| **Fulfillment** | `validate_hsn()` in `main.py`, returns validation responses |
| **Data Store**  | Excel file (`HSN_Master_Data.xlsx`) with HSNCode and Description columns |

### 🧾 Input Handling

- Accepts a **single HSN code** or **multiple comma-separated codes**
- Parses them and processes each individually

### 🧾 Output Handling

- For **valid codes**: Returns ✅ message with code and its description
- For **invalid codes**: Returns ❌ with reason like "not found" or "invalid format"

---

## 🗂️ Data Handling Strategy

### 📥 Accessing and Processing Excel

- Excel file (`HSN_Master_Data.xlsx`) is read once using `pandas.read_excel()` with `openpyxl` engine
- Stored in memory as a DataFrame to ensure fast lookup

### ⏱️ Pre-Processing vs On-Demand

- **Pre-load Strategy Used**:
  - Loads the entire file once at startup
  - Fast lookups for all validation operations
  - **Trade-off**: File changes require re-running the app

---

## 🧪 Validation Logic

### ✅ Format Validation

Each input code must:
- Be numeric
- Be of length **2, 4, 6, or 8 digits** (standard HSN structure)

### ✅ Existence Validation

- Checks if the **exact code exists** in the `HSNCode` column of the dataset

### 🌲 (Optional) Hierarchical Validation (Suggested for Bonus)

For a given 8-digit code like `01011010`:
- Check if parent codes like `01`, `0101`, and `010110` also exist
- This shows structural validity across HSN hierarchy
- Adds semantic value and highlights inconsistencies in master data

---

## 💬 Agent Response Format

### ✅ For Valid Codes:
01011010 ✅ Valid: PURE-BRED BREEDING ANIMAL



### ❌ For Invalid Codes (Not Found):
ABC123 ❌ Invalid format (must be numeric and 2/4/6/8 digits)





---

## 💡 Expected Interview Deliverables

### 🧩 Design Summary

- Built using ADK-style components
- Fulfillment logic written in Python (`main.py`)
- UI implemented using Streamlit (`chatbot.py`)
- Excel file used as data source
- Config files:
  - `agent.yaml` – defines agent
  - `intent.yaml` – defines intent, entity, fulfillment

### 📈 Clarity, Robustness, and Edge Handling

- Proper input validation
- Handles empty, malformed, or non-numeric codes
- Modular code and logical separation of concerns

---

## 🚀 How to Run This Agent Locally

### 🔧 Requirements

Install required libraries:

```bash
pip install -r requirements.txt

▶️ Start the chatbot

streamlit run chatbot.py

---

🗃️ File Structure

hsn-agent/
│
├── main.py               # Fulfillment logic
├── chatbot.py            # Streamlit chatbot UI
├── HSN_Master_Data.xlsx  # Excel file with valid codes
├── agent.yaml            # Agent definition (ADK-style)
├── intent.yaml           # Intent & entity definition
├── requirements.txt      # Python dependencies
└── README.md             # This file

---

🏆 Bonus Discussion Points

✅ Can support dynamic Excel file upload in the future

✅ Hierarchical validation logic can improve classification accuracy

✅ Agent can be extended to flag data anomalies in the master file (e.g., duplicate or missing parents)

✅ Conversational UI encourages user interaction