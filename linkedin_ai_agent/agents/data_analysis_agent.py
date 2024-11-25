
from tools.analysis import analyze_data

class DataAnalysisAgent:
    def __init__(self):
        self.name = "Data Analysis Agent"

    def execute(self, data):
        analysis = analyze_data(data)
        return analysis
