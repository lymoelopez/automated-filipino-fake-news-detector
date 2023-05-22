from webSearcher import webSearcher
from findTopEvidences import findTopEvidences


def evidenceCollector(inputClaim, urlBanList, cosineSimilarityModel):

  urlList, urlBodyList = webSearcher(inputClaim, urlBanList)

  if len(urlList) == 0:
    topEvidences = []
    topEvidencesUrl = []
  else:
    topEvidences, topEvidencesUrl = findTopEvidences(inputClaim, urlBodyList, urlList, cosineSimilarityModel)

  return topEvidences, topEvidencesUrl
