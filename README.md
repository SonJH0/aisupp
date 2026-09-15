#  AI 취업 코치 (AI Career Coach)

> LLM과 RAG 기반의 개인 맞춤형 AI 취업 코칭 서비스

[![Frontend](https://img.shields.io/badge/Frontend-Vercel-black)](https://aisupp.vercel.app)
[![Backend](https://img.shields.io/badge/Backend-Render-purple)](https://aisupp.onrender.com)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

🔗 **서비스 바로가기:** [https://aisupp.vercel.app](https://aisupp.vercel.app)

---

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

##  팀 구성

| 이름 | 역할 | 담당 업무 |
|------|------|-----------|
| **손재윤** | Frontend | 전체적인 인터페이스 및 대시보드 개발 |
| **황준식** | AI/Data | RAG 파이프라인 및 프롬프트 설계 |
| **손재형** | Backend | AI Agent 개발 및 API 설계 |

---

##  기술 스택

### Frontend
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

### Backend
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?logo=gunicorn&logoColor=white)

### AI / Data
![OpenAI](https://img.shields.io/badge/gpt--5--mini-412991?logo=openai&logoColor=white)
- RAG (Retrieval-Augmented Generation)
- 코디세이 API 연동
- Prompt Engineering

### Deployment
![Vercel](https://img.shields.io/badge/Vercel-000000?logo=vercel&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?logo=render&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)

---

##  실행 방법

### 1️⃣ 저장소 클론
```bash
git clone https://github.com/SonJH/aisupp.git
cd aisupp
```

### 2️⃣ 백엔드 실행
```bash
cd backend
pip install -r requirements.txt

# 환경변수 설정 (.env 파일 생성)
echo "CODYSSEY_API_KEY=your_api_key" > .env

# 서버 실행
uvicorn main:app --reload
```

### 3️⃣ 프론트엔드 실행
```bash
cd frontend
# index.html 파일을 브라우저로 열기
# 또는 Live Server 사용
```
→ 백엔드, 프론트엔드 접속: `http://localhost:5500`

---

##  서비스 아키텍처

```
┌─────────────┐
│   사용자      │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│   Frontend (Vercel) │
│   aisupp.vercel.app │
│   - 분석 화면        │
│   - 채팅 인터페이스   │
└──────────┬──────────┘
           │ HTTP Request
           ▼
┌───────────────────────────┐
│   Backend (Render)        │
│   aisupp.onrender.com     │
│   - FastAPI 서버           │
│   - /recommend  /chat      │
└──────────┬────────────────┘
           │
           ▼
┌───────────────────────────┐
│    AI Agent               │
│   (도구 자동 선택)          │
│   ┌──────────┐             │
│   │ analyze  │ 이력서 분석   │
│   │ search   │ 직무 검색(RAG)│
│   │ chat     │ 취업 상담     │
│   └──────────┘             │
└──────────┬────────────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
┌─────────┐  ┌──────────┐
│job.json │  │gpt-5-mini│
│(RAG DB) │  │  (LLM)   │
└─────────┘  └──────────┘
```

---

##  AI 활용 방식

### 1. AI Agent (도구 자동 선택)
사용자의 입력을 분석하여 3가지 도구 중 최적의 기능을 자동 실행합니다.

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

##  실행 결과

### 분석 기능
사용자 스펙 입력 시 **강점 · 부족한 점 · 다음 행동 · 근거**를
체계적으로 분석하여 제공합니다.

```
예시

<img width="793" height="884" alt="image" src="https://github.com/user-attachments/assets/f1e838ec-5675-4153-baf5-71d66792f8d0" />

<img width="738" height="433" alt="image" src="https://github.com/user-attachments/assets/91bf6af9-d63f-491a-8ddf-56bbd36e2e49" />


```

### 채팅 상담 기능
AI Agent가 질문 의도를 파악하여 전문적인 취업 상담을 제공합니다.

### 성능 지표
| 항목 | 결과 |
|------|------|
| API 응답 성공률 | **100%** (200 OK) |
| Error Rate | **0%** |
| 평균 응답 시간 | 약 2~3초 |

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

**긍정적 피드백**
- 개인 맞춤형 분석의 정확도가 높음
- 근거를 함께 제시해 신뢰도가 높음
- 직관적이고 깔끔한 UI

**개선 요청 사항**
- 첫 요청 시 응답 지연 (무료 서버 특성) → 향후 유료 인스턴스 검토
- 분석 결과 저장/기록 기능 요청 → DB 연동 예정
- 더 다양한 직무 데이터 추가 요청
- 조금 더 높은 버전의 ai를 사용함으로써 답변에 대한 품질을 높일 것

---
