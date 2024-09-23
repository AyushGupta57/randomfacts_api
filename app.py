from fastapi import FastAPI, HTTPException, Path
from json_dep import load_json
import random
from typing import Annotated
from pydantic import BaseModel
# import uvicorn

app = FastAPI()

facts_data = load_json()

class FactsFormat(BaseModel):
    ind: int
    fact: str

@app.get("/")
async def index():
    return {"Home": "Go to /docs for testing API"}

@app.get("/get-random-fact")
async def random_fact():
    return facts_data[str(random.randrange(0, len(facts_data)))]

@app.get("/get-n-random-facts/{n_facts}")
async def n_random_facts(n: int):
    ret_facts = dict()
    i = 0
    while i <= n:
        ran_num = str(random.randrange(0, len(facts_data)))
        if random_fact not in ret_facts.keys():
            ret_facts[ran_num] = facts_data[ran_num]
            i = i + 1
    print(ret_facts)
    return ret_facts


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)