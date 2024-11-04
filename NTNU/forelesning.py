def write_data(weather_Data, filename):
    weather_Data = weather_Data.copy()
    with open (filename, "w") as file:
        for line in weather_Data:
            
            file.write