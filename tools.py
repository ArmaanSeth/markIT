from langchain.tools import tool
from exa_py import Exa
from dotenv import load_dotenv
import os

load_dotenv()
class SearchTools:
    @tool("Search on internet")
    def search(query:str):
        """Used to search any information on the internet.
        Args:
            query (str): The query to search on the internet.
        Return (str): The search results."""
        
        return f"{Exa(api_key=os.environ.get("EXA_API_KEY")).search_and_contents(
                    query=query,
                    type="neural",
                    use_autoprompt=True,
                    num_results=1,
                    text=True
                    )}"
    
    