import requests
import sys
import os

def fetch_page_content(page_title):
    # Set language for Wikipedia search
    language = 'en'  # English language Wikipedia
    # Set Wikipedia API endpoint
    url = f"https://{language}.wikipedia.org/w/api.php"

    # Set parameters for the query
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "titles": page_title
    }

    try:
        # Make request to Wikipedia API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for any HTTP error

        # Extract page content from the response
        pages = response.json()['query']['pages']
        
        # Get the page ID (there will be only one page in the response)
        page_id = next(iter(pages))
        
        # Extract the page content (extract is the key for the content)
        page_content = pages[page_id]['extract']

        return page_content

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def main():
    # Check if query is provided
    if len(sys.argv) != 2:
        print("Usage: python request_wikipedia.py <search_query>")
        return

    # Extract query from command line argument
    query = sys.argv[1]

    # Fetch page content from Wikipedia for the query
    result = fetch_page_content(query)

    # If the result is empty or an error message, try the alternative term
    if not result:
        alternative_query = "pain au chocolat"
        print(f"Failed to find information for '{query}'. Trying '{alternative_query}'.")
        result = fetch_page_content(alternative_query)

    # Check if the result is empty or an error message again
    if result:
        # Define file name based on the query
        file_name = f"{query.replace(' ', '_')}.wiki"

        # Write the result to the file
        with open(file_name, 'w') as file:
            file.write(result)
        print(f"Result written to {file_name}")
    else:
        print("Error: Unable to retrieve information from Wikipedia.")

if __name__ == "__main__":
    main()
