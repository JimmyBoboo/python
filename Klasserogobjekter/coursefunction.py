def calculate_total_points(kurs):
    total_credits = 0
    for element in kurs:
        total_credits += element.credit
        return total_credits