# liver-disease-prediction-using-ai-and-ml




Project: Liver Disease Prediction Web Application
🔹 1. Introduction & Problem Statement 

“My project is Liver Disease Prediction using Artificial Intelligence and Machine Learning, implemented as a web application using Django.
Liver disease is a serious health issue, and early diagnosis is very important.
The main objective of this project is to predict whether a patient has liver disease based on medical parameters and present the results through a user-friendly web interface.”

🔹 2. Overall Architecture

“The project follows a full-stack architecture consisting of:

Frontend using HTML, CSS, and JavaScript

Backend using Django

Database using MongoDB

Machine Learning models using Python

All these components work together to provide real-time liver disease prediction.”

🔹 3. Frontend – HTML Templates 

“The frontend is built using HTML, CSS, and JavaScript and implemented as Django templates.
The project contains 24 HTML files, mainly inside the app and users template folders.”

Important HTML Files:

index.html – main landing page

chatbot.html – AI chatbot interface

Basic_report.html – displays basic prediction report

Ml_output.html – shows machine learning results

Database.html – database-related views

9_Deploy.html – deployment and real-time prediction page

User authentication pages like:

login.html

register.html

profile.html

“These HTML files use Django template tags like {% load static %} and {% url %} to dynamically connect static files and backend URLs.”

🔹 4. CSS – Styling & User Interface 

“For styling, the project uses 26 CSS files, including custom styles and third-party libraries.”

Key CSS Files:

style.css – main custom stylesheet

bootstrap.min.css – responsive design

main.css – modern UI styling

Role of CSS:

Styling forms, buttons, tables, and reports

Responsive design for mobile, tablet, and desktop

Layout management using Flexbox/Grid

Animations and hover effects

Overriding Bootstrap styles for consistent theme

“CSS improves usability and makes the application visually professional.”

🔹 5. JavaScript – Client-Side Functionality 

“JavaScript is used for client-side logic and interactivity.
There are 26 JavaScript files in the project.”

Important JS Files:

custom.js – handles form submission, prediction logic, and UI updates

jquery-2.1.1.js – DOM manipulation

bootstrap.min.js – interactive UI components

main.js – animations and page effects

Role of JavaScript:

Client-side form validation

Sending data to backend

Displaying prediction results dynamically

Enhancing user experience

🔹 6. Backend – Django Framework 

“The backend is developed using Django, a Python web framework.
Django manages routing, business logic, and communication between frontend, database, and machine learning models.”

Backend Responsibilities:

Handling HTTP requests and responses

User authentication and authorization

Processing patient input data

Connecting frontend with ML models

Storing and retrieving data from MongoDB

“Django templates are used to render HTML pages dynamically.”

🔹 7. Database – MongoDB 

“For the database, I used MongoDB, which is a NoSQL document-based database.”

Why MongoDB?

Flexible schema

Stores data in JSON-like documents

Easy integration with backend

Data Stored:

User details

Patient medical data

Prediction results and history

🔹 8. Machine Learning & Python 

“Machine learning is implemented using Python.
I used Pandas and NumPy for data preprocessing and numerical operations.”

ML Algorithms Used:

Support Vector Machine (SVM)

Extra Trees Classifier

CatBoost

Neural Network (experimental)

“Different models were trained and evaluated, and the best-performing model was selected for prediction.”

🔹 9. Model Saving & Deployment 

“The trained machine learning model is saved using Pickle, which allows the model to be reused during deployment without retraining.”

“The final deployment happens through 9_Deploy.html, where users enter patient data and receive real-time prediction results.”

🔹 10. Working Flow 

“User enters medical data → frontend sends data to Django backend → ML model predicts liver disease → result is stored in MongoDB → output is displayed on the web page.”

🔹 11. Conclusion & Importance 

“This project integrates web development, machine learning, and database technologies into a complete healthcare solution.
It demonstrates how AI can be applied in the medical field for early disease prediction, which can help in timely treatment and better decision-making.”

⭐ Strong Ending Line (Optional)

“This project demonstrates an end-to-end implementation from data prediction to web deployment using Django.”
