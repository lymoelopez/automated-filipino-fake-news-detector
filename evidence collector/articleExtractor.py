from newspaper import Article
from newspaper import Config


def articleExtractor(url, articleExtractorConfig):

  try:
    article = Article(url, config=articleExtractorConfig)
    article.download()
    article.parse()
  except:
    return ""

  return article.text

def createExtractedArticlesList(urlList):

  extractedArticlesList = []

  articleExtractorConfig = Config()
  articleExtractorConfig.requests_timeout = 30

  for url in urlList:
    extractedArticlesList.append(articleExtractor(url, articleExtractorConfig))

  return extractedArticlesList