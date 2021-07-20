import json
import behave2cucumber
with open('behave_json.json') as behave_json:
    cucumber_json = behave2cucumber.convert(json.load(behave_json))
