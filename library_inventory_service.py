from concurrent import futures
import logging
import grpc

from service import inventory_service_pb2
from service import inventory_service_pb2_grpc

class LibraryInventoryService(inventory_service_pb2_grpc.InventoryService):
    # dictionary that stores the books
    lib = {
        "N10000": {
            "author": "Yuki",
            "genre": "BIOGRAPHY",
            "isbn": "N10000",
            "publishingYear": 1997,
            "title": "Yuki's Bio"
        },
        "N20000": {
            "author": "Lizzu",
            "genre": "FICTION",
            "isbn": "N20000",
            "publishingYear": 2000,
            "title": "How To Get An A In API Design"
        }
    }

    # create a book by providing necessary information that exists in a book 
    def CreateBook(self, request, context):
        isbn = request.book.isbn
        title = request.book.title
        publishingYear = request.book.publishingYear
        # validate required values
        if (isbn == "" or title == "" or publishingYear == 0):
            return inventory_service_pb2.CreateBookResponse(status=False, message="Failed to create a book with empty required field(s).")
        # validate if year is a valid number 
        if (publishingYear <= 0 or publishingYear > 2022):
            return inventory_service_pb2.CreateBookResponse(status=False, message="Failed to create a book with invalid publishing year.")
        # validate if isbn already exists
        if (self.lib.get(isbn)):
            return inventory_service_pb2.CreateBookResponse(status=False, message="Failed to create a book with existed isbn.")
        # add book to the dictionary library
        self.lib[isbn] = {
            "author": request.book.author,
            "genre": request.book.genre,
            "isbn": isbn,
            "publishingYear": publishingYear,
            "title": title
        }
        return inventory_service_pb2.CreateBookResponse(status=True, message="The book is successfully created.")

    def GetBook(self, request, context):
        isbn = request.isbn
        result = self.lib.get(isbn)
        # validate if isbn exists in the library
        if (not result):
            return inventory_service_pb2.GetBookResponse(status=False, message="Failed to get a book with non-existing isbn.") 
        # find book and return with success message
        return inventory_service_pb2.GetBookResponse(status=True, message="Successfully fetched book with this isbn.", book=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_service_pb2_grpc.add_InventoryServiceServicer_to_server(LibraryInventoryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on localhost:50051")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()