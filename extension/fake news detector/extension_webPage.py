from flask import Blueprint, render_template, request
from automatedFakeNewsDetector_module import automatedFakeNewsPipeline


webPage = Blueprint('webPage', __name__)

@webPage.route('/')
def homePage(withErrorMessage=False):
    return render_template('homePage.html', withErrorMessage=withErrorMessage)

@webPage.route('/', methods=['POST'])
def fakeNewsPredictionRequest():
    
    inputClaim = request.form['text']

    if inputClaim == "":
        return homePage(withErrorMessage=True)
    else:
        return render_template('loadingScreen.html', inputClaim=inputClaim)

@webPage.route('/prediction')
def fakeNewsPredictionMessage():
    
    inputClaim = str(request.args.to_dict(flat=False)['inputClaim'][0])
    predictionDetails, topEvidencesDetails = automatedFakeNewsPipeline(inputClaim)
    finalPrediction = predictionDetails[0]
    predictionPercentage =  predictionDetails[1]
    numberOfEvidences = topEvidencesDetails[3]
    
    if finalPrediction == 0:
        predictionMessage = "Real"
    else:
        predictionMessage = "Fake"
        
    return render_template('responsePage.html', inputClaim=inputClaim, predictionMessage=predictionMessage, predictionPercentage=predictionPercentage, topEvidencesDetails=topEvidencesDetails, numberOfEvidences=numberOfEvidences)
