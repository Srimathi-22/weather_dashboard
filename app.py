from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "319a0d7d6907e6da8eaad449b925d473"
BASE_URL = "http://api.openweathermap.org/data/2.5/"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    forecast = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        
        # Current weather
        current_url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
        current_response = requests.get(current_url)
        
        if current_response.status_code == 200:
            weather = current_response.json()
            
            # 5 day forecast
            forecast_url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
            forecast_response = requests.get(forecast_url)
            forecast = forecast_response.json()
        else:
            error = "City not found! Try again."

    return render_template("index.html", weather=weather, forecast=forecast, error=error, city=city if request.method == "POST" else "")

if __name__ == "__main__":
    app.run(debug=True)