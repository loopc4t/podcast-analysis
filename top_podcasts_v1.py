import requests
import xml.etree.ElementTree as ET


def get_top_podcasts(country="us", limit=20):
    """
    Fetch top podcasts from Apple Podcasts RSS feed

    Args:
        country: Country code  (default: 'us')
        limit: Number of podcasts to retrieve (default: 20)
    """
    # Apple's RSS feed for top podcasts (XML format)
    url = f"https://itunes.apple.com/{country}/rss/toppodcasts/limit={limit}/xml"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parse XML response
        root = ET.fromstring(response.content)

        print(f"\n{'='*80}")
        print(f"TOP {limit} PODCASTS ON APPLE PODCASTS")
        print(f"{'='*80}\n")

        # XML namespace for iTunes RSS feed
        namespaces = {'': 'http://www.w3.org/2005/Atom',
                      'im': 'http://itunes.apple.com/rss'}

        entries = root.findall('.//{http://www.w3.org/2005/Atom}entry')

        for idx, entry in enumerate(entries, 1):
            # Extract podcast information
            name_elem = entry.find('.//{http://itunes.apple.com/rss}name')
            artist_elem = entry.find('.//{http://itunes.apple.com/rss}artist')
            link_elem = entry.find('.//{http://www.w3.org/2005/Atom}link')

            name = name_elem.text if name_elem is not None else 'N/A'
            artist = artist_elem.text if artist_elem is not None else 'N/A'
            link = link_elem.get('href') if link_elem is not None else 'N/A'

            print(f"{idx:2d}. {name}")
            print(f"    Artist: {artist}")
            print(f"    URL: {link}")

        return

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return None


if __name__== "__main__":
    # You can change the country code here (e.g., 'uk', 'br')
    podcasts = get_top_podcasts(country='us', limit=20)

    if podcasts:
        print(f"Successfully retrieved {len(podcasts)} podcasts!")
    else:
        print("Failed to retrieve podcasts.")
