import sys
import requests
from requests.exceptions import (
    Timeout, ConnectionError, HTTPError,
    TooManyRedirects, SSLError,
    ProxyError, InvalidURL,
    InvalidSchema, ChunkedEncodingError,
    RequestException
)
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QLineEdit, QPushButton, QVBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

load_dotenv()
API_KEY = os.getenv("API_KEY")


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Advanced Weather Application")
        self.setGeometry(600, 250, 460, 520)
        self.setStyleSheet("background-color: #1E1E2F;")

        self.init_ui()

    def init_ui(self):

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter City or City,Country (e.g. Delhi,IN)")
        self.city_input.setStyleSheet("""
            padding: 12px;
            font-size: 16px;
            border-radius: 8px;
            background-color: #2C2C3E;
            color: white;
        """)

        self.search_button = QPushButton("Get Weather")
        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #3A86FF;
                color: white;
                padding: 12px;
                font-size: 16px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #265DAB;
            }
        """)

        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setWordWrap(True)
        self.result_label.setFont(QFont("Arial", 13))
        self.result_label.setStyleSheet("color: white; margin-top: 20px;")

        layout = QVBoxLayout()
        layout.addWidget(self.city_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        self.search_button.clicked.connect(self.get_weather)

    def get_weather_emoji(self, weather_id):
        if 200 <= weather_id <= 232:
            return "⛈ Thunderstorm"
        elif 300 <= weather_id <= 321:
            return "🌦 Drizzle"
        elif 500 <= weather_id <= 531:
            return "🌧 Rain"
        elif 600 <= weather_id <= 622:
            return "❄ Snow"
        elif 700 <= weather_id <= 781:
            return "🌫 Atmosphere"
        elif weather_id == 800:
            return "☀ Clear Sky"
        elif 801 <= weather_id <= 804:
            return "☁ Clouds"
        else:
            return "🌍 Unknown"

    def get_weather(self):

        if not API_KEY or API_KEY == "YOUR_NEW_API_KEY":
            self.result_label.setText("🔑 Invalid API Key.")
            return

        city = self.city_input.text().strip()

        if not city:
            self.result_label.setText("⚠ Please enter a city name.")
            return

        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        try:
            response = requests.get(url, timeout=10)

            # -------- HTTP STATUS HANDLING --------
            if response.status_code == 400:
                self.result_label.setText("❌ 400 Bad Request.")
                return

            elif response.status_code == 401:
                self.result_label.setText("🔑 401 Unauthorized (Invalid API key).")
                return

            elif response.status_code == 403:
                self.result_label.setText("⛔ 403 Forbidden (Access denied).")
                return

            elif response.status_code == 404:
                self.result_label.setText("🌍 404 City Not Found.")
                return

            elif response.status_code == 500:
                self.result_label.setText("🔥 500 Internal Server Error.")
                return

            elif response.status_code == 502:
                self.result_label.setText("🌐 502 Bad Gateway.")
                return

            elif response.status_code == 503:
                self.result_label.setText("⏳ 503 Service Unavailable.")
                return

            elif response.status_code == 504:
                self.result_label.setText("⏱ 504 Gateway Timeout.")
                return

            response.raise_for_status()

            data = response.json()

            city_name = data.get("name", "N/A")
            country = data.get("sys", {}).get("country", "N/A")
            main = data.get("main", {})
            weather = data.get("weather", [{}])[0]
            wind = data.get("wind", {})

            weather_text = (
                f"🌍 Location: {city_name}, {country}\n\n"
                f"🌡 Temperature: {main.get('temp', 'N/A')} °C\n"
                f"🤒 Feels Like: {main.get('feels_like', 'N/A')} °C\n"
                f"💧 Humidity: {main.get('humidity', 'N/A')}%\n"
                f"🧭 Pressure: {main.get('pressure', 'N/A')} hPa\n"
                f"🌬 Wind Speed: {wind.get('speed', 'N/A')} m/s\n"
                f"☁ Condition: {weather.get('description', 'N/A').title()}"
            )

            self.result_label.setText(weather_text)

        # -------- CONNECTION / NETWORK ERRORS --------
        except Timeout:
            self.result_label.setText("⏳ Request timed out.")

        except ConnectionError:
            self.result_label.setText("🌐 Connection error. Check internet.")

        except HTTPError:
            self.result_label.setText("⚠ HTTP error occurred.")

        except TooManyRedirects:
            self.result_label.setText("🔄 Too many redirects.")

        except SSLError:
            self.result_label.setText("🔒 SSL certificate error.")

        except ProxyError:
            self.result_label.setText("🌐 Proxy error.")

        except InvalidURL:
            self.result_label.setText("❌ Invalid URL.")

        except InvalidSchema:
            self.result_label.setText("⚠ Invalid URL schema.")

        except ChunkedEncodingError:
            self.result_label.setText("⚠ Chunked encoding error.")

        except requests.exceptions.JSONDecodeError:
            self.result_label.setText("⚠ Failed to decode JSON.")

        except RequestException:
            self.result_label.setText("⚠ General request exception.")

        except Exception as e:
            self.result_label.setText(f"⚠ Unexpected Error:\n{str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())