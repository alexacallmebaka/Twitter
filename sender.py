#message sender

import redis

import logging

import message as msg

class Sender:

    def __init__(self, room: str,  author: str, port: int = 6379, host: str = 'localhost', debug: bool = False) -> None:
        self.room: str = room

        self.author: str = author

        self.debug: bool = debug

        self.server: redis.Redis = redis.Redis(host=host, port=port, decode_responses=True)

        if self.debug:
            logging.basicConfig(level=logging.DEBUG)
            logging.debug(f'Debug logging active.')

    def send_message(self, msg_content: str) -> bool:
        try:
            out_msg = msg.Message(msg_content, self.author).serialize()
            self.server.publish(self.room, out_msg)
            if self.debug:
                logging.debug(f'Message sent: \"{msg_content}\"')
            return True
        except Exception as err:
            logging.error(f'{err}')
            return False

     
