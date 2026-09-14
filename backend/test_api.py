import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("CODYSSEY_API_KEY")

# 🔍 확인용: 키가 제대로 읽혔는지 체크
print("키 앞 10자리:", api_key[:10] if api_key else "❌ 키를 못 읽음!")

response = requests.post(
    "https://copa.codyssey.kr/v1/chat/completions",
    headers={"Authorization": f"Bearer {api_key}"},
    json={
        "model": "gpt-5-mini",
        "messages": [{"role": "user", "content": "안녕하세요"}],
    },
)

# 🔍 응답 전체를 출력해서 문제 확인
print("응답 전체:", response.json())