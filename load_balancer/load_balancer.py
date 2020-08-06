import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        self.connections.pop(connection_id)

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        for connection in self.connections.values():
            total += connection
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

class LoadBalancer:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        self.connections[connection_id] = server
        server.add_connection(connection_id)
        self.ensure_availability()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        for server in self.servers:
            for connection in server.connections:
                if connection == connection_id:
                    server.close_connection(connection_id)
                    self.connections.pop(connection_id)
                    return

    def avg_load(self):
        """Calculates the average load of all servers"""
        total = 0
        for server in self.servers:
            total += server.load()
        return total / len(self.servers)

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
