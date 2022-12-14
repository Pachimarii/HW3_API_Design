import library_inventory_pb2 as _library_inventory_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBookRequest(_message.Message):
    __slots__ = ["book"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: _library_inventory_pb2.Book
    def __init__(self, book: _Optional[_Union[_library_inventory_pb2.Book, _Mapping]] = ...) -> None: ...

class CreateBookResponse(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: bool
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["isbn"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    isbn: str
    def __init__(self, isbn: _Optional[str] = ...) -> None: ...

class GetBookResponse(_message.Message):
    __slots__ = ["book", "message", "status"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    book: _library_inventory_pb2.Book
    message: str
    status: bool
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., book: _Optional[_Union[_library_inventory_pb2.Book, _Mapping]] = ...) -> None: ...
