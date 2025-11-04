import requests
import xml.etree.ElementTree as ET
import csv


def get_top_podcasts(country="us", limit=20):
    """
    Fetch top podcasts from Appled podcasts RSS feed

    Args:
        country: Country code (default: 'us')
        limit: Number of podacsts to retrieve (default: 20)

    Returns:
        List of dicts with podcast info (name, artist, link)
    """

    url = f"https://itunes.apple.com/{country}/rss/toppodcasts/limit={limit}/xml"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        root = ET.fromstring(response.content)

        print(f"\n{'='*80}")
        print(f"TOP {limit} PODCASTS ON APPLE PODCASTS ({country.upper()}")
        print(f"{'='*80}\n")

        entries = root.findall('.//{http://www.w3.org/2005/Atom}entry')
        podcasts = []

        for idx, entry in enumerate(entries, 1):
            name_elem = entry.find('.//{http://itunes.apple.com/rss}name')
            artist_elem = entry.find('.//{http://itunes.apple.com/rss}artist')
            link_elem = entry.find('.//{http://www.w3.org/2005/Atom}link')

            name = name_elem.text if name_elem is not None else 'N/A'
            artist = artist_elem.text if artist_elem is not None else 'N/A'
            link = link_elem.get('href') if link_elem is not None else 'N/A'

            podcasts.append({
                "rank": idx,
                "name": name,
                "artist": artist,
                "url": link
            })

            print(f"{idx:2d}. {name}")
            print(f"    Artist: {artist}")
            print(f"    URL: {link}")

        return podcasts

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return None

def save_to_csv(podcasts, filename="top_podcasts.csv"):
    """
    Save podcast list to as CSV file
    """
    if not podcasts:
        print("No podcasts to save.")
        return

    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["rank", "name", "artist", "url"])
            writer.writeheader()
            writer.writerows(podcasts)
        print(f"\n✅ Data successfully saved to '{filename}'")
    except Exception as e:
        print(f"Error writing CSV: {e}")


if __name__ == "__main__":
    podcasts = get_top_podcasts(country='us', limit=20)

    if podcasts:
        save_to_csv(podcasts, filename="top_podcasts_us.csv")
    else:
        print("Failed to retrieve podcasts.")













        














        







        
