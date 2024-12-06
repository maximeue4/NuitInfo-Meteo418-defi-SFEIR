import datetime

def convertHeureTo24(heure):
    heure24 = int(heure.split(":")[0])+12
    minute = int(heure.split(":")[1])
    return f"{heure24}:{minute}"

def contructGraph(dataJson, day):
    value_graph_int = []
    for i in range(0, 8, 1):
        value_graph_int.append( int( dataJson["weather"][day]["hourly"][i]["chanceofrain"] ) )
    return str(value_graph_int)

def contructGraphSpeed(dataJson, day):
    value_graph_int = []
    for i in range(0, 8, 1):
        value_graph_int.append( int( dataJson["weather"][day]["hourly"][i]["windspeedKmph"] ) )
    return str(value_graph_int)

def contructGraphHumidity(dataJson, day):
    value_graph_int = []
    for i in range(0, 8, 1):
        value_graph_int.append( int( dataJson["weather"][day]["hourly"][i]["humidity"] ) )
    return str(value_graph_int)

def convertDateInDayWeek(dataJson, nextDay):
    date_str = dataJson['current_condition'][0]['localObsDateTime'].replace(" PM", "").replace(" AM", "")
    print("Date : ",date_str)
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    day_of_week = date.strftime("%A")

    days_in_number = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    days_in_french = {
        "Monday": "Lundi",
        "Tuesday": "Mardi",
        "Wednesday": "Mercredi",
        "Thursday": "Jeudi",
        "Friday": "Vendredi",
        "Saturday": "Samedi",
        "Sunday": "Dimanche"
    }

    number_day = days_in_number[day_of_week]

    number_day = (number_day + nextDay) % 7

    return days_in_french[list(days_in_number.keys())[number_day]]

def contient_mot(texte, mot):
    return mot in texte

def weather_logo(weather):
    if(contient_mot(weather, "Ensoleillé") or contient_mot(weather, "Temps clair")):
        return "sunny.png"
    if(contient_mot(weather, "Partiellement couvert") or contient_mot(weather, "Patchy rain nearby")):
        return "partly_cloudy.png"
    if(contient_mot(weather, "Nuageux")):
        return "cloudy.png"
    if(contient_mot(weather, "Couvert")):
        return "partly_cloudy.png"
    if(contient_mot(weather, "Pluie légère") or contient_mot(weather, "pluie") or contient_mot(weather, "Pluie") or contient_mot(weather, "Averses")):
        return "rain_light.png"
    if(contient_mot(weather, "Brouillard givrant") or contient_mot(weather, "Nappes de brouillard") or contient_mot(weather, "Bruine")):
        return "rain_s_cloudy.png"
    if(contient_mot(weather, "neige")):
        return "snow_light.png"
    return "nuage.png"
