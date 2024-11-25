
from tools.scraper import scrape_profile, scrape_posts

class LinkedInScraperAgent:
    def __init__(self):
        self.name = "LinkedIn Scraper Agent"

    def execute(self, profile_url):
        profile_data = scrape_profile(profile_url)
        posts_data = scrape_posts(profile_url)
        return {"profile_data": profile_data, "posts_data": posts_data}
