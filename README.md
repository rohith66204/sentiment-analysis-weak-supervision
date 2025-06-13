# 🛍️ Sentiment Analysis of Product Reviews with Weak Supervision

This project presents a **web-based sentiment analysis system** built using **Python**, **Django**, and **deep learning** techniques to classify customer product reviews as **positive or negative**. It uses a **Weakly-supervised Deep Embedding (WDE)** framework that leverages review ratings as weak labels to improve sentiment classification accuracy.

---

## 🚀 Features

- User & Admin login system  
- Admin uploads products with details  
- Users can view, rate, and review products  
- Sentiment classification using Naive Bayes  
- Weak supervision via review ratings  
- Real-time prediction of review sentiment  
- Graphical reports using pie and bar charts  
- Django-based UI with Bootstrap styling  

---

## 🔐 Admin Login and User Activation

- After registration, new users are **inactive by default**  
- Admin logs in with credentials:
  - **Username:** `admin`
  - **Password:** `admin`  
- Admin navigates to the **user activation panel**, reviews pending accounts, and activates them using the admin password for confirmation

> 🛡️ This process ensures only authorized users get access to the system features

---

## 🧠 Techniques Used

- Weakly-supervised Deep Embedding (WDE)  
- Naive Bayes classifier  
- CNN & LSTM for review embedding  
- Text preprocessing (cleaning, vectorizing)  
- Review rating-based supervision  
- Graphical data visualization (Matplotlib / Chart.js)  

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Backend:** Python, Django  
- **Database:** MySQL (WAMP)  
- **ML Libraries:** Scikit-learn  
- **Other Tools:** WAMP Server, VS Code  

---

## 📊 Modules

1. **Product Initiation:** Admin uploads and manages product listings  
2. **Product Browsing:** Users view product details, ratings, reviews  
3. **Review Submission:** Users rate & review purchased products  
4. **Sentiment Classification:** Naive Bayes model analyzes sentiment  
5. **Weak Supervision:** System compares rating with sentiment  
6. **Graphical Analysis:** Admin and users see sentiment and rating charts  

---

## 🧪 Testing & Validation

- ✅ Unit Testing  
- ✅ Integration Testing  
- ✅ System Testing  
- ✅ Acceptance Testing  
- ✅ White Box & Black Box Testing  

> All test cases passed successfully with no defects encountered.

---

## 🧪 How It Works

1. Admin uploads product listings via dashboard  
2. User registers, logs in (post-activation), and explores products  
3. After purchasing, users leave ratings & reviews  
4. Naive Bayes classifier predicts sentiment based on review text  
5. System compares rating vs. sentiment → stored and visualized  

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/rohith66204/product-review-sentiment-analysis.git
cd productreview
pip install -r requirements.txt
python manage.py runserver 8000
