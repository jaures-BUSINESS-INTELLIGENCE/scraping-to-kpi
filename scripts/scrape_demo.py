import requests
from bs4 import BeautifulSoup

URL = "https://fr.wikipedia.org/wiki/Le_Mans"
# Le "User-Agent" dit au site qui nous sommes 
USER_AGENT = "ENSIM-BI-course-TD (educational)"

def robots_allows(url, user_agent="*"):
    # Vérifie dans robots.txt si on a le droit de lire cette page.
    # On télécharge le texte avec requests puis on le donne à rp.parse().
    # On évite rp.read() : sur un réseau avec proxy, il répond "tout est interdit"
    # SANS afficher la moindre erreur (échec silencieux).
    import urllib.robotparser
    resp = requests.get("https://fr.wikipedia.org/robots.txt",
                         proxies={"http": None, "https": None},
                         headers={"User-Agent": USER_AGENT}, timeout=15)
    resp.raise_for_status()  # si le téléchargement échoue : erreur visible, on s'arrête
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(resp.text.splitlines())
    return rp.can_fetch(user_agent, url)

def main():
    allowed = robots_allows(URL)
    print(f"robots.txt allows fetching {URL}: {allowed}")
    if not allowed:
        # Si c'est interdit, on s'arrête. On ne scrape pas quand même.
        raise SystemExit("robots.txt disallows this -- stopping, not scraping anyway.")

    resp = requests.get(URL, proxies={"http": None, "https": None},
                         headers={"User-Agent": USER_AGENT}, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")  # transforme le HTML en objet explorable

    # Le titre de la page = la balise <h1>
    title = soup.find("h1").get_text(strip=True)

    # Le premier vrai paragraphe : on saute les "hatnotes" (bandeaux du type
    # "Pour les articles homonymes...") qui ne sont pas du vrai contenu
    first_para = None
    for p in soup.find_all("p"):
        if p.find_parent(class_="hatnote"):
            continue
        text = p.get_text(strip=True)
        if len(text) > 40:
            first_para = text
            break

    print(f"\nPage title: {title}")
    print(f"First real paragraph ({len(first_para)} chars): {first_para[:200]}...")

    # La population : on cherche la ligne de l'encadré dont le titre contient
    # "population" (on cherche par le texte, pas par la position, c'est plus solide)
    population = None
    for row in soup.select("table.infobox_v2 tr, table.infobox tr"):
        header = row.find("th")
        if header and "population" in header.get_text(strip=True).lower():
            cell = row.find("td")
            if cell:
                population = cell.get_text(" ", strip=True)
                break
    print(f"Extracted population field (unstructured -> one variable): {population!r}")

if __name__ == "__main__":
    main()
