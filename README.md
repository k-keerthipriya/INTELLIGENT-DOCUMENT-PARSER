# 🧠 Intelligent Document Parser

An AI-powered pipeline designed to extract **structured tables** and **semantic information** from scanned documents such as invoices, reports, receipts, and forms.

This system integrates:
- **OCR (Tesseract)** to read text + bounding boxes  
- **LayoutLMv3 Transformer Model** for understanding document structure  
- **Custom table reconstruction logic** for headers, rows, and hierarchical formatting  

---

## 🚀 Features
- Extracts words + bounding boxes using OCR  
- Identifies table headers, sub-headers, rows, and columns  
- Uses LayoutLMv3 for spatial-text understanding  
- Reconstructs clean, structured tables  
- Exports results to CSV or JSON  
- Works on invoices, financial reports, and printed tables  

---

## 🛠️ Tech Stack
- Python  
- Tesseract OCR  
- LayoutLMv3 (Transformers)  
- OpenCV  
- Pandas  

---

## 📌 Usage
```bash
python run.py
```

---

## 📂 Output
- Clean table extracted from the scanned document  
- Saved as `extracted_table.csv`

---

## 🧑‍💻 Author
cutieluu 💗
