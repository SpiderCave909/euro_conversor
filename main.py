import requests;

URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml";

try:
    response = requests.get(URL);

    if response.status_code == 200:
        print("Successfully entered!");
        print(response.content.decode("utf-8")[:500]);
    else:
        print("Error, unable to connect to the server.");
except Exception as e:
    print("Error,", e);