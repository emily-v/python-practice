import unittest
from load_balancer import Server, LoadBalancer

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.server = Server()
        self.loadBalancer = LoadBalancer()

    def test_server_add(self):
        self.server.add_connection("192.168.1.1")
        self.assertTrue(len(self.server.connections) == 1)

    def test_server_close(self):
        self.server.close_connection("192.168.1.1")
        self.assertTrue(len(self.server.connections) == 0)

    def test_loadBalancer_add(self):
        self.loadBalancer.add_connection("fdca:83d2::f20d")
        self.assertTrue(len(self.loadBalancer.connections) == 1)
        self.assertTrue(len(self.loadBalancer.servers) == 1)

    def test_loadBalancer_avgAndAppend(self):
        avg = self.loadBalancer.avg_load()
        self.assertTrue(avg > 0)
        self.loadBalancer.servers.append(Server())
        newAvg = self.loadBalancer.avg_load()
        self.assertTrue(avg > newAvg)

    def test_loadBalancer_close(self):
        self.loadBalancer.close_connection("fdca:83d2::f20d")
        self.assertTrue(len(self.loadBalancer.connections) == 0)
        self.assertTrue(self.loadBalancer.avg_load() == 0)

    def test_loadBalancer_ensureAvailability(self):
        for connection in range(20):
            self.loadBalancer.add_connection(connection)
        self.assertTrue(self.loadBalancer.avg_load() < 50)

if __name__ == '__main__':
    unittest.main()