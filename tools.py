from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print
load_dotenv()

#User asks a question
 #       ↓
  # web_search()
   #     ↓
   #Tavily searches web
    #    ↓
#Title + URL + Snippet
 #       ↓
#If deeper information is needed
 #       ↓
  # scrape_url(URL)
   #     ↓
#Download webpage HTML
 #       ↓
#BeautifulSoup cleans HTML
 #       ↓
#Extract useful text
 #       ↓
#Return up to 3000 characters

tavily =  TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# =========================================================
# TOOL 1: WEB SEARCH
# User Query → Tavily Search → Get 5 Results
# → Extract Title + URL + Short Snippet → Return Results
# =========================================================
@tool
def web_search(query : str) -> str:
    """Search the web for recent and reliable information on a topic . Returns Titles , URLs and snippets."""
    results = tavily.search(query=query,max_results=5)

    out=[]  #create a new list

    for r in results['results']:    #run loop in the results
         out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"    #from result only extract title , url, snippet ,content of 300 words

        )

    return "\n----\n".join(out)
#print(web_search.invoke("what is the recent news of nepal?"))


# =========================================================
# TOOL 2: URL SCRAPER
# Flow:
# URL → Send Request → Get HTML
# → BeautifulSoup → Remove Unwanted Tags
# → Extract Text → Return First 3000 Characters
# =========================================================
@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"


