import bs4
import requests
from bs4 import BeautifulSoup


class Forecast:
    """
    Writes down the file with the forecast information.
    """
    def __init__(self, city: str):
        self.city = city.lower()

    def get_forecast(self):
        file = requests.get(url=f"https://pogoda.mail.ru/prognoz/{self.city}")
        soup = BeautifulSoup(file.content, 'html.parser')
        city = soup.find(
            "div",
            {"class": "information__header__left__place"}).text.strip()
        temperature = soup.find(
            "div",
            {"class": "information__content__temperature"}).text.strip()
        current_date = soup.find(
            "div",
            {"class": "information__header__left__date"}).text.strip()
        approximate_temp = soup.find(
            "div",
            {"class": "information__content__additional__item"}).text.strip()
        try:
            with open('weather.txt', 'w', encoding="utf-8") as f:
                f.write(
                    f"{city}\n"
                    f"{current_date.capitalize()}\n"
                    f"Сейчас: {temperature}\n"
                    f"{approximate_temp.capitalize()}"
                )
        except bs4.FeatureNotFound:
            return "Empty response."
        finally:
            return "The weather.txt file has been created."
