import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # .env 파일 불러오기

# 1. 직무 데이터 불러오기
def load_jobs():
    with open("job.json", "r", encoding="utf-8") as f:
        return json.load(f)

# 2. 이력서와 직무 매칭 (RAG 검색 핵심!)
def search_jobs(resume_text):
    jobs = load_jobs()
    results = []

    for job in jobs:
        score = 0
        for keyword in job["keywords"]:
            if keyword.lower() in resume_text.lower():
                score += 1
        results.append({"job": job, "score": score})

    results.sort(key=lambda x: x["score"], reverse=True)
    return results

# 4. LLM으로 분석 결과 생성
def recommend_job(job_posting, career_summary):  # ⭐ 인자 2개로!
    # 경력요약으로 직무 검색
    matches = search_jobs(career_summary)
    top_job = matches[0]["job"]

    # .env 파일의 API 키 불러오기
    api_key = os.getenv("CODYSSEY_API_KEY")

    # 🔍 API 키 확인
    if not api_key:
        print("❌ API 키를 못 불러왔어요! .env 파일의 키 이름을 확인하세요!")
        return None
    print("✅ API 키 확인 (앞 8자리):", api_key[:8])

    # ⭐ 프론트가 원하는 JSON 형식으로 답변 요청!
    prompt = f"""
당신은 취업 코치입니다. 아래 정보를 분석해주세요.

[채용공고]
{job_posting}

[지원자 경력요약]
{career_summary}

[가장 관련 있는 직무]
{top_job['title']} - {top_job['description']}

위 정보를 바탕으로 다음 JSON 형식으로만 답변하세요.
설명이나 다른 말 없이 순수 JSON만 출력하세요:

{{
  "strengths": ["강점1", "강점2", "강점3"],
  "gaps": ["부족한점1", "부족한점2"],
  "next_actions": ["다음행동1", "다음행동2", "다음행동3"],
  "evidence": ["근거1", "근거2"]
}}
"""

    response = requests.post(
        "https://copa.codyssey.kr/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "gpt-5-mini",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    # 🔍 API 응답 확인
    print("API 응답 전체:", response.json())

    # LLM 답변 텍스트 꺼내기
    content = response.json()["choices"][0]["message"]["content"]

    # ⭐ 텍스트를 JSON(딕셔너리)으로 변환!
    result = json.loads(content)
    return result

# 테스트
if __name__ == "__main__":
    job = "Python 백엔드 개발자를 찾습니다. FastAPI 경험 필수"
    career = "저는 Python과 FastAPI로 API를 개발했습니다"
    result = recommend_job(job, career)
    if result:
        print("강점:", result["strengths"])
        print("부족한 점:", result["gaps"])