import requests;

class Scrapper:
    URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml";

    def __init__(self):
        pass;

    def scrap(self):
        try:
            response = requests.get(self.URL);
            
            if response.status_code == 200:
                print("Successfull connection.");

                with open("currencies.xml", "wb") as f:
                    f.write(response.content);
            else:
                raise Exception("Unable to connect to server.");
        except Exception as e:
            print("Error,", e);