from bs4 import BeautifulSoup
import requests
import keys

SHEETY_URL: str = keys.ROOMS_SHEETY_URL

piso_compartido_url: str = "https://www.pisocompartido.com/en/renting-rooms-barcelona_capital/hasta-450" \
                           "/?precio=450&id_tipo_hab=&ch_hab=1&ch_piso=0&companero=&orden=9"

# Get URL (unique identifier) for rooms that are already in the sheet.
response = requests.get(url=SHEETY_URL)
data: dict = response.json()
current_urls: list = [entry["url"] for entry in data["sheet1"]]

# Get data for rooms on the website.
response = requests.get(url=piso_compartido_url)

soup = BeautifulSoup(response.text, "html.parser")
amount_pages: int = int(soup.find(name="ul", class_="list-inline").find_all(name="li")[-2].text)

results: list = []
print(amount_pages)
for page in range(1, amount_pages+1):
    if page > 1:
        piso_compartido_url: str = f"https://www.pisocompartido.com/en/renting-rooms-barcelona_capital/hasta-450" \
                                   f"/{page}/?precio=450&id_tipo_hab=&ch_hab=1&ch_piso=0&companero=&orden=9"
        response = requests.get(url=piso_compartido_url)
        soup = BeautifulSoup(response.text, "html.parser")
    ads = soup.find_all(name="div", class_="cCards")
    for ad in ads:
        infos: dict = {"address": ad.find(name="div", class_="contLocalizacion").text.strip(),
                       "price": ad.find(name="span", class_="contPrecio").text.split()[0] + " Euro",
                       "url": ad.find(name="a", class_="linkCard")["href"]}
        results.append(infos)

# If any room is not already in the sheet, add it.
for room in results:
    if room["url"] not in current_urls:
        print("Posting..")
        data: dict = {
            "sheet1": room
        }
        requests.post(url=SHEETY_URL, json=data)

# If any room in the sheet is not in the results, delete it.
new_urls: list = [entry["url"] for entry in results]

add: int = 2
for i, curr_url in enumerate(current_urls):
    if curr_url not in new_urls:
        requests.delete(url=SHEETY_URL + f"/{i+add}")
        add -= 1
