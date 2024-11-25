
class TaskRouter:
    def __init__(self, agents):
        self.agents = agents

    def execute(self, task_name, data):
        if task_name == "scrape":
            return self.agents["scraper"].execute(data)
        elif task_name == "analyze":
            return self.agents["analyzer"].execute(data)
        elif task_name == "generate":
            return self.agents["generator"].execute(data)
        elif task_name == "publish":
            return self.agents["publisher"].execute(data)
        else:
            raise ValueError("Unknown task")
