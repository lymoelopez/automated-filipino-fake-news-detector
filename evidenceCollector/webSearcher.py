from duckduckgo_search import DDGS


def urlFilter(url, urlBanList):
  lowercasedURL = url.lower()
  if all(excludedURL not in lowercasedURL for excludedURL in urlBanList):
    return url

def duckDuckGoSearch(inputClaim):
  duckDuckGoSearch = DDGS()
  duckDuckGoTextSearchGenerator = duckDuckGoSearch.text(inputClaim, region='ph-tl', safesearch='Off')
  return duckDuckGoTextSearchGenerator 

def webSearcher(inputClaim, urlBanList):

  urlList = []
  urlContentList = []
  
  duckDuckGoTextSearchGenerator = duckDuckGoSearch(inputClaim)

  for searchResult in duckDuckGoTextSearchGenerator:
 
    if urlFilter(searchResult["href"], urlBanList):
      urlList.append(searchResult["href"])
      urlContentList.append(searchResult["title"] + " " + searchResult["body"])

  return urlList, urlContentList
