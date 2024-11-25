
from tools.publisher import post_content

class PublishingAgent:
    def __init__(self):
        self.name = "Publishing Agent"

    def execute(self, content):
        result = post_content(content)
        return result
