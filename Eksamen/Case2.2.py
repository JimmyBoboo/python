def create_car(car_register, brand, model, price, year, month, new, km):
    car_register[brand + model] = {
        "brand": brand,
        "Model": model,
        "Price": price,
        "year": year,
        "Month": month,
        "New": new,
        "km": km
    }
    return car_register

    
    