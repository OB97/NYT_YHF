from pynytimes import NYTAPI

# set up key and api
apiKey = '6ykwvVJlIk4EKnpTk4PWaEsAJmdJ6dTN'
nyt = NYTAPI(apiKey, parse_dates=True)

# call the most_viewed method, store as a list of dictionaries
most_viewed = nyt.most_viewed()

# convert to enumerated dictionary
most_viewed_dict = {}
for i, d in enumerate(most_viewed):
    most_viewed_dict[i] = d

# simple loop to add article titles to a list
titleList = []
for article in most_viewed_dict.values():
    titleList.append(article['title'])

print("")
print("\n".join(titleList))
