from flask import Flask, render_template, send_from_directory, redirect, url_for
import requests, json, lib

app = Flask(__name__)

@app.route('/')
def home():
    # Ville par défault lorsque qu'on arrive sur le site web
    return redirect(url_for('index', country='Paris'))

@app.route('/<country>')
def index(country):
    r = requests.get(f"https://wttr.in/{country}?format=j1&lang=fr")
    dataJson = json.loads(r.text)
    if(dataJson["nearest_area"][0]["areaName"][0]["value"]== "Ban Not"):
        return "Erreur 404"

    temperature = dataJson["current_condition"][0]["temp_C"]
    humidite = dataJson["current_condition"][0]["humidity"]
    weather = dataJson["current_condition"][0]["lang_fr"][0]["value"]
    windspeed = dataJson["current_condition"][0]["windspeedKmph"]
    precipitations = dataJson["current_condition"][0]["precipMM"].split(".")[0] # Récupérer nombre avant la virgule
    teeling_temperature = dataJson["current_condition"][0]["FeelsLikeC"]
    sun_open = dataJson["weather"][0]["astronomy"][0]["sunrise"].replace(" AM", "")
    sun_close = lib.convertHeureTo24(dataJson["weather"][0]["astronomy"][0]["sunset"].replace(" PM", ""))

    value_graph_today = lib.contructGraph(dataJson,0)
    value_graph_tomorrow = lib.contructGraph(dataJson,1)
    value_graph_after_tomorrow = lib.contructGraph(dataJson,2)

    value_graphSpeed_today = lib.contructGraphSpeed(dataJson,0)
    value_graphSpeed_tomorrow = lib.contructGraphSpeed(dataJson,1)
    value_graphSpeed_after_tomorrow = lib.contructGraphSpeed(dataJson,2)

    value_graphHumidity_today = lib.contructGraphHumidity(dataJson,0)
    value_graphHumidity_tomorrow = lib.contructGraphHumidity(dataJson,1)
    value_graphHumidity_after_tomorrow = lib.contructGraphHumidity(dataJson,2)

    name_of_today = lib.convertDateInDayWeek(dataJson, 0)
    name_of_tomorrow = lib.convertDateInDayWeek(dataJson, 1)
    name_of_after_tomorrow = lib.convertDateInDayWeek(dataJson, 2)

    weather_logo = lib.weather_logo(weather)

    return render_template('index.html',
        country=country,
        temperature=temperature,
        humidite=humidite,
        weather=weather,
        windspeed=windspeed,
        precipitations=precipitations,
        teeling_temperature=teeling_temperature,
        sun_open=sun_open,
        sun_close=sun_close,
        value_graph_today=value_graph_today,
        value_graph_tomorrow=value_graph_tomorrow,
        value_graph_after_tomorrow=value_graph_after_tomorrow,
        name_of_today=name_of_today,
        name_of_tomorrow=name_of_tomorrow,
        name_of_after_tomorrow=name_of_after_tomorrow,
        value_graphSpeed_today=value_graphSpeed_today,
        value_graphSpeed_tomorrow=value_graphSpeed_tomorrow,
        value_graphSpeed_after_tomorrow=value_graphSpeed_after_tomorrow,
        value_graphHumidity_today=value_graphHumidity_today,
        value_graphHumidity_tomorrow=value_graphHumidity_tomorrow,
        value_graphHumidity_after_tomorrow=value_graphHumidity_after_tomorrow,
        weather_logo=weather_logo
    )

@app.route('/script.js')
def script():
    return send_from_directory('javascript', 'script.js')

@app.route('/style.css')
def style():
    return send_from_directory('css', 'style.css')

@app.route('/nuage.png')
def nuage():
    return send_from_directory('images', 'nuage.png')

@app.route('/search.png')
def search():
    return send_from_directory('images', 'search.png')

@app.route('/sunny.png')
def sunny():
    return send_from_directory('images', 'sunny.png')

@app.route('/partly_cloudy.png')
def partly_cloudy():
    return send_from_directory('images', 'partly_cloudy.png')

@app.route('/cloudy.png')
def cloudy():
    return send_from_directory('images', 'cloudy.png')

@app.route('/rain_light.png')
def rain_light():
    return send_from_directory('images', 'rain_light.png')

@app.route('/rain_s_cloudy.png')
def rain_s_cloudy():
    return send_from_directory('images', 'rain_s_cloudy.png')

@app.route('/snow_light.png')
def snow_light():
    return send_from_directory('images', 'snow_light.png')

@app.route('/cloud_video.mp4')
def cloud_video():
    return send_from_directory('videos', 'cloud_video.mp4')

if __name__ == '__main__':
    app.run(debug=True)
