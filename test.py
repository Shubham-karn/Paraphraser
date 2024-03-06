from parrot import Parrot
from fastapi import FastAPI
import warnings
warnings.filterwarnings("ignore")

app = FastAPI()

parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

@app.get("/paraphrase/")
async def read_paraphrase(phrase: str):
    para_phrases = parrot.augment(input_phrase=phrase, use_gpu=False, max_return_phrases = 10)
    return {"paraphrases": para_phrases}