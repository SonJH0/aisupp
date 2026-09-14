import os
import json
import requests
from dotenv import load_dotenv
from rag import recommend_job, search_jobs  # ⭐ 기존 함수 재활용!

load_dotenv()

# 🔧 LLM 호출 공통 함수 (rag.py 방식 그대로!)
def call_llm(prompt):
    api_key = os.getenv("CODYSSEY_API_KEY")
    response = requests.post(
        "https://copa.codyssey.kr/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "gpt-5-mini",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return response.json()["choices"][0]["message"]["content"]


# 🧠 1단계: LLM이 도구를 선택 (Agent의 핵심!)
def choose_tool(user_message):
    prompt = f"""
사용자 질문을 분석해서 필요한 작업을 하나만 고르세요.

[판단 기준]
- analyze : 내 경력/이력서를 분석하거나 "될 수 있을까?" 평가받고 싶을 때
            (예: "제 경력으로 백엔드 될 수 있나요?", "이 이력서 어때요?", "저 어때요?")
- search : 특정 직무 정보를 찾을 때
           (예: "백엔드 개발자란?", "FastAPI 직무 찾아줘", "프론트엔드 알려줘")
- chat : 일반적인 취업 상담, 조언, 팁을 원할 때
         (예: "면접 팁 알려줘", "긴장 어떻게 풀어?", "이력서 쓰는 법")

사용자 질문: "{user_message}"

위 3개 중 하나의 단어만 답하세요 (analyze/search/chat):
"""
    tool = call_llm(prompt).strip().lower()
    return tool


# 💬 도구 3: 일반 취업 상담
def general_chat(user_message):
    prompt = f"""
당신은 친절한 취업 코치입니다.
아래 질문에 도움이 되는 조언을 2~3문장으로 답해주세요.

질문: {user_message}
"""
    answer = call_llm(prompt)
    return {"answer": answer}


# 🔍 도구 2: 직무 검색 (결과 정리)
def job_search(keyword):
    matches = search_jobs(keyword)
    # 상위 3개만 정리
    top3 = matches[:3]
    jobs = [
        {"title": m["job"]["title"],
         "description": m["job"]["description"],
         "score": m["score"]}
        for m in top3
    ]
    return {"matched_jobs": jobs}


# 🤖 메인 Agent (판단 → 도구 실행)
def run_agent(user_message, career_summary=""):
    # 1단계: LLM이 도구 선택
    tool = choose_tool(user_message)
    print(f"🤖 Agent가 선택한 도구: {tool}")

    # 2단계: 선택된 도구 실행
    if "analyze" in tool:
        # 이력서 분석 (기존 recommend_job 함수!)
        result = recommend_job(user_message, career_summary)
        return {"tool_used": "이력서분석", "result": result}

    elif "search" in tool:
        # 직무 검색
        result = job_search(user_message)
        return {"tool_used": "직무검색", "result": result}

    else:
        # 일반 상담
        result = general_chat(user_message)
        return {"tool_used": "일반상담", "result": result}


# 🧪 테스트
if __name__ == "__main__":
    print("=" * 50)
    print("테스트 1: 이력서 분석 질문")
    print(run_agent("제 경력으로 백엔드 개발자 될 수 있을까요?",
                    "Python과 FastAPI로 API를 개발했습니다"))

    print("=" * 50)
    print("테스트 2: 직무 검색 질문")
    print(run_agent("FastAPI 관련 직무 찾아줘"))

    print("=" * 50)
    print("테스트 3: 일반 상담 질문")
    print(run_agent("면접 볼 때 긴장을 안 하려면 어떻게 해야 하나요?"))