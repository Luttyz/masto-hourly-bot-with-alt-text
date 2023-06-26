import json
import requests
import shutil 
from mastodon import Mastodon

retries = 0

# set the API's used URL
url = "https://api.tinyfox.dev/img?animal=capy"

r = requests.get(url, stream = True)

# This part definitely wasn't copy pasted and I definitely do understand what it does yes yes

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    with open("capybara.jpg",'wb') as f:
        shutil.copyfileobj(r.raw, f)
        
    print('Image sucessfully Downloaded')
else:
    print('Image couldn\'t be downloaded')

# request ML-based image recognition through Vercel's public CLIP-2 instance
# NOTE : this requires that the image that we have downloaded before this step
# ////// is on a PUBLIC web server, that Vercel can access, for the sake of
# ////// example, in this case, this will be the URL i'll use for the Capy bot

while True:

 APIANSWER = requests.get("https://alt-text-generator.vercel.app/api/generate?imageUrl=https://webserver-url.example/capybara.jpg")
 IMGRECresponse = APIANSWER.text

 if "EDGE_FUNCTION_INVOCATION_TIMEOUT" in IMGRECresponse:
   # Handle the error
   print("The edge function timed out")
   # Retry using the same API URL and parameters
   retries += 1
   if retries == 5:
     print("API failed to provide alt text within 5 tries")
     raise Exception("API failure, not posting")
   else:
     print("Retrying...")
     APIANSWER = requests.get("https://alt-text-generator.vercel.app/api/generate?imageUrl=https://webserver-url.example/capybara.jpg")
 else:
   IMGRECresponse = APIANSWER.text
   print(IMGRECresponse)
   alt_text = IMGRECresponse.replace('Caption: ', '').replace('\"','').replace('animal','capybara').replace('monkey','capybara').replace('rodent','capybara')
   print(alt_text)
   # NOTE : the last .replace with "animal" is because CLIP-2 struggles to recognize
   # capybaras from time to time, this is a very weird solution, but shush
   break

# Send through Mastodon server (used in example : my own server)
mastodon = Mastodon(
    access_token = 'dummy-access-token-GO-GET-YOUR-OWN',
    api_base_url = 'https://instance.example'
)
# if needed : the masto.ml instance (my own) is bot-friendly, as long as asked before creating the account and posted in unlisted, and botsin.space was specifically made for bots

# Upload image and get media ID
media = mastodon.media_post('capybara.jpg', description=alt_text, mime_type="image/jpeg")

# Post status with media ID and alt text
mastodon.status_post('Here\'s an image of a #Capybara! #HourlyAnimals', media_ids=[media])
