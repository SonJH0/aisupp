#  AI 취업 코치 (AI Career Coach)

> LLM과 RAG 기반의 개인 맞춤형 AI 취업 코칭 서비스

[![Frontend](https://img.shields.io/badge/Frontend-Vercel-black)](https://aisupp.vercel.app)
[![Backend](https://img.shields.io/badge/Backend-Render-purple)](https://aisupp.onrender.com)

🔗 **서비스 바로가기:** [https://aisupp.vercel.app](https://aisupp.vercel.app)


##  프로젝트 개요

**AI 취업 코치**는 취업 준비생의 스펙과 경력을 분석하여
개인 맞춤형 직무 추천과 취업 상담을 제공하는 풀스택 AI 서비스입니다.

사용자가 보유 자격증·경력을 입력하면, AI Agent가 상황을 판단해
**이력서 분석 / 직무 검색(RAG) / 취업 상담** 중 최적의 기능을
자동으로 수행합니다.

###  해결하고자 한 문제
- 취업 준비생이 자신의 강점·약점을 객관적으로 파악하기 어려움
- 방대한 직무 정보 속에서 적합한 직무를 찾기 힘듦
- 개인 맞춤형 취업 상담을 받을 기회가 부족함

---

##  요구사항 명세서

### 1. 기능 요구사항 (Functional Requirements)

| ID | 요구사항 | 상세 설명 | 수용 기준 (Acceptance Criteria) | 상태 |
|----|----------|-----------|-------------------------------|:----:|
| FR-01 | 스펙 분석 | 사용자 자격증/경력 입력 시 강점·약점 분석 | 강점/약점/다음행동/근거 4개 항목 출력 | ✅ |
| FR-02 | 직무 추천 (RAG) | job.json 기반 관련 직무 검색 | 입력 키워드와 매칭되는 직무 반환 | ✅ |
| FR-03 | AI 상담 채팅 | 취업 관련 질의응답 | 질문 의도에 맞는 답변 제공 | ✅ |
| FR-04 | AI Agent 자동 분기 | 입력 유형에 따라 도구 자동 선택 | analyze/search/chat 중 자동 실행 | ✅ |
| FR-05 | 응답 화면 표시 | 분석 결과를 프론트에 시각화 | 카드 형태 UI로 결과 출력 | ✅ |

### 2. 비기능 요구사항 (Non-Functional Requirements)

| ID | 요구사항 | 수용 기준 | 상태 |
|----|----------|-----------|:----:|
| NFR-01 | 응답 속도 | 평균 응답 3초 이내 | ✅ |
| NFR-02 | 안정성 | Error Rate 1% 미만 | ✅ (0%) |
| NFR-03 | 가용성 | 24시간 무중단 서비스 | ✅ |
| NFR-04 | 보안 | API Key 환경변수 관리 (.env 제외) | ✅ |
| NFR-05 | 배포 | 클라우드 배포 및 외부 접속 가능 | ✅ |

---

##  팀 구성 및 기여도

| 이름 | 역할 | 담당 업무 |
|------|------|-----------|
| **손재윤** | Frontend | 전체적인 인터페이스 및 대시보드 개발 |
| **황준식** | AI/Data | RAG 파이프라인 및 프롬프트 설계 |
| **손재형** | Backend | AI Agent 개발 및 API 설계 |


---

##  브랜치 전략

본 프로젝트는 **기능별 브랜치 전략(Git Flow)**을 사용했습니다.

| 브랜치 | 용도 | 담당 |
|--------|------|------|
| `main` | 배포용 안정 버전 | 공통 |
| `feature/frontend` | 프론트엔드 개발 | 손재윤 |
| `feature/ai-rag` | RAG 파이프라인 | 황준식 |
| `feature/backend-agent` | AI Agent/API | 손재형 |


---

## 🛠️ 기술 스택

### Frontend
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

### Backend
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)

### AI / Data
![OpenAI](https://img.shields.io/badge/gpt--5--mini-412991?logo=openai&logoColor=white)
- RAG (Retrieval-Augmented Generation)
- Prompt Engineering

### Deployment
![Vercel](https://img.shields.io/badge/Vercel-000000?logo=vercel&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?logo=render&logoColor=white)

###  기술 선택 근거
| 기술 | 선택 이유 |
|------|-----------|
| **FastAPI** | 비동기 처리 지원, 자동 API 문서화(Swagger), 빠른 개발 속도 |
| **Vercel** | 프론트 배포 최적화, 자동 CI/CD, 무료 SSL |
| **Render** | Python 서버 배포 간편, 무료 티어 제공 |
| **RAG** | LLM 환각(hallucination) 감소, 근거 기반 답변 |

---

##  서비스 아키텍처

```
┌─────────────┐
│   사용자      │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│   Frontend (Vercel)  │
│   aisupp.vercel.app  │
│   - 분석 화면          │
│   - 채팅 인터페이스     │
└──────────┬──────────┘
           │ HTTP Request
           ▼
┌───────────────────────────┐
│   Backend (Render)         │
│   aisupp.onrender.com      │
│   - FastAPI 서버            │
└──────────┬────────────────┘
           │
           ▼
┌───────────────────────────┐
│   🤖 AI Agent (도구 자동선택) │
│   ┌──────────┐             │
│   │ analyze  │ 이력서 분석   │
│   │ search   │ 직무검색(RAG) │
│   │ chat     │ 취업 상담     │
│   └──────────┘             │
└──────────┬────────────────┘
     ┌─────┴─────┐
     ▼           ▼
┌─────────┐  ┌──────────┐
│job.json │  │gpt-5-mini│
│(RAG DB) │  │  (LLM)   │
└─────────┘  └──────────┘
```

---

##  활용 방식

### 1. AI Agent (도구 자동 선택)
| 도구 | 기능 | 예시 |
|------|------|------|
| `analyze` | 이력서/스펙 분석 | "토익 900, 컴활 1급" |
| `search` | 직무 검색 (RAG) | "백엔드 직무 추천" |
| `chat` | 일반 취업 상담 | "면접 준비 어떻게?" |

### 2. RAG (Retrieval-Augmented Generation)
- `job.json` 직무 데이터베이스 기반 키워드 매칭
- 사용자 스펙과 관련성 높은 직무를 검색하여 근거 있는 추천 제공


### 3. Prompt Engineering
- JSON 형식의 구조화된 답변 설계 (강점/약점/다음행동/근거)
- 취업 코치 페르소나 부여로 전문적인 상담 품질 확보

---

##  실행 방법

### 1️⃣ 저장소 클론
```bash
git clone https://github.com/SonJH/aisupp.git
cd aisupp
```

###  백엔드 실행
```bash
cd backend
pip install -r requirements.txt

# 환경변수 설정 (.env 파일 생성)
echo "CODYSSEY_API_KEY=your_api_key" > .env

# 서버 실행
uvicorn main:app --reload
```
→ 백엔드 접속: `http://localhost:8000`
→ API 문서(Swagger): `http://localhost:8000/docs`

###  프론트엔드 실행
```bash
cd frontend
# index.html 파일을 브라우저로 열기 (Live Server 권장)
```
→ 프론트 접속: `http://localhost:5500`

---

##  실행 결과 및 테스트 증거

###  1. 배포 상태 증빙

vercel
```
<img width="1877" height="922" alt="image" src="https://github.com/user-attachments/assets/14452ae4-f041-44c7-816b-7e59ca984383" />

```
```
Status: Ready ●  (초록불)
URL: aisupp.vercel.app
Source: main (63a0e20)
```

render
```
<img width="1856" height="911" alt="image" src="https://github.com/user-attachments/assets/731e70ee-9270-4d8c-97a6-5a9264334e0d" />

```
```
Status: Live ●
URL: aisupp.onrender.com
```

###  2. API 테스트 로그

**분석 API 요청/응답 테스트:**
```bash
# 요청
$ curl -X POST https://aisupp.onrender.com/recommend \
  -H "Content-Type: application/json" \
  -d '{"query": "토익 900, 컴활 1급, 한국사 1급"}'

# 응답 (HTTP 200 OK)
{
  "강점": [
    "토익 900 보유로 영문 자료 이해 능력 우수",
    "컴활 1급으로 컴퓨터 활용 기본 역량 보유"
  ],
  "부족한_점": ["백엔드 프로그래밍 언어 경험 부재"],
  "다음_행동": ["Spring/Django 등 백엔드 프레임워크 학습"],
  "근거": ["자격증 기반 역량 분석 결과..."]
}
```

**채팅 API 요청/응답 테스트:**
```bash
# 요청
$ curl -X POST https://aisupp.onrender.com/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "공기업 면접 준비 어떻게?"}'

# 응답 (HTTP 200 OK)
{
  "reply": "공기업 면접은 NCS 기반으로...",
  "tool_used": "chat"
}
```

스크린샷
```
<img width="1240" height="788" alt="image" src="https://github.com/user-attachments/assets/246c07b3-ecd1-4eed-8667-bb046506d35f" />

<img width="1246" height="802" alt="image" src="https://github.com/user-attachments/assets/63977981-3927-4b8c-947f-225b7468e228" />

<img width="698" height="606" alt="image" src="https://github.com/user-attachments/assets/1218e339-3588-4e2c-96f9-10ca9459e364" />

<img width="729" height="910" alt="image" src="https://github.com/user-attachments/assets/808b97fc-73ac-470a-8fe4-d32b25c2ca48" />

<img width="725" height="440" alt="image" src="https://github.com/user-attachments/assets/24e5d84f-821d-4a9e-ac8f-f541cd10f9d1" />

<img width="760" height="450" alt="image" src="https://github.com/user-attachments/assets/61cd6c03-78a0-41e5-a89f-37048e9bc6c6" />




```

### 3. 성능 지표

| 항목 | 결과 | 측정 방법 |
|------|------|-----------|
| API 응답 성공률 | **100%** | Vercel Analytics |
| Error Rate | **0%** | Vercel Dashboard |
| 평균 응답 시간 | 약 2~3초 | curl 응답 시간 측정(다만 무료 버전이라 처음 실행 시 평균보다 30초 정도 더 시간이 걸림 |

---

## 코드 품질 관리

리뷰 피드백을 반영하여 아래와 같이 코드를 정리했습니다.

### 1. 디버그 코드 제거
개발 중 사용한 `print()` 디버그 출력을 제거하고,
**표준 `logging` 모듈**로 전환했습니다.

**Before (디버그 코드)**
```python
# backend/rag.py
print("API 응답 전체:", response.json())  # 제거됨
```

**After (로깅 적용)**
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 운영 환경에 맞는 로그 레벨 관리
logger.info("API 요청 처리 완료")
logger.error("API 요청 실패", exc_info=True)
```

### 2. 에러 처리 강화
```python
try:
    response = call_api(query)
    logger.info("API 응답 성공")
    return response.json()
except Exception as e:
    logger.error(f"API 호출 오류: {e}", exc_info=True)
    return {"error": "요청 처리 중 오류가 발생했습니다."}
```

### 3. 린터(Linter) 적용
```bash
# 코드 스타일 통일
$ pip install flake8 black
$ black backend/        # 자동 포맷팅
$ flake8 backend/       # 스타일 검사
```

---

## 사용자 피드백 

실제 사용자 5명을 대상으로 서비스를 제공하고 피드백을 수집했습니다.

| 사용자 | 피드백 | 만족도 |
|--------|-----------|-----------:|
| A  |  내 자격증으로 어떤 직무가 맞는지 몰랐는데, 방향을 잡는 데 큰 도움이 됐습니다 | ⭐⭐⭐⭐⭐ |
| B  |  부족한 점을 콕 집어줘서 뭘 공부해야 할지 명확해졌습니다. | ⭐⭐⭐⭐⭐ |
| C  |  한 사이트에서 여러 기능을 쓸 수 있어서 편했어요. | ⭐⭐⭐⭐ |
| D  |  빠른 응답과 근거 있는 추천이 신뢰가 갔습니다. UI도 깔끔해요. | ⭐⭐⭐⭐⭐ |
| E  |  IT 직무 전환을 고민 중이었는데 학습 로드맵까지 제시해줘서 좋았어요. | ⭐⭐⭐⭐ |
### 📈 종합 만족도: **4.6 / 5.0**

** 긍정적 피드백**
- 개인 맞춤형 분석의 정확도가 높음
- 근거를 함께 제시해 신뢰도가 높음
- 직관적이고 깔끔한 UI

** 개선 요청 사항 및 반영**
| 요청 사항 | 반영 계획 |
|-----------|-----------|
| 첫 요청 시 응답 지연 (무료 서버) | 유료 인스턴스 검토 예정 |
| 분석 결과 저장/기록 기능 | DB 연동 예정 |
| 더 다양한 직무 데이터 | job.json 데이터 확장 예정 |

---

## 향후 개선 계획

- [ ] 분석 기록 저장 기능 (Database 연동)
- [ ] 직무 데이터베이스 확장
- [ ] 사용자 로그인 및 마이페이지
- [ ] 응답 속도 개선 (서버 업그레이드)
- [ ] 커스텀 도메인 연결

---

