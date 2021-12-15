# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
#
# student_grades = {}
# for grade in student_scores:
#     if  student_scores[grade] in range(91, 101):
#         student_scores[grade] = "Outstanding"
#     elif student_scores[grade] in range (81, 91):
#         student_scores[grade] = " Exceeds Expectations"
#     elif student_scores[grade] in range (71, 81):
#         student_scores[grade] = "Acceptable"
#     else:
#         student_scores[grade] = "Fail"
#
# print(student_scores)
# travel_log =[
#     {"country": "France",
#      "cities_visited": ["Paris", "Lille", "Dijon"],
#      "Total_visits": 17
#      },
#     {"country": "Germany",
#      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#      "Total_visits": 12
#      },
# ]
# def add_new_country(country_visted, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visted
#     new_country["Visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)
#
# add_new_country ("Russia", 12, ["Moscow", "Stuttgart"])
# print(travel_log)
from os import system, name
def clear():
    if name == "nt":
        _ = system("cls")

print("Welcome to the secret auction Program")

bid_list = {}
bidding_finished = False


def find_highest_bidder(bid_list):
    winner = ""
    highest_bid = 0
    for bidder in bid_list:
        bid_amount = bid_list[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount  
            winner = bidder
    print(f"The highest bidder is {winner} with a bid of {highest_bid}")


while  not bidding_finished:
    name = input("What is your name? \n")
    bid = int(input("Whats your bid \n"))
    bid_list[name] = bid
    continue_bidding = input("Any other bidders? \n")
    if continue_bidding == "no":
        bidding_finished = True
        find_highest_bidder(bid_list)
    elif continue_bidding == "Yes":
        clear()







