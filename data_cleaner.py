import pandas as pd

# ==== CONFIGURE FILES ====
input_file = "sample_input.csv"     # CSV to clean
output_file = "cleaned_output.xlsx" # Excel output

# ==== CLEANING FUNCTION ====
def clean_csv(input_file, output_file):
    """
    Cleans a CSV file and saves it as an Excel file with summary stats.
    Steps:
    1. Remove duplicate rows
    2. Fill missing values with 'N/A'
    3. Standardize column names
    4. Generate summary statistics
    """
    # Load CSV
    df = pd.read_csv(input_file)

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna("N/A")

    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Save to Excel
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Cleaned Data")
        summary = df.describe(include="all").transpose()
        summary.to_excel(writer, sheet_name="Summary Stats")

    print(f"✅ Cleaned data saved to {output_file}")

# ==== RUN SCRIPT ====
if __name__ == "__main__":
    clean_csv(input_file, output_file)
