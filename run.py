from src.pipeline import process_document

if __name__ == "__main__":
    df = process_document("samples/sample_invoice.png")
    print("\nEXTRACTED TABLE:\n")
    print(df)
    df.to_csv("extracted_table.csv", index=False)
    print("\nSaved extracted_table.csv")
