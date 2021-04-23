# 1436. Destination City
# Easy

# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        # create a map where key,value = source, destination.
        # iterate over destinations
        # if destination is not a key in map, return destination.

        routes = {}

        for i in paths:
            routes[i[0]] = i[1]

        for start, stop in paths:
            if stop not in routes:
                return stop
