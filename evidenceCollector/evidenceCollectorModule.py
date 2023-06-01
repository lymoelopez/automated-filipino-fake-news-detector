from webSearcher import webSearcher
from evidenceSelector import evidenceSelector


def evidenceCollector(inputClaim, urlBanList, cosineSimilarityModel):

  urlList, urlContentList = webSearcher(inputClaim, urlBanList)

  if len(urlList) == 0:
    topEvidences = []
    topEvidencesUrl = []
  else:
    topEvidences, topEvidencesUrl = evidenceSelector(inputClaim, urlContentList, urlList, cosineSimilarityModel)

  return topEvidences, topEvidencesUrl
