from fastapi import FastAPI, HTTPException, status

app = FastAPI()

predictor = None


@app.on_event("startup")
def load_predictor():
    global predictor
    # TODO: load predictor here
    predictor = 1


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health", status_code=status.HTTP_200_OK)
def healthcheck():
    return {"healthcheck": "Everything's OK!"}


@app.post("/predictions")
def predictions():
    try:
        return {"predictor": predictor}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
