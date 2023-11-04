#message and related functions.

import datetime as dt

import json

import typing as ty

MessageType = ty.TypeVar("MessageType", bound="Message")

class Message:
    """Class for all data related to a given message."""

    def __init__(self, msg_content: str, timestamp: dt.datetime=dt.datetime.today()) -> None:
        self.timestamp: dt.datetime = timestamp
        self.msg_content: str = msg_content

    @classmethod
    def deserialize(cls, msg_json: str) -> MessageType:
        """Get message from JSON encoded-string."""
        return cls(**json.loads(msg_json))

    def serialize(self) -> str:
        """Serialize message as JSON-encoded string."""
        return json.dumps({ 'timestamp': self.timestamp.isoformat()
                          , 'msg_content': self.msg_content
                          })

    def __str__(self) -> str:
        return f'"{self.msg_content}" @ {self.timestamp}'
