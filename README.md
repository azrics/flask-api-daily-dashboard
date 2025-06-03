# NexVerse Freebie Pack: Flask User Management App

Welcome to the **NexVerse Freebie Pack**!  
This repository is a quick-start template for Python web development, automation, and testing using Flask.  
It includes a user management app with registration, login, profile update, password reset, and a modern UI.  
You also get a ready-to-use CI/CD pipeline with pytest for automated testing.

---

## 🚀 Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo/user-management-app/src
```

### 2. Install Dependencies

Make sure you have Python 3.11+ installed.

```sh
pip install -r ../requirements.txt
```

### 3. Run the Application

```sh
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🧪 Running Tests

All tests are in the `src` folder and use `pytest`.  
To run tests locally and see detailed output:

```sh
pytest -s
```

You’ll see green ticks (✅) for success and red crosses (❌) for failures, along with clear explanations.

---

## 🤖 CI/CD with GitHub Actions

Every push or pull request to the `main` branch triggers automated tests via GitHub Actions.

- Workflow file: `.github/workflows/python-app.yml`
- Test results and print outputs are visible in the "Actions" tab of your GitHub repo.

**How to view results:**
1. Go to your repository on GitHub.
2. Click the "Actions" tab.
3. Select the latest workflow run to see logs and test results.

---

## 🛠️ Making Changes

1. **Edit code or templates** in the `user-management-app/src` directory.
2. **Add new features or tests** as needed.
3. **Commit and push** your changes:
    ```sh
    git add .
    git commit -m "Describe your change"
    git push
    ```
4. **Check the Actions tab** on GitHub to ensure all tests pass.

---

## 💾 Database Backup

To back up your SQLite database, run:

```sh
python backup_db.py
```

Backups are stored in the `db_backups/` folder.

---

## 📦 Features

- User registration, login, logout
- Profile update and password reset
- Beautiful, responsive UI
- Pytest-based testing with clear console output
- GitHub Actions CI/CD pipeline
- Easy database backup script

---

## 📝 License

This project is part of the **NexVerse Freebie Pack** and is free to use for learning and rapid prototyping.

---

Happy coding!  
**NexVerse Team**