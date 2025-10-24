# Procurement Portal

A web-based Procurement Portal built using Flask, designed to manage college inventory and procurement requests efficiently. This README will guide you from installation to running the application locally.

---

## 🚀 Features

* Department-based item request form
* Estimated cost and justification section
* File upload for authorization documents
* Displays list of submitted requests (frontend only)
* Backend-ready structure for developers to implement logic

---

## 📂 Project Structure

```
procurement_portal/
│-- app.py
│-- .gitignore
│-- requirements.txt (optional)
│-- static/
│   └── css/style.css
│-- templates/
│   ├── base.html
│   ├── index.html
│   ├── request_form.html
│   ├── success.html
│   └── list_requests.html
```

---

## ✅ Prerequisites

Make sure you have the following installed:

* **Python 3.8+**
* **PIP (Python Package Installer)**
* **Git** (optional but recommended)

---

## ⚙️ Step 1: Clone or Download the Project

### If using Git:

```bash
git clone https://github.com/your-username/procurement_portal.git
cd procurement_portal
```

### If downloaded as ZIP:

* Extract the folder
* Open it in **VS Code or Terminal**

---

## 🔧 Step 2: Create Virtual Environment

Open terminal in the project folder and run:

```bash
python -m venv venv
```

Activate the environment:

### On Windows (PowerShell):

```bash
venv\Scripts\activate
```

### On macOS/Linux:

```bash
source venv/bin/activate
```

You should now see `(venv)` before your terminal path.

---

## 📦 Step 3: Install Required Packages

```bash
pip install flask
```

If using `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🏃 Step 4: Run the Application

```bash
python app.py
```

After running, you will see something like:

```
Running on http://127.0.0.1:5000/
```

👉 Open your browser and go to: **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 📚 File Descriptions

| File Name          | Description                                 |
| ------------------ | ------------------------------------------- |
| app.py             | Main Flask application file                 |
| base.html          | Master layout file for templates            |
| index.html         | Homepage with navigation                    |
| request_form.html  | Procurement request submission form         |
| list_requests.html | View all submitted requests (frontend only) |
| success.html       | Displays submission success message         |
| style.css          | Custom styling file                         |

---

## 🔄 How to Stop the Server

Press `CTRL + C` in the terminal.

---

## 🛠 Backend Integration Guide (For Developers)

* Add a database (SQLite or MySQL)
* Create `models.py` for database tables
* Use SQLAlchemy for ORM
* Implement CRUD in `app.py` or separate into `routes.py`

---

## 📌 Future Enhancements

* User authentication
* Role-based access (Admin, HOD, Store Manager)
* Email notifications
* Approval workflow

---

## 🤝 Contribution Guidelines

1. Create a new branch: `git checkout -b feature-xyz`
2. Make changes and commit: `git commit -m "Added new feature"`
3. Push and create pull request

---

## 📄 License

This project is open for educational and development purposes.

---

## 💬 Need Help?

Feel free to raise issues or contribute to the project. Happy coding! ✨
