import requests
import base64

appId = "01GH72WYV283GVWHYW2VAZYBBR"
accessKey = "b597f6be-6dbe-4a0a-859a-0d605259648e"
accessSecret = "W~f5K5yF-lFBN_lk9.lu5Qja6R"
projectId = "82ee0b94-e39f-42e5-bb3d-353a07588059"
channel = "SMS"
identity = "+918858893156"
url = "https://us.conversation.api.sinch.com/v1/projects/" + projectId + "/messages:send"

data = accessKey + ":" + accessSecret
encodedBytes = base64.b64encode(data.encode("utf-8"))
accessToken = str(encodedBytes, "utf-8")

payload = {
  "app_id": appId,
  "recipient": {
      "identified_by": {
          "channel_identities": [
            {
                "channel": channel,
                "identity": identity
            }  
            ]
      }
  },
  "message": {
      "text_message": {
          "text": "Hello Mr. Pranav, we are looking for desperate people and who else comes to mind other than you. To make your life less miserable we are organising sperm donation camp in VIT near chancellor's office tommorrow @ 2 PM. You are a prime candidate so grab this one time chance you virgin!!! or die alone. \n We look forward for your sperm."
      }
  }  
}

headers = {
  "Content-Type": "application/json",
  "Authorization": "Basic " + accessToken
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(data)