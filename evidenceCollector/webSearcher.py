from googlesearch import search


URL_banList = ["facebook", "twitter", "youtube", "pdf", "blog", "tiktok", "instagram", "youtu.be", "mp4", "mp3", "audiobook", "podcast", "spotify", "slideshare", "github", "huggingface"]

def URLfilter(url):
  lowercasedURL = url.lower()
  if all(excludedURL not in lowercasedURL for excludedURL in URL_banList):
    return url
     
def webSearcher(inputClaim, numOfSearchResults):

  filteredList = []
  
  while len(filteredList) <= numOfSearchResults:
    if len(filteredList) >= numOfSearchResults:
      break
    for url in search(inputClaim, lang="tl", num=numOfSearchResults, pause=3):
      filteredURL = URLfilter(url)
      if filteredURL and (filteredURL not in filteredList):
        filteredList.append(filteredURL)
      if len(filteredList) >= numOfSearchResults:
        break

    return filteredList
