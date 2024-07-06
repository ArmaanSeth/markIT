
from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq
from tools import SearchTools
import os

class MarkitAgents:
    def __init__(self) -> None:
        self.llm=ChatGroq(api_key=os.environ.get("GROQ_API_KEY"),model="mixtral-8x7b-32768",verbose=True)
        self.maxiter=3
        
    def MarketingHeadAgent(self):
        return Agent(
            role="Marketing Head",
            goal=dedent("""Conduct a market research about similar products for a new product that is to be launched in the market  . There is no information available about the new product but can search about similar products. 
                        Based on the research, create a product mockup with taglines on top of the images for social media marketing."""),
            backstory=dedent("""Expert in market research and social media marketing, 
                             Specializes in creating product mockup taglines for social media marketing for new product to be launched in the market."""),
            verbose=True,
            llm=self.llm,
            max_iter=self.maxiter
        )

    def ResearchAnalystAgent(self):
        return Agent(
            role="Research Analyst",
            goal=dedent("""Conduct a thorough market research about the products similar to the one being lauched. 
                        Find out the target audience, market trends, and existing advertisement content.
                        Gather information about the features and benefits of the product that can be used in the marketing campaign around the theme provided."""),
            backstory=dedent("""Expert in market research and analysis, 
                             Specializes in finding out market demands and usp of a product."""),
            tools=[SearchTools.search],
            verbose=True,
            llm=self.llm,
            max_iter=self.maxiter
        )
    
    def ContentCreatorAgent(self):
        return Agent(
            role="Content Creator",
            goal=dedent("""Create engaging content for the new product for social media marketing. 
                        Takes information from the Research Analyst and creates engaging taglines and slogans for the product. Identifies USP of the product and uses them as taglines."""),
            backstory=dedent("""Expert in content creation and writing slogans and taglines for marketing campaigns, 
                             Specializes in writing catchy taglines and slogans for social media marketing."""),
            tools=[SearchTools.search],
            verbose=True,
            llm=self.llm,
            max_iter=self.maxiter
        )

    # def ProductDesignerAgent(self):
    #     return Agent(
    #         role="Product Designer",
    #         goal=dedent("""Create product images for the new product. 
    #                     Uses the taglines and slogans provided by the Content Creator to create engaging product images for social media marketing."""),
    #         backstory=dedent("""Expert in product design and visualization, 
    #                          Specializes in creating product images for marketing purposes."""),
    #         tools=[],
    #         verbose=True,
    #         llm=self.llm,
    #         max_iter=self.maxiter
    #     )