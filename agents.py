from tabnanny import verbose
from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq
import os

class MarkitAgents:
    def __init__(self) -> None:
        self.llm=ChatGroq(api_key=os.environ.get("GROQ_API_KEY"),model="mixtral-8x7b-32768",verbose=True)
        self.maxiter=3
        
    def MarketingHeadAgent(self):
        return Agent(
            role="Marketing Head",
            goal=dedent("""Conduct a market research about the new product and its competitors. 
                        Based on the research, create a product mockup with taglines on top of the images for social media marketing."""),
            backstory=dedent("""Expert in market research and social media marketing, 
                             Specializes in creating product mockups for social media marketing."""),
            tools=[],
            verbose=True,
            llm=self.llm,
            max_iter=self.maxiter
        )

    def ResearchAnalystAgent(self):
        return Agent(
            role="Research Analyst",
            goal=dedent("""Conduct a thorough market research about the new product and its competitors. 
                        Find out the target audience, market trends, and competitors' strategies.
                        Provide the Marketing Head with a detailed report of the research.
                        Find out about the slogans and taglines used by competitors for their products."""),
            backstory=dedent("""Expert in market research and analysis, 
                             Specializes in finding out market trends and competitors' strategies."""),
            tools=[],
            verbose=True,
            llm=self.llm,
            max_iter=self.maxiter
        )
    
    def ContentCreatorAgent(self):
        return Agent(
            role="Content Creator",
            goal=dedent("""Create engaging content for the new product for social media marketing. 
                        Takes information from the Research Analyst and creates engaging taglines and slogans for the product."""),
            backstory=dedent("""Expert in content creation and copywriting, 
                             Specializes in writing catchy taglines and slogans for social media marketing."""),
            tools=[],
            verbose=True,
            llm=self.llm,
            max_iter=self.maxiter
        )

    def ProductDesignerAgent(self):
        return Agent(
            role="Product Designer",
            goal=dedent("""Create product images for the new product. 
                        Uses the taglines and slogans provided by the Content Creator to create engaging product images for social media marketing."""),
            backstory=dedent("""Expert in product design and visualization, 
                             Specializes in creating product images for marketing purposes."""),
            tools=[],
            verbose=True,
            llm=self.llm,
            max_iter=self.maxiter
        )