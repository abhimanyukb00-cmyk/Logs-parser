from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

from timer import CodeTimer

from processor import Processor

app = FastAPI()
processor = Processor()

class LogBatch(BaseModel):
    log: list[str]

@app.post("/Parse-logs/")
def process_logs(logs: LogBatch):
    if not logs.log:
        raise HTTPException(status_code=400, detail="Log batch cannot be empty.")

    with CodeTimer("Log batch process time") as timer:
        result = processor.process_batch(logs.log)

        return{
            "Elapsed_time":timer.elapsed_time,
            "Processed_count":len(logs.log),
            "Result":result
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000, host="localhost")