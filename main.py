import uvicorn
from fastapi import FastAPI

from my_types import HelloWorldModel

app = FastAPI()


@app.get("/", response_model=HelloWorldModel)
def root():
    return {"Hello": "World"}


def main() -> None:
    print("===== main() =====")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, workers=2)


if __name__ == "__main__":
    main()

