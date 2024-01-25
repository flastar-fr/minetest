import socket


class MinetestClient:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to(self, ip: str, port: int):
        self.socket.connect((ip, port))

    def disconnect(self):
        self.socket.close()

    def chat_post(self, message: str):
        requete = f"chat.post({message})\n"
        self.socket.send(requete.encode())

    def world_set_block(self, x: int, y: int, z: int, block_id: int, block_data: int = 1):
        requete = f"world.setBlock({x}, {y}, {z}, {block_id}, {block_data})\n"
        self.socket.send(requete.encode())

    def world_set_blocks(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int,
                         block_id: int, block_data: int = 1):
        requete = f"world.setBlocks({x1}, {y1}, {z1}, {x2}, {y2}, {z2}, {block_id}, {block_data})\n"
        self.socket.send(requete.encode())

    def world_destroy_block(self, x: int, y: int, z: int):
        requete = f"world.setBlock({x}, {y}, {z}, 0, 0)\n"
        self.socket.send(requete.encode())

    def world_destroy_blocks(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int):
        requete = f"world.setBlocks({x1}, {y1}, {z1}, {x2}, {y2}, {z2}, 0, 0)\n"
        self.socket.send(requete.encode())
