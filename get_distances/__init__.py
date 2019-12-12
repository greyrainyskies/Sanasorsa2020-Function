import json

import azure.functions as func

from gensim.models import Word2Vec

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Parse Http-request body into original word and an array of guessed words:
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("No JSON data found in the request body.", status_code=400) # If no body is found, return 400 Bad Request
    else:
        original = req_body.get('original')
        guesses = req_body.get('guesses')
    
    # If format is wrong, return 400 Bad Request
    if original and guesses:
        # Load Word2Vec model
        model = Word2Vec.load('data/vectors.model')
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

        return func.HttpResponse(json.dumps(similarities))
    else:
        return func.HttpResponse("The format of the JSON request was invalid.", status_code=400)

    # model = Word2Vec.load('data/wikiW2Vtest.model')

    # wv = model.wv

    # if in wv:
    #     model.w

    # # result = model.wv.similarity('hkj', 'sukkula')

    # # model = KeyedVectors.load('get_distances/keyed.txt')

    # # vector = model.wv['avaruussukkula']

    # logging.info(result)
    # return func.HttpResponse(str(result))

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello {name}!")
    # else:
    #     return func.HttpResponse(
    #          "Please pass a name on the query string or in the request body",
    #          status_code=400
    #     )
