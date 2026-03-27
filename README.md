# 🚀 ME & PDFs

An all-in-one **PDF + AI toolkit** built with Flask that allows users to convert, edit, manage, and interact with PDFs seamlessly.

---

## ✨ Features

### 📄 PDF Tools

* Merge PDF
* Split PDF
* Compress PDF
* Add Page Numbers
* Watermark (Text + Image)
* Sign PDF
* Protect / Unlock PDF

### 🔄 Converters

* PDF → Word
* Word → PDF
* PDF → JPG
* JPG → PDF
* Excel → PDF
* PPT → PDF
* HTML → PDF

### 🤖 AI Tools

* AI Summarizer
* AI Translator
* AI Rewriter
* Chat with PDF
* AI Document Generator
* AI PPT Generator
* AI Website Summarizer

### 🌐 Other Features

* Supabase Authentication (Login / Signup)
* File Storage & Management
* Interactive Editor
* Watermark Studio (Drag & Drop UI)
* Clean UI with Glassmorphism Design

---

## 🛠 Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, JavaScript, Bootstrap
* **Database:** PostgreSQL / SQLite
* **Auth & Storage:** Supabase
* **Libraries:**

  * PyPDF2
  * reportlab
  * python-docx
  * python-pptx
  * pdf2image
  * Pillow
  * BeautifulSoup

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/me-pdfs.git
cd me-pdfs
```

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup environment variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key

DB_HOST=your_host
DB_NAME=your_db
DB_USER=your_user
DB_PASS=your_password
DB_PORT=5432

EMAIL_USER=your_email
EMAIL_PASS=your_password
```

---

### 5️⃣ Run the app

```bash
python app.py
```

👉 Open: http://127.0.0.1:5000

---

## 📁 Project Structure

```
ME-PDFS/
│── app.py
│── auth.py
│── database.py
│── supabase_client.py
│── requirements.txt
│── Procfile
│
├── templates/
├── static/
├── utils/
│   ├── converter.py
│   ├── ai_tools.py
│   ├── ocr.py
```

---

## 👨‍💻 Team

* **Niket Thakur** (Team Lead & Developer)
* **Nikhil Singh Chauhan** (Frontend & Design)

---

## 📌 Future Improvements

* Real PDF preview (pdf.js)
* Multi-watermark support
* Drag-resize UI (like Canva)
* Cloud deployment (Render / AWS)
* User analytics dashboard

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---

## 📜 License

This project is for educational and hackathon purposes.
