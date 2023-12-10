class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create a dictionary to store the adjacency list of airports
        adj_list = defaultdict(list)

        # Populate the adjacency list
        for ticket in tickets:
            from_airport, to_airport = ticket
            adj_list[from_airport].append(to_airport)

        # Sort the destinations in lexicographical order
        for airport in adj_list:
            adj_list[airport].sort()

        # Initialize a list to store the itinerary
        itinerary = []

        # Define a DFS function to explore the airports
        def dfs(airport):
            nonlocal itinerary
            while adj_list[airport]:
                # Visit the smallest lexicographical airport first
                next_airport = adj_list[airport].pop(0)
                dfs(next_airport)
            itinerary.insert(0, airport)  # Insert the airport in reverse order

        # Start the DFS from "JFK"
        dfs("JFK")

        return itinerary