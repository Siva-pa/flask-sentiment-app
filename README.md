# 🚀 Flipkart Sentiment Analysis Web App

> 🌐 Live Demo: **http://54.153.221.175:5000**

---

## 🧠 Project Overview

This project is an **end-to-end Machine Learning web application** that performs **sentiment analysis on Flipkart product reviews**.

It predicts whether a review is:

- 😊 **Positive**
- 😠 **Negative**

Built using Flask and deployed on AWS EC2, this project demonstrates a complete **MLOps workflow** from data to deployment.

---

## ⚡ Key Highlights

- ✨ Real-time sentiment prediction  
- ✨ End-to-end ML pipeline  
- ✨ Deployed on cloud (AWS EC2)  
- ✨ Production-ready with Gunicorn  
- ✨ Handles real-world messy datasets  
- ✨ Clean UI using Flask templates  

---

## 🛠️ Tech Stack

- **Language:** Python 🐍  
- **Backend:** Flask  
- **ML Algorithm:** Logistic Regression  
- **NLP:** NLTK  
- **Feature Engineering:** TF-IDF  
- **Deployment:** AWS EC2  
- **Server:** Gunicorn  
- **Version Control:** GitHub  

---

## 📊 Machine Learning Pipeline

Raw Data → Cleaning → Preprocessing → TF-IDF → Model → Flask → AWS


---

## 📁 Project Structure

```
flask-sentiment-app/
│── app.py # Flask application
│── sentiment_model.pkl # Trained ML model
│── tfidf_vectorizer.pkl # TF-IDF vectorizer
│── requirements.txt
│── mlflow.db # Experiment tracking
│── Sentiment_Analysis_notebook.ipynb
│
├── templates/
│ └── index.html # Frontend UI
│
├── reviews_badminton/ # Dataset folder
│
└── .ipynb_checkpoints/

```

---

## 🔍 Features

- 🧠 ML-based sentiment prediction  
- ⚡ Fast real-time inference  
- 🧹 Text preprocessing (stopwords, lemmatization)  
- 📦 Model loading using pickle  
- 🌐 Publicly deployed app  
- 🛡️ Handles invalid inputs gracefully  

---

## ⚙️ Local Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Siva-pa/flask-sentiment-app.git
cd flask-sentiment-app
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run Application

```
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

### ☁️ Deployment (AWS EC2)

Steps followed:

🚀 Created EC2 instance (Ubuntu)
🔐 Configured security groups (22, 80, 5000)
🔑 Connected via SSH (.pem key)
📥 Cloned repo from GitHub
🧪 Created virtual environment
📦 Installed dependencies
⚡ Deployed using Gunicorn:

```
gunicorn app:app --bind 0.0.0.0:5000
```

### 💡 Key Learnings

🔁 End-to-end ML lifecycle
🌐 Cloud deployment (AWS EC2)
🐍 Flask web development
⚙️ Production server setup (Gunicorn)
🔐 Networking & security basics
🧠 Handling real-world data
🔮 Future Improvements
🔒 Add HTTPS (SSL with Nginx)
🌍 Custom domain integration
🎨 Improve UI/UX
📡 Add REST API endpoints
🐳 Dockerize application
📊 Monitoring with CloudWatch

### 👨‍💻 Author

Siva Kishore Pasupuleti

🎯 Aspiring AI/ML Engineer
🚀 Focused on MLOps & Deployment
⭐ Show Your Support

If you found this useful:

⭐ Star this repository
💬 Share feedback
🤝 Connect on LinkedIn

### 🏁 Final Note

This project showcases a complete real-world ML deployment pipeline:

📊 Data → 🧠 Model → 🌐 Web App → ☁️ Cloud Deployment
