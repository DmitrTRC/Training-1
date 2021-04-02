def get_average(obj):
    s = sum(obj)
    avg = round(sum(obj) / len(obj), 2)
    return avg


temp_hall = [10, 12, 15, 14.2, 11, 9.5, 8.3]
temp_outside = [-20, -21, -34, -5, -7, -6.5, -8]
temp_body = [36.6, 36.7, 38.0, 38.3, 38.4, 37, 36.6]
print(get_average(temp_hall))
print(get_average(temp_outside))
print(get_average(temp_body))