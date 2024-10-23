import queue as Q
from RMP import dict_gn

start = 'Arad'
goal = 'Bucharest'
result = ''

def DLS(city, visitedstack, startlimit, endlimit):
    global result
    result += city + ' '
    visitedstack.append(city)
    
    if city == goal:
        return True
    
    if startlimit == endlimit:
        return False
    
    for eachcity in dict_gn[city].keys():
        if eachcity not in visitedstack:
            found = DLS(eachcity, visitedstack, startlimit + 1, endlimit)
            if found:
                return found
    return False

def IDDFS(city, visitedstack, endlimit):
    global result
    for i in range(0, endlimit + 1):
        print("Searching at limit:", i)
        found = DLS(city, visitedstack, 0, i)
        
        if found:
            print("Found")
            break
        else:
            print("Not found")
            print(result)
            print("---")
            result = ''
            visitedstack.clear()

def main():
    visitedstack = []
    IDDFS(start, visitedstack, 9)
    print("IDDFS Traversal from", start, "to", goal, "is:")
    print(result)

main()
