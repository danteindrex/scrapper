from crewai_tools import SerperDevTool
import json
import pandas as pd

tool = SerperDevTool(
    search_url="https://google.serper.dev/scholar",
    n_results=20,
    location="us"
)

def Scrapper(query):
    results = tool.run(search_query=query)
    organic = results.get('organic', [])

    # Structure the results
    structured = [
        {
            'title':    item.get('title', ''),
            'link':     item.get('link', ''),
            'snippet':  item.get('snippet', ''),
            'position': item.get('position')
        }
        for item in organic
    ]

    # Save to JSON
    with open('search_results.json', 'w', encoding='utf-8') as f:
        json.dump(structured, f, indent=2, ensure_ascii=False)

    # Optional: load into DataFrame
    df = pd.DataFrame(structured)

    pd.set_option('display.max_columns', None)    # show all columns
    pd.set_option('display.width', 0)             # no line‑wrapping limit
    print(df)
    print(df.columns)

# Example usage
Scrapper("remote AI engineer jobs")
