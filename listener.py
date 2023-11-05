#message listener

import redis

import json

import logging

import message as msg

class Listener:
    """Listener for messages in a chat room."""
    
    def __init__(self, room: str,  port: int = 6379, host: str = 'localhost', debug: bool = False) -> None:
        self.room: str = room

        self.debug: bool = debug

        self.server : redis.Redis.PubSub = redis.Redis(host=host, port=port, decode_responses=True).pubsub()

        self.server.subscribe(room)
        
        if self.debug:
            logging.basicConfig(level=logging.DEBUG)
            logging.debug(f'Debug logging active.')

        while True:
            stream_data = self.server.get_message()

            #need to check if data exists and if it is a string.
            if stream_data and type(stream_data['data']) == str:
                try:
                    print(msg.Message.deserialize(stream_data['data']))
                    if self.debug:
                        logging.debug(f'Message recieved: \"{stream_data["data"]}\"')

                #just ignore bad message, output in debug log
                except json.JSONDecodeError:
                    logging.debug(f'Bad message recieved: \"{stream_data["data"]}\"')



