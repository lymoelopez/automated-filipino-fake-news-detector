def findLLMmmessage(evidence, claim, llmWithPromptTemplate):
  message = llmWithPromptTemplate.run({"evidence": evidence, "claim": claim})
  return message

def llmClassifier (inputClaim, evidence, llmWithPromptTemplate):
  
  message = findLLMmmessage(evidence, inputClaim, llmWithPromptTemplate)

  if ("true" in message.strip().lower()) or ("yes" in message.strip().lower()):
    return 0
  else:
    return 1
