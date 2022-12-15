import inventory_client
import logging

def getListOfBooks(client, isbns) -> list:
    getBooks = client.getBooks
    lst = getBooks(isbns)
    return lst

if __name__ == '__main__':
    logging.basicConfig()
    client = inventory_client.InventoryClient("localhost:50051")
    isbns = ["N10000", "N20000"]
    results = getListOfBooks(client, isbns)
    print("===== fetched books with titles =====")
    for res in results:
        print(res)