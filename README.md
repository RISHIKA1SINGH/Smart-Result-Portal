
# 🎓 Smart Result Portal

A Flask + MongoDB-based student result portal where students can log in securely to view their marks, aggregate percentage, and pass/fail status — complete with a printable result page.

## 🚀 Features

- 🔐 Secure login system for students  
- 📄 View subject-wise marks, aggregate, and status  
- 🖨️ Download/print result as PDF  
- 🌐 Responsive and clean UI  
- 🧠 Data managed using MongoDB  

## 🛠️ Tech Stack

- **Backend:** Flask (Python)  
- **Frontend:** HTML, CSS (Robust styling with custom design)  
- **Database:** MongoDB  
- **Template Engine:** Jinja2 (Flask default)


## 🧪 Sample Users

| Username | Password  | Roll No |
|----------|-----------|---------|
| priya22  | priya123  | R006    |
| jane21   | jane123   | R002    |
| ravi22   | ravi123   | R003    |
| sneha20  | sneha123  | R004    |

## ▶️ Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/smart-result-portal.git
   cd smart-result-portal
````

2. **Install dependencies**

   ```bash
   pip install flask pymongo
   ```

3. **Run MongoDB**

   Make sure MongoDB is running locally (default port `27017`) or update the URI in `app.py`.

4. **Start the app**

   ```bash
   python app.py
   ```

5. **Open in browser**

   Navigate to [http://localhost:5000](http://localhost:5000)


## 📝 License

MIT License.
Feel free to use, modify, and share.


