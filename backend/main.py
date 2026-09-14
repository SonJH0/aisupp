from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag import recommend_job      # ⭐ RAG 추천 함수
from agent import run_agent        # ⭐ Agent 함수

app = FastAPI()

# 🔓 CORS 설정 (프론트엔드가 접근 가능하도록)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # 모든 주소 허용 (개발용)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# 📥 데이터 형식 정의
# ==========================================

# 이력서 추천용
class ResumeRequest(BaseModel):
    job_posting: str      # 채용공고
    career_summary: str   # 경력요약

# 채팅(Agent)용
class ChatRequest(BaseModel):
    message: str              # 사용자 질문
    career_summary: str = ""  # 경력 (선택)


# ==========================================
# 🏠 서버 작동 확인용
# ==========================================
@app.get("/")
def home():
    return {"message": "AI 취업 코치 서버 작동중! 🚀"}


# ==========================================
# 🎯 추천 API (RAG 기반 직무 추천)
# ==========================================
@app.post("/recommend")
def recommend(request: ResumeRequest):
    result = recommend_job(request.job_posting, request.career_summary)
    return result


# ==========================================
# 🤖 Agent API (스스로 도구 선택!)
# ==========================================
@app.post("/chat")
def chat(request: ChatRequest):
    result = run_agent(request.message, request.career_summary)
    return result