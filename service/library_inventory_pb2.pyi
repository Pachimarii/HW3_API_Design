from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Book(_message.Message):
    __slots__ = ["author", "genre", "isbn", "publishingYear", "title"]
    class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    BIOGRAPHY: Book.Genre
    FICTION: Book.Genre
    GENRE_FIELD_NUMBER: _ClassVar[int]
    HISTORY: Book.Genre
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TRAVEL: Book.Genre
    author: str
    genre: Book.Genre
    isbn: str
    publishingYear: int
    title: str
    def __init__(self, isbn: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., publishingYear: _Optional[int] = ..., genre: _Optional[_Union[Book.Genre, str]] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["inventoryNumber", "oneOf", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AVAILABLE: InventoryItem.Status
    INVENTORYNUMBER_FIELD_NUMBER: _ClassVar[int]
    ONEOF_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAKEN: InventoryItem.Status
    inventoryNumber: int
    oneOf: Book
    status: InventoryItem.Status
    def __init__(self, inventoryNumber: _Optional[int] = ..., oneOf: _Optional[_Union[Book, _Mapping]] = ..., status: _Optional[_Union[InventoryItem.Status, str]] = ...) -> None: ...
