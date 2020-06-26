from fastapi import FastAPI
from pydantic import BaseModel
from imageDiff import ImageDiff

from fastapi.middleware.cors import CORSMiddleware

file_A, file_B = "a.jpg", "b.jpg"
res1, res2, similarity_score = ImageDiff(file_A, file_B, './static/')
app = FastAPI()

# Access-Control-Allow-Origin
origins = [
    "http://localhost:8000",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Access-Control-Allow-Origin end

@app.get("/")
def read_root():
    return {"FastAPI": "FastAPI Python APP"}

@app.get("/imagediff")
async def read_imgdiff():
    return {
        "image_1": file_A,
        "image_2": file_B, 
        "result_1": res1,
        "result_2": res2,
        "similarity": similarity_score
    }
