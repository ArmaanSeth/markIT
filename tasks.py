import re
from textwrap import dedent
from crewai import Task
from langsmith import expect

class MarkitTasks:
    def MarketingHeadTask(self, agent, product_name, product_description, tagline_theme):
        return Task(
            description=dedent(f"""\
                            Task: Conduct a market research about simial product and generate a product mockup with taglines under a specific theme on top of the images for social media marketing.
                            Description: The Marketing Head is responsible for conducting a market research about similar. Based on the research and theme provided, the Marketing Head needs to create taglines to launch this new product.
                            Parameters:
                               - Product Name: {product_name}.
                               - Product Description: {product_description}.
                               - Tagline theme: {tagline_theme}."""),
            expected_output=dedent(f"""\
                                    Python list of taglines and slogans for the new product that are relevant to the product and its theme.    
                                   """),
            agent=agent,
            async_execution=True
        )
    
    def ResearchAnalystTask(self, agent, product_name, product_description, context):
        return Task(
            description=dedent(f"""\ 
                            Task: Conduct a thorough market research about the similar products using its description only. Provide the Marketing Head with a detailed report of the research. Find out about the slogans and taglines used by similar products.
                            Description: The Research Analyst is responsible for conducting a thorough market research about the similar products, find out features and USP that the new product can offer.
                            Parameters:
                               - context: {context}.
                               - Product Name: {product_name}.
                               - Product Description: {product_description}."""),
            expected_output=dedent(f"""\
                            Detailed report of the market research about similar products that can be helpful in creating taglines. Competetors' strategies and slogans used by them for their products."""),
            agent=agent,
            async_execution=True
        )
    
    def ContentCreatorTask(self, agent, product_name, product_description, tagline_theme, context):
        return Task(
            description=dedent(f"""\
                            Task: Create engaging content for the new product for social media marketing. Takes information from the Research Analyst and creates engaging taglines and slogans for the product.
                            Description: The Content Creator is responsible for creating engaging content for the new product for social media marketing. The Content Creator needs to take information from the Research Analyst and create engaging taglines and slogans for the product under a specific theme.
                            Parameters:
                                 - context: {context}.
                               - Product Name: {product_name}.
                               - Product Description: {product_description}.
                               - Tagline theme: {tagline_theme}."""),
            expected_output=dedent(f"""\
                                   Multiple engaging taglines and slogans for the new product that are relevant to the product and its theme returned in a lorm of python list.    
                                   """),
            agent=agent,
            async_execution=True
        )
