from evidenceCollector_webSearcher import webSearcher
from evidenceCollector_evidenceSelector import evidenceSelector


def evidenceCollector(inputClaim, urlBanList, cosineSimilarityModel):
  
  filteredSearchResults = webSearcher(inputClaim, urlBanList)

  if len(filteredSearchResults[0]) == 0:
    topEvidences = [[],[],[],[]]
    highestSimilarityScores = []
  else:
    topEvidences, highestSimilarityScores = evidenceSelector(inputClaim, filteredSearchResults, cosineSimilarityModel)

  return topEvidences, highestSimilarityScores
