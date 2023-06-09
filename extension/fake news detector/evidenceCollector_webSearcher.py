from duckduckgo_search import DDGS


def urlFilter(url, urlBanList):
  lowercasedURL = url.lower()
  if all(excludedURL not in lowercasedURL for excludedURL in urlBanList):
    return url

def duckDuckGoSearch(searchQuery):
  duckDuckGoSearch = DDGS()
  duckDuckGoTextSearchGenerator = duckDuckGoSearch.text(searchQuery, region='ph-tl', safesearch='Off')
  return duckDuckGoTextSearchGenerator 

def duckDuckGoBangsRemover(searchQuery):
  reversedQuery = searchQuery[::-1]
  newQuery = reversedQuery.replace("!", "!\\",1)[::-1]
  return newQuery  
  
def webSearcher(inputClaim, urlBanList):

  urlList = []
  urlTitleList = []
  urlBodyList = []
  maxSearchResults = 20
  
  try:
    duckDuckGoTextSearchGenerator = duckDuckGoSearch(inputClaim)
  except:
    inputClaim = duckDuckGoBangsRemover(inputClaim)
    duckDuckGoTextSearchGenerator = duckDuckGoSearch(inputClaim)
  else:
    inputClaim = duckDuckGoBangsRemover(inputClaim)
    duckDuckGoTextSearchGenerator = duckDuckGoSearch(inputClaim)
    
  for searchResult in duckDuckGoTextSearchGenerator:

    if len(urlList) != maxSearchResults:
      if urlFilter(searchResult["href"], urlBanList):
        urlList.append(searchResult["href"])
        urlTitleList.append(searchResult["title"])
        urlBodyList.append(searchResult["body"])

    else:
      filteredSearchResults = [urlList, urlTitleList, urlBodyList]
      return filteredSearchResults 

  filteredSearchResults = [urlList, urlTitleList, urlBodyList]
  return filteredSearchResults
