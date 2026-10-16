from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import subprocess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Streamgrabber API is running. Use /get-stream?imdb_id=YOUR_ID"}

@app.get("/get-stream")
def get_stream(imdb_id: str):
    try:
        result = subprocess.run(
            ["streamgrabber", imdb_id, "--list"],
            capture_output=True,
            text=True,
            check=True
        )
        stream_url = result.stdout.strip()
        if not stream_url:
            raise HTTPException(status_code=404, detail="No stream links detected.")
        return {"imdb_id": imdb_id, "m3u8_url": stream_url}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Extraction failed: {e.stderr or e.stdout}")
