import requests

class Weather:
    def get_quick_weather(unit):
        """
        Get the weather.

        :param unit: The unit of the weather.
        :type unit: str

        :return: The weather.
        :rtype: str
        """
        url = f"https://wttr.in/?format=3&{unit if unit else 'm'}"
        response = requests.get(url)
        return response.text
    
