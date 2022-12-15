from unittest.mock import MagicMock
import unittest
import inventory_client
import get_book_titles

class TestGetBookTitles(unittest.TestCase):
    mocked_client = inventory_client.InventoryClient("localhost:50051")
    book = {
            "isbn": "N10000",
            "title": "Yuki's Bio",
            "author": "Yuki",
            "publishingYear": 1997,
            "genre": "BIOGRAPHY"
        }
    mocked_client.getBooks = MagicMock(return_value=["Yuki's Bio", "How To Get An A In API Design"])

    # Mocked client
    def test_with_mocked_client(self):
        print("===== Testing with mocked client: =====")
        lst = get_book_titles.getListOfBooks(self.mocked_client, ["N10000", "N20000"])
        res = self.helper_match_result(lst)
        self.assertTrue(res)

    # Live client
    def test_with_live_client(self):
        live_client = inventory_client.InventoryClient("localhost:50051")
        print("===== Testing with live client: =====")
        lst = get_book_titles.getListOfBooks(live_client, ["N10000", "N20000"])
        res = self.helper_match_result(lst)
        self.assertTrue(res)
    
    def helper_match_result(self, result) -> bool:
        expected = ["Yuki's Bio", "How To Get An A In API Design"]
        for idx, item in enumerate(result):
            isEqual = (expected[idx] == item)
            print("Assert [" + expected[idx] + " == " + item + "] => " + str(isEqual))
            if (not isEqual):
                return False
        return True

if __name__ == '__main__':
    unittest.main()