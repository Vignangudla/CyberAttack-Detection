Toward Detection and Attribution of Cyber Attacks

📖 Project Overview:
This project is a Django-based web application that demonstrates how to detect, classify, and analyze cyber attacks using machine learning. It integrates a user interface for remote users (to test attack prediction) and a service provider interface (to train models, view analytics, and manage datasets).
The application leverages a labeled dataset of network traffic (IOT_Cyber_Attacks.csv, Labled_Data.csv) to train a machine learning model that can classify various attack types such as:
DoS (Denial of Service)
Probe / Reconnaissance
R2L (Remote to Local)
U2R (User to Root)
Normal traffic
It also includes data visualization, reporting, and ratio/chart analysis to give insights into attack trends.

✨ Features

User Authentication & Registration
Remote users can register and log in to test the system.
Cyber Attack Prediction
Input: source IP, destination IP, and traffic/attack details.
Output: predicted attack type based on trained ML models.
Service Provider Portal
Upload datasets.
Train ML model on provided datasets.
View ratio of attack types.
Generate charts and visualizations (accuracy, ratios, likes).
Download trained datasets.
Visualization & Reports
Matplotlib/Seaborn plots.
Excel/CSV export (via openpyxl and xlwt).

Database
Uses MySQL for persistent storage.
Tracks users, predictions, datasets, and analytics.



⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/<your-username>/CyberAttack-Detection.git
cd CyberAttack-Detection

2. Create Virtual Environment & Install Requirements
python -m venv venv
venv\Scripts\activate   # (Windows)
# or: source venv/bin/activate (Linux/Mac)

pip install -r requirements.txt

3. Configure MySQL Database

Ensure MySQL is installed and running.

Create the database:

CREATE DATABASE toward_detection_and_attribution_of_cyberattacks;


Import schema (Windows example):

"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p toward_detection_and_attribution_of_cyberattacks < Database\toward_detection_and_attribution_of_cyberattacks.sql


Update settings.py with your MySQL username & password:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'toward_detection_and_attribution_of_cyberattacks',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

4. Run Migrations
python manage.py makemigrations
python manage.py migrate

5. Start Development Server
python manage.py runserver


Visit: http://127.0.0.1:8000/

🚀 Usage Flow
Remote User (Frontend)

Register a new user → /Register1/.
Log in → /.
Test cyber attack prediction → /Predict_Cyber_Attack_Type/.
Service Provider (Backend Portal)
Log in → /serviceproviderlogin/.
Train model on dataset → /train_model/.
View prediction results → /View_Prediction_Of_Cyber_Attack_Type/.
Check attack ratio → /View_Cyber_Attack_Type_Ratio/.
View charts → /charts/, /charts1/, /likeschart/.
Download trained datasets → /Download_Trained_DataSets/.

🛠️ Dependencies
All dependencies are listed in requirements.txt and include:
Django
MySQL client (mysqlclient / PyMySQL)
scikit-learn, numpy, pandas
matplotlib, seaborn
openpyxl, xlwt
Install all with:
pip install -r requirements.txt
