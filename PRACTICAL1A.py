import queue as Q
from RMP import dict_gn

start = 'Arad'
goal = 'Bucharest'
result = ''

def BFS(city, cityq, visitedq):
    global result
    if city == start:
        result += city

    for eachcity in dict_gn[city].keys():
        if eachcity == goal:
            result += ' -> ' + eachcity
            return
        if eachcity not in cityq.queue and eachcity not in visitedq.queue:
            cityq.put(eachcity)
            result += ' -> ' + eachcity

    visitedq.put(city)
    
    if not cityq.empty():
        BFS(cityq.get(), cityq, visitedq)

def main():
    cityq = Q.Queue()
    visitedq = Q.Queue()
    BFS(start, cityq, visitedq)
    print(f"Path from {start} to {goal}:")
    print(result)

main()
