import requests
import webbrowser

class TFL:

  _app_id = "_"
  _app_key = "_"
  _domain =  "https://api.tfl.gov.uk"

  def __init__(self):
    pass

  def journey(self, origin, destiny):
    part="snippet" #id
    params = (
        "nationalSearch=False&&&timeIs=Departing&&&&&&&&&&&&&alternativeCycle=False"
        "&alternativeWalking=True&applyHtmlMarkup=False"
        "&useMultiModalCall=False&app_id={app_id}&app_key={app_key}"
        .format(app_id = self._app_id, app_key = self._app_key)
    )
    url = "{domain}/Journey/JourneyResults/{origin}/to/{destiny}?{params}".format( domain= self._domain, origin = origin, destiny = destiny, params = params )

    print ("url "+ url)

    response = requests.get(url).json()["journeys"][0]["duration"]

    print ("response", response)

    return response
