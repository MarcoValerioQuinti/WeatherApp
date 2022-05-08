from data import GetData

# data = GetData.get_data()

# GetData.jprint(data)

def start():
    city = input("Di quale città vorresti vedere il meteo?: ")
    print('Caricamento...')
    weather = GetData(city)
    message = f"""
    Meteo {weather.title()} in {weather.country()}:
        Temperatura: {weather.temp()}°C
        Massima: {weather.max_temp()}°C
        Minima: {weather.min_temp()}°C
        Vento: {weather.wind_speed()} knots
        Direzione del vento: {weather.wind_direction_compass()}
        Stato: {weather.weather_state_name()}
        Pressione: {weather.air_pressure()} hPa
        Alba: {weather.sun_rise()}
        Tramonto: {weather.sun_set()}
    """
    print(message)

if __name__ == "__main__":
    start()