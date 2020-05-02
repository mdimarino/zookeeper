# put your python code here

duration_in_days = int(input())
daily_food_cost = int(input())
one_flight_cost = int(input())
daily_hotel_cost = int(input())

print((daily_food_cost * duration_in_days) + (one_flight_cost * 2) + (daily_hotel_cost * (duration_in_days - 1)))
