from fastapi import FastAPI
from pydantic import BaseModel
from imageDiff import ImageDiff

file_A, file_B = "a.jpg", "b.jpg"
res1, res2, similarity_score = ImageDiff(file_A, file_B, './static/')
app = FastAPI()

@app.get("/")
def read_root():
    return {
        "image_1": file_A,
        "image_2": file_B, 
        "result_1": res1,
        "result_2": res2,
        "similarity": similarity_score
    }
