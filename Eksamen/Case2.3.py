from datetime import datetime
def get_car_age(year_lagd):
    naa_dagens_aar = datetime.now().year
    car_age = naa_dagens_aar - year_lagd
    return car_age
