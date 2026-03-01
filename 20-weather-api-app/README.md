# 🌦 Advanced Weather API App (PyQt5 GUI)

A modern graphical weather application built using Python, PyQt5, and OpenWeatherMap API.

---

## 📌 Description

This application allows users to:

- Enter a city name
- Fetch real-time weather data
- Display temperature, humidity, wind speed, pressure
- Handle HTTP errors gracefully
- Show formatted results in a styled GUI

---

## 🚀 Features

- Real-time API integration
- Secure API key handling using `.env`
- Advanced HTTP status handling
- JSON parsing
- Styled modern UI
- Robust exception handling

---

## 🛠 Technologies Used

- Python
- PyQt5 (GUI)
- Requests (API calls)
- python-dotenv (Environment variables)
- REST API (OpenWeatherMap)

---

## 🔐 API Setup

1. Get a free API key from:
   https://openweathermap.org/

2. Create a `.env` file in the project directory:

```
API_KEY=your_api_key_here
```

⚠ Do NOT upload `.env` to GitHub.

---

## 📦 Installation

```
pip install -r requirements.txt
```

---

## ▶ How to Run

```
python main.py
```

Enter city name in the input box and click **Get Weather**.

---

## 💡 Example Output

🌍 Location: Delhi, IN  
🌡 Temperature: 32 °C  
💧 Humidity: 45%  
🌬 Wind Speed: 10 m/s  

---

## 🚀 Project Level

Advanced Beginner to Intermediate – Demonstrates GUI development, API integration, secure key management, JSON handling, and robust error handling.

---

## 📁 Project Structure

```
20-weather-api-app/
│
├── main.py
├── requirements.txt
├── .env   (not pushed to GitHub)
└── README.md
```