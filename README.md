# ExpenseTracker

Expense Tracker project:

Expense Tracker API 💰📊

A simple Expense Tracker API built with Flask, MongoDB, and JWT Authentication. This API allows users to register, log in, add expenses, and retrieve expenses securely.

🚀 Features

✅ User Registration & Login (with JWT Authentication)
✅ Secure Token-based Authentication
✅ Add & Retrieve Expenses
✅ MongoDB as Database
✅ CORS-enabled for frontend integration
✅ Deployable on Render

🛠️ Tech Stack
	•	Backend: Flask
	•	Database: MongoDB
	•	Authentication: JWT
	•	Hosting: Render

📦 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/username/ExpenseTracker.git
cd ExpenseTracker

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Up Environment Variables

Create a .env file in the root directory and add:

MONGO_URI=mongodb+srv://username:your_password@your_cluster.mongodb.net/ExpenseTracker
JWT_SECRET_KEY=secret_key

4️⃣ Run the Application

python main.py

Your API will be running at:
👉 http://127.0.0.1:8080/

🔗 API Endpoints

Method	Endpoint	Description	Auth Required?
POST	/register	Register a new user	❌ No
POST	/login	User login (returns token)	❌ No
POST	/add-expense	Add a new expense	✅ Yes
GET	/get-expenses	Get all user expenses	✅ Yes

🚀 Deploying to Render
	1.	Push your code to GitHub.
	2.	Go to Render → New Web Service.
	3.	Connect your repository.
	4.	Set the Start Command as:

gunicorn main:app


	5.	Add Environment Variables (MONGO_URI, JWT_SECRET_KEY).
	6.	Deploy & get your live API URL! 🌍

🎯 Future Improvements
	•	📊 Add Data Visualization (Graphs & Charts)
	•	🏷️ Add Category-based Expense Filtering
	•	📆 Add Expense Date Filters
	•	📱 Build a React Frontend for UI

👨‍💻 Author

👤 Sivaprasad Ponduru
🔗 https://github.com/evennumber2
