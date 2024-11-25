
from tools.content_generator import generate_content

class ContentGenerationAgent:
    def __init__(self):
        self.name = "Content Generation Agent"

    def execute(self, analysis):
        strategy, content = generate_content(analysis)
        return {"strategy": strategy, "content": content}
