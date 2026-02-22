# 📊 GitHub Profile Language Analyzer

A Python-based tool that analyzes a GitHub profile and visualizes the distribution of programming languages used across all repositories.

This project integrates with the GitHub REST API, securely authenticates using environment variables, aggregates language statistics, and generates a pie chart using Matplotlib.

---

## 🚀 Features

* Fetches all public repositories of a GitHub user
* Aggregates language usage across repositories
* Skips forked repositories for cleaner analytics
* Secure authentication using Personal Access Token
* Generates a pie chart visualization
* Clean and modular Python implementation

---

## 🛠 Tech Stack

* Python 3.x
* GitHub REST API
* requests
* matplotlib
* python-dotenv

---

## 📂 Project Structure

```
Github_Repo_analyzer/
│
├── githubProfileAnalyzer.py
├── .env
├── .gitignore
├── Demo.png
```

---

## 🔐 Setup Instructions

### 1️⃣ Clone the Repository

```
git clone <your-repository-link>
cd Github_Repo_analyzer
```

---

### 2️⃣ Install Dependencies

```
pip install requests matplotlib python-dotenv
```

---

### 3️⃣ Create `.env` File

Create a `.env` file in the project root directory:

```
GITHUB_USERNAME=your_username
GITHUB_TOKEN=your_personal_access_token
```

⚠️ Make sure `.env` is included inside `.gitignore` to prevent pushing secrets.

---

### 4️⃣ Run the Script

```
python githubProfileAnalyzer.py
```

---

## 📈 Output

The script generates a pie chart showing the distribution of programming languages used across the GitHub profile.

Example Output:

![Language Distribution]([Demo.png](https://github.com/Aditya-xcity/GitHub-analytics/blob/main/Github_Repo_analyzer/Demo.png))

---

## 🧠 What This Project Demonstrates

* API integration and HTTP requests
* Handling API rate limits
* Secure token-based authentication
* Environment-based configuration
* Data aggregation and transformation
* Data visualization using Matplotlib

---

## 📌 Future Improvements

* Add bar chart visualization option
* Export analytics to JSON format
* Generate PDF summary report
* Build a web dashboard version
* Add support for private repositories

---

## 📄 License

This project is open for learning, experimentation, and further enhancement.
