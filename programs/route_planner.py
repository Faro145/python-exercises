route = [8, 1, 4, 10, 6, 2, 11, 5, 3, 7, 9, 2]

def route_planner(route):
    routeplanner = [i for i in route if i < 7]
    return routeplanner
    
print("Best Route:")
print(route_planner(route))