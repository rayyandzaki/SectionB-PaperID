import unittest
import requests

class TestAPI(unittest.TestCase):
    def test_login(self):
        url = "https://reqres.in/api/login"
        headers = {"Content-Type": "application/json"}
        data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }

        # Send POST request
        response = requests.post(url, json=data, headers=headers)

        # Test: Response status should be 200
        self.assertEqual(response.status_code, 200)

        # Test: Response should contain a token
        response_json = response.json()
        self.assertIn("token", response_json)

if __name__ == "__main__":
    unittest.main()
