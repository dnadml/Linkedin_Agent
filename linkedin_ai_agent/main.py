
from agents.linkedin_scraper_agent import LinkedInScraperAgent
from agents.data_analysis_agent import DataAnalysisAgent
from agents.content_generation_agent import ContentGenerationAgent
from agents.publishing_agent import PublishingAgent
from tasks.task_router import TaskRouter

scraper = LinkedInScraperAgent()
analyzer = DataAnalysisAgent()
generator = ContentGenerationAgent()
publisher = PublishingAgent()

agents = {
    "scraper": scraper,
    "analyzer": analyzer,
    "generator": generator,
    "publisher": publisher
}

router = TaskRouter(agents)

try:
    profile_url = "https://www.linkedin.com/in/example-profile/"
    print("Scraping profile...")
    scraped_data = router.execute("scrape", profile_url)

    print("Analyzing data...")
    analysis = router.execute("analyze", scraped_data)

    print("Generating content...")
    generated = router.execute("generate", analysis)

    print("Publishing content...")
    result = router.execute("publish", generated["content"])

    print("Workflow completed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
