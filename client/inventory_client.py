import grpc
import os
import sys
sys.path.append(os.path.dirname(__file__) + '/..')
sys.path.append(os.path.dirname(__file__) + '/../service')
from service import inventory_service_pb2, inventory_service_pb2_grpc

class InventoryClient:
    port = None

    def __init__(self, port) -> None:
        self.port = port

    def getBooks(self, isbns) -> list:
        res = []
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = inventory_service_pb2_grpc.InventoryServiceStub(channel)
            for isbn in isbns:
                response = stub.GetBook(inventory_service_pb2.GetBookRequest(isbn=isbn))
                res.append(response.book.title)
        return res
