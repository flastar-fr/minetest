""" MinetestClient File """

import socket


class MinetestClient:
    """ Class manager of server's requests
        :attr socket: socket object -> connection to server
    """
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to(self, ip: str, port: int):
        """ Method to connect into the server adress
            :param ip: str -> server ip to connect
            :param port: int -> port to use to connect into the server
        """
        self.socket.connect((ip, port))

    def disconnect(self):
        """ Method to disconnect the server """
        self.socket.close()

    def chat_post(self, message: str):
        """ Method to send a server message
            :param message: str -> message to send
        """
        requete = f"chat.post({message})\n"
        self.socket.send(requete.encode())

    def world_set_block(self, x: int, y: int, z: int, block_id: int, block_data: int = 1):
        """ Method to set a block into the world
            :param x: int -> x coordinate to set
            :param y: int -> y coordinate to set
            :param z: int -> z coordinate to set
            :param block_id: int -> block to set based from its id
            :param block_data: int -> block data to set for the block
        """
        requete = f"world.setBlock({x}, {y}, {z}, {block_id}, {block_data})\n"
        self.socket.send(requete.encode())

    def world_set_blocks(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int,
                         block_id: int, block_data: int = 1):
        """ Method to set blocs into the world
            :param x1: int -> first x coordinate to set
            :param y1: int -> first y coordinate to set
            :param z1: int -> first z coordinate to set
            :param x2: int -> second x coordinate to set
            :param y2: int -> second y coordinate to set
            :param z2: int -> second z coordinate to set
            :param block_id: int -> block to set based from its id
            :param block_data: int -> block data to set for the block
        """
        requete = f"world.setBlocks({x1}, {y1}, {z1}, {x2}, {y2}, {z2}, {block_id}, {block_data})\n"
        self.socket.send(requete.encode())

    def world_destroy_block(self, x: int, y: int, z: int):
        """ Method to destroy a block in the world (set as air)
            :param x: int -> x coordinate to set
            :param y: int -> y coordinate to set
            :param z: int -> z coordinate to set
        """
        self.world_set_block(x, y, z, 0, 0)

    def world_destroy_blocks(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int):
        """ Method to destroy blocks in the world
            :param x1: int -> first x coordinate to set
            :param y1: int -> first y coordinate to set
            :param z1: int -> first z coordinate to set
            :param x2: int -> second x coordinate to set
            :param y2: int -> second y coordinate to set
            :param z2: int -> second z coordinate to set
        """
        self.world_set_blocks(x1, y1, z1, x2, y2, z2, 0, 0)
