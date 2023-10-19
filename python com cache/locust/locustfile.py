from locust import HttpUser, TaskSet, task, between


class UserTasks(TaskSet):
    @task
    def invocação_1(self):
        self.client.get("/?url=https%3A%2F%2Fpt.wikipedia.org%2Fwiki%2FUruguai")

    @task
    def invocação_2(self):
        self.client.get("/?url=https%3A%2F%2Fpt.wikipedia.org%2Fwiki%2FArgentina")

    @task
    def invocação_3(self):
        self.client.get("/?url=https%3A%2F%2Fpt.wikipedia.org%2Fwiki%2FParaguai")

    @task
    def invocação_4(self):
        self.client.get("/?url=https%3A%2F%2Fpt.wikipedia.org%2Fwiki%2FChile")

    @task
    def invocação_5(self):
        self.client.get("/?url=https%3A%2F%2Fpt.wikipedia.org%2Fwiki%2FBrasil")

    @task
    def invocação_6(self):
        self.client.get("/?url=https%3A%2F%2Fpt.wikipedia.org%2Fwiki%2FPeru")

    @task
    def invocação_7(self):
        self.client.get("/?url=https%3A%2F%2Fpt.wikipedia.org%2Fwiki%2FColombia")

    @task
    def invocação_8(self):
        self.client.get("/?url=https%3A%2F%2Fpt.wikipedia.org%2Fwiki%2FGuiana")

    @task
    def invocação_9(self):
        self.client.get("/?url=https%3A%2F%2Fpt.wikipedia.org%2Fwiki%2FEquador")

    @task
    def invocação_10(self):
        self.client.get("/?url=https%3A%2F%2Fpt.wikipedia.org%2Fwiki%2FVenezuela")


class WebsiteUser(HttpUser):
    tasks = [UserTasks]
    wait_time = between(1, 5)  # Define the wait time between tasks
