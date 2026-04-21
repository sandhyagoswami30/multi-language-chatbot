from ddgs import DDGS

def search_duckduckgo(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

            for r in results:
                text = r.get("body") or r.get("title")
                if text:
                    return text

        return "No useful result found."
    except Exception as e:
        return f"Search Error: {e}"