from webSearcher import webSearcher
from evidenceSelector import evidenceSelector


def evidenceCollector(inputClaim, urlBanList, cosineSimilarityModel):

  filteredSearchResults = webSearcher(inputClaim, urlBanList)
  
  if len(filteredSearchResults[0]) == 0:
    topEvidences = [[],[],[],[]]
    highestSimilarityScores = []
  else:
    topEvidences, highestSimilarityScores = evidenceSelector(inputClaim, filteredSearchResults, cosineSimilarityModel)

  return topEvidences, highestSimilarityScores
