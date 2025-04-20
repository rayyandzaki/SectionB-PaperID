from locust import HttpUser, task

class APITest(HttpUser):
    @task
    def login(self):
        self.client.post(
            "/api/login",
            json={
                "email": "eve.holt@reqres.in",
                "password": "cityslicka"
            },
            headers={"Content-Type": "application/json"}
        )
