from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, pipeline, AutoModelForSeq2SeqLM, AutoModelForSequenceClassification


def automatedFakeNewsConfig(
    urlBanList = ["facebook.com", "twitter.com", "youtube.com", "blogspot.com", "tiktok.com", 
                  "instagram.com", "youtu.be","spotify.com", "slideshare.net", "github.com", "huggingface.com,", 
                  "reddit.com", "bible.com", "dailymotion.com", "/opinyon", "/opinion", 
                  "brainly.com", "quizlet.com", "dutertedefender.com", "dutertenews.com",
                  "du30worldwide.com", "du30newsblog.blogspot.com", "trendingbalita.info", 
                  "pinoyviralissues.net", "pinoyspeak.info", "newstitans.com", "mindanation.com", 
                  "phppoliticsnews.blogspot.com", "tahonews.com", "pinoynewsblogger.blogspott.com", 
                  "liberalpartysite.wordpress.com", "pinoyworld.net", "newsmediaph.com", 
                  "thevolatiliian.com", "socialnewsph.com", "leaknewsph.com", "du30newsinfo.com", 
                  "hotnewsphil.blogspot.com", "iampilipino.com", "trendingnewsportal-ph.blogspot.com", 
                  "kalyepinoy.com", "classifiedtrents.net", "ilikeyquotes.blogspot.com", "filipinewsph.com", 
                  "newsfeedsociety.tk", "pinoyfreedomwall.com", "philnewsportal.com", "ilikeyouquotes.blogspot.com", 
                  "pinoytrending.altervista.org", "pinoytrendingnews.net", "newstrendph.com", "asianpolicy.press", 
                  "publictrending.net", "trendingviral.tk", "newsinfolearn.com", "allthingspinoy.com", "todayinmanila.ga", 
                  "definitelyfilipino.com", "trendingnewsportal.net", "classifiedtrends.net", "philippinesinfinity.com", 
                  "reportph.com", "topnewsphil.com", "pilipinasnewsnetwork.com", "du30newsportal.com", "bidyoko.com", 
                  "philnewstrend.com", "food-health-365.com", "netizensph.com", "superworld18.xyz", "rap-fr.fr", 
                  "real8scoop.blogspot.com", "netviral.com", "ignitepinoy.com", "angatpinoy.info", "viralhubph.com", 
                  "artikuloph.com", "balitaph.info", "globalnews.favradiofm.com", "globalnews.favradio.fm", "themaharlikan.info", 
                  "inewser.com", "pinoythinking.info", "duterteviral.info", "balitangpinas.net", "okd2.com", "bbc101.c0m", 
                  "dwtcv3.com", "da1lymail.com", "thet1mes.com", "guard1an.com", "ondamic.com", "da1lymail.com", 
                  "sowhatsnews.wordpress.com", "adobochronicles.com", "thephilippinechronicle.com", "Balitangmaharlika.com", 
                  "GetRealPhilippines.com", "Thinkingpinoy.net", "Pinasheadlines.com", "Pinoytribune.blogspot.com", 
                  "trendsenthusiast.blogspot.com", "Newsinfomanila.com", "MNLTrend.blogspot.com", "Tribune.net.ph", 
                  "amazon.com", "olx.com", "wattpad.com", "ask.fm", "ebay.com", "twitch.tv", "discord.com"],
    cosineSimilarityModelID = "danjohnvelasco/filipino-sentence-roberta-v1", 
    transformerModel = "jcblaise/electra-tagalog-small-uncased-discriminator-newsphnli",
):
  
  cosineSimilarityModel = SentenceTransformer(cosineSimilarityModelID)
  
  entailmentClassifierTokenizer = AutoTokenizer.from_pretrained(transformerModel)
  entailmentClassifierModel = AutoModelForSequenceClassification.from_pretrained(transformerModel)
  entailmentClassifier = [entailmentClassifierTokenizer, entailmentClassifierModel]
  
  return urlBanList, cosineSimilarityModel, entailmentClassifier
