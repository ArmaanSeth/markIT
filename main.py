from crewai import Crew
from agents import MarkitAgents
from tasks import MarkitTasks
import dotenv
dotenv.load_dotenv()

class MarkitCrew:
    def __init__(self, product_name, product_description, tagline_theme) -> None:
        self.product_name = product_name
        self.product_description = product_description
        self.tagline_theme = tagline_theme

    def run(self):
        agents=MarkitAgents()
        tasks=MarkitTasks()
        marketing_head_agent=agents.MarketingHeadAgent()
        research_analyst_agent=agents.ResearchAnalystAgent()
        content_creator_agent=agents.ContentCreatorAgent()

        marketing_head_task=tasks.MarketingHeadTask(marketing_head_agent, self.product_name, self.product_description, self.tagline_theme,"")
        research_analyst_task=tasks.ResearchAnalystTask(research_analyst_agent, self.product_name, self.product_description,"")
        content_creator_task=tasks.ContentCreatorTask(content_creator_agent, self.product_name, self.product_description, self.tagline_theme,"")

        research_analyst_task.context=[marketing_head_task]
        content_creator_task.context=[marketing_head_task, research_analyst_task]

        crew=Crew(
            agents=[marketing_head_agent, research_analyst_agent, content_creator_agent],
            tasks=[marketing_head_task, research_analyst_task, content_creator_task],
            verbose=True
        )
        res=crew.kickoff()
        return res

if __name__ == "__main__":
    print("           Welcome to markIT!        ")
    print("=====================================")
    product_name = input("Enter the name of the product: ")
    product_description = input("Enter the description of the product: ")
    tagline_theme = input("Enter the tagline theme: ")
    
    crew=MarkitCrew(product_name, product_description, tagline_theme)
    res=crew.run()
    print("=====================================")
    print("Result from the crew:")
    print(res)
    print("=====================================")
    print("=====Thank you for using markIT!=====")
