from googlesearch import search


URL_banList = ["facebook", "twitter", "youtube", "pdf", "blog", "tiktok", "instagram", "youtu.be", "mp4", "mp3", "audiobook", "podcast", "spotify", "slideshare", "github", "huggingface"]

def URLfilter(url):
  lowercasedURL = url.lower()
  if all(excludedURL not in lowercasedURL for excludedURL in URL_banList):
    return url
     
def webSearcher(inputClaim, numOfResults=20):

  filteredList = []
  
  while len(filteredList) <= numOfResults:
    if len(filteredList) >= numOfResults:
      break
    for url in search(inputClaim, lang="tl", num=numOfResults, pause=3):
      filteredURL = URLfilter(url)
      if filteredURL and (filteredURL not in filteredList):
        filteredList.append(filteredURL)
      if len(filteredList) >= numOfResults:
        break

    return filteredList
     
#print(webSearcher("Phased out na ang mga jeep",5))
