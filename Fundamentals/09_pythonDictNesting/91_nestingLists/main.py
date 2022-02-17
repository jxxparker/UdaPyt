# listDict = {
#     Key: [List]
#     Key2: {Dict}
# }

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    }

#nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Liille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# ["A", "B", ["C", "D"]] #useless

travel_log2 = {
    "France": 
    {"cities_visited" : ["Paris", "Liille", "Dijon"],
     "total_visits": 12},
    
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}