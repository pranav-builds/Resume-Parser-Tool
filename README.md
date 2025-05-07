# 📄 Resume Parser & PDF Organizer Tool

An automated Python tool that **organizes PDF resumes** and **extracts key details** like **Name**, **Email**, **Phone Number**, and **Skills** into a clean Excel sheet. Built as a **beginner-to-intermediate level** project, this tool blends simplicity, automation, and real-world utility — perfect for portfolio building.

---

## 🚀 Features

- 🗂️ Organizes PDF files by last modified date  
- 🔍 Extracts key resume info:
  - ✅ Full Name
  - ✅ Email Address
  - ✅ Phone Number
  - ✅ Skills (via Regex)
- 📊 Generates a styled Excel output
- 💻 Beautiful terminal display using `tabulate` and `rich`
- 🧠 Great use-case for HR teams, recruiters, or freelancers

---

## 🧰 Tech Stack

| Tool          | Purpose                      |
|---------------|------------------------------|
| Python 3.10+  | Core scripting language      |
| os, shutil    | File & folder management     |
| pdfplumber    | PDF text extraction          |
| re (Regex)    | Pattern matching             |
| pandas        | Structured data handling     |
| openpyxl      | Excel output                 |
| tabulate, rich| Terminal visualization       |

---

## 📁 Project Structure

```
Resume-Parser-Tool/
├── resumes/                # Folder containing PDF resumes
├── output/                 # Output Excel file saved here
├── main.py                 # Main script (organize + parse)
├── parser.py               # Resume parsing logic
├── requirements.txt        # List of dependencies
└── README.md               # Project overview
```

---

## 🖥️ How to Use

### 1️⃣ Clone the Repository


### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add Resumes

inside the `resumes/` folder.

### 4️⃣ Run the Tool

```bash
python main.py
```

### ✅ Output

- An Excel file: `output/extracted_data.xlsx`
- A terminal summary of extracted info

---

## ✨ Potential Improvements

- Resume **ranking** based on job description match  
- Web-based version using **Streamlit** or **Flask**  
- Integration with **email or cloud storage**  
- **Keyword search** in resumes (e.g. Python, SQL)

---

## 📚 What You Learn

- Python file handling & folder automation  
- Regular expressions (regex) for data extraction  
- PDF parsing using `pdfplumber`  
- Working with Excel using `pandas` + `openpyxl`  
- Clean CLI output using `rich` & `tabulate`  
- Real-world project structure and documentation

---

## 👤 Author

Made with ❤️ by [Pranav](https://github.com/pranav-builds/)  
📫 Connect on [LinkedIn](https://www.linkedin.com/in/pranav-92267a309/)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
