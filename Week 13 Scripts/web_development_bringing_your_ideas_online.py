# Using Flask: A lightweight web framework
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Display the homepage."""
    return render_template('index.html', title='Weather App')

@app.route('/forecast/<city>')
def forecast(city):
    """Show weather forecast for a specific city."""
    # Get weather data (simplified example)
    weather_data = get_weather(city)
    return render_template('forecast.html', 
                          city=city, 
                          forecast=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
