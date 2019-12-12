import json
import pathlib

import azure.functions as func

from gensim.models import Word2Vec

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Parse Http-request body into original word and an array of guessed words:
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("No JSON data found in the request body.", status_code=400) # If no body is found, return 400 Bad Request
    else:
        original = req_body.get('original').lower() # Putting inputs to lower-case, just in case
        guesses = [x.lower() for x in req_body.get('guesses')]
    
    # If format is wrong, return 400 Bad Request
    if original and guesses:
        # Load Word2Vec model
        model = Word2Vec.load(str(pathlib.Path(__file__).parent / 'vectors.model'))
        wv = model.wv

        # Check that the original word is in model
        if original not in wv:
            return func.HttpResponse("The original word is not in the dictionary.", status_code=400)
        # Return similarities for each guess
        similarities = []
        for guessed_word in guesses:
            # Check if guess is in the model, otherwise return 0
            if guessed_word in wv:
                similarities.append(str(wv.similarity(original, guessed_word)))
            else:
                similarities.append(str(0))

        return func.HttpResponse(json.dumps({"original": original, "distances":similarities}))
    else:
        return func.HttpResponse("The format of the JSON request was invalid.", status_code=400)