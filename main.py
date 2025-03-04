from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "🚀 FastAPI 運行成功！"}

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 10000))  # 確保 PORT 變數存在
    uvicorn.run(app, host="0.0.0.0", port=port)
