#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    route = [None] * length
    locations = {}

    for ticket in tickets:
        locations[ticket.source] = ticket.destination
    next = locations["NONE"]

    for i in range(0, length):
        route[i] = next
        next = locations[next]
    return route
