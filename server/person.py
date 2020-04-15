class Person:
    def __init__(self, addr, name, client):
        self.addr = addr
        self.name = name
        self.client = client

    def __repr__(self):
        return f"Person({self.addr}, {self.name})"

    def __str__(self):
        return f"Person({self.addr}, {self.name})"