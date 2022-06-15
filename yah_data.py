import requests

url = "https://yh-finance.p.rapidapi.com/stock/v3/get-historical-data"

querystring = {"symbol":"AMRN"}

headers = {
	"X-RapidAPI-Key": "5717a7948cmsha10773330926d2bp1b628cjsn10aeae9706c9",
	"X-RapidAPI-Host": "yh-finance.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)