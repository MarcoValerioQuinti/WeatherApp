from api import Api

class GetData():

    def __init__(self, city) -> None:
        self.data = Api.get_data(self, city)
        self.weather_data = self.data['consolidated_weather'][0]

    def title(self):
        title = self.data['title']
        return title
    
    def country(self):
        country = self.data['parent']['title']
        return country
    
    def sun_rise(self):
        sun_rise = self.data['sun_rise']
        return sun_rise
    
    def sun_set(self):
        sun_set = self.data['sun_set']
        return sun_set
    
    def time(self):
        time = self.data['time']
        return time
    
    def weather_state_name(self):
        weather_state_name = self.weather_data['weather_state_name']
        return weather_state_name
    
    def temp(self):
        temp = self.weather_data['the_temp']
        return temp

    def min_temp(self):
        min_temp = self.weather_data['min_temp']
        return min_temp
    
    def max_temp(self):
        max_temp = self.weather_data['max_temp']
        return max_temp

    def wind_speed(self):
        wind_speed = self.weather_data['wind_speed']
        return wind_speed
    
    def wind_direction(self):
        wind_direction = self.weather_data['wind_direction']
        return wind_direction
    
    def wind_direction_compass(self):
        wind_direction_compass = self.weather_data['wind_direction_compass']
        return wind_direction_compass
    
    def air_pressure(self):
        air_pressure = self.weather_data['air_pressure']
        return air_pressure
    
    def humidity(self):
        humidity = self.weather_data['humidity']
        return humidity