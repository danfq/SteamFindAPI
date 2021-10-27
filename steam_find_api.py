#SteamFind v1.0.0 - API
#DanFQ

#Requirements
from bs4 import BeautifulSoup
import requests

class API():

    def htmlParse(htmlContent):
        return str(htmlContent).strip().replace("\n", "").replace("\t", "").replace("\r", "").replace("Developer:", "").replace("Publisher:", "")

    def steam_data(appID):
        steamAppURL = "https://store.steampowered.com/app/"
        requestURL = steamAppURL + str(appID)
        response = requests.get(requestURL)

        steam_app_data = {}

        data = BeautifulSoup(response.text, 'html.parser')

        for title in data.find_all('title'):
            pageTitle = title.get_text()
            
            if (pageTitle == "Welcome to Steam" or response.status_code == 302):
                return {"error" : "Invalid Steam AppID"}
            else:
                steam_app_data["title"] = API.htmlParse(data.find('div', {"class" : "apphub_AppName"}).get_text())
                steam_app_data["description"] = API.htmlParse(data.find('div', {"class" : "game_description_snippet"}).get_text().replace("\"", '"'))
                steam_app_data["cover_image"] = data.find('img', {"class" : "game_header_image_full"})["src"].split("?", 1)[0]
                steam_app_data["release_date"] = API.htmlParse(data.find('div', {"class" : "date"}).get_text())
                steam_app_data["developer"] = API.htmlParse(data.find_all('div', {"class" : "dev_row"})[0].text)
                steam_app_data["editor"] = API.htmlParse(data.find_all('div', {"class" : "dev_row"})[1].text)
                steam_app_data["price"] = API.htmlParse(data.find('div', {"class" : "game_purchase_price price"}).get_text())
                return steam_app_data

    def get_steam_app_info(appID):
        return API.steam_data(appID)
