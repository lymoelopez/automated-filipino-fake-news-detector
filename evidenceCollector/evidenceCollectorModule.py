from webSearcher import webSearcher
from evidenceSelector import evidenceSelector


def duckDuckGoBangsRemover(searchQuery):
  reversedQuery = searchQuery[::-1]
  newQuery = reversedQuery.replace("!", "!\\",1)[::-1]
  return newQuery

def evidenceCollector(inputClaim, urlBanList, cosineSimilarityModel):

  try:
    filteredSearchResults = webSearcher(inputClaim, urlBanList)
  except AssertionError:
    inputClaim = duckDuckGoBangsRemover(inputClaim)
    filteredSearchResults = webSearcher(inputClaim, urlBanList)
  
  if len(filteredSearchResults[0]) == 0:
    topEvidences = [[],[],[],[]]
    highestSimilarityScores = []
  else:
    topEvidences, highestSimilarityScores = evidenceSelector(inputClaim, filteredSearchResults, cosineSimilarityModel)

  return topEvidences, highestSimilarityScores
