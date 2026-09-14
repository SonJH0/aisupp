// 1. HTML 요소들을 미리 찾아두기
const analyzeBtn = document.getElementById("analyzeBtn");
const jobPosting = document.getElementById("jobPosting");
const careerSummary = document.getElementById("careerSummary");

const statusArea = document.getElementById("statusArea");
const statusMessage = document.getElementById("statusMessage");
const resultArea = document.getElementById("resultArea");

const strengthsList = document.getElementById("strengthsList");
const gapsList = document.getElementById("gapsList");
const nextActionsList = document.getElementById("nextActionsList");
const evidenceList = document.getElementById("evidenceList");

// 2. 버튼 클릭 이벤트 등록
analyzeBtn.addEventListener("click", async () => {
  // 2-1. 입력값 확인
  if (jobPosting.value.trim() === "" || careerSummary.value.trim() === "") {
    alert("채용공고와 경력 요약을 모두 입력해 주세요.");
    return; // 여기서 함수 종료
  }

  // 2-2. 이전 결과 숨기고 "분석 중" 표시
  resultArea.hidden = true;
  statusArea.hidden = false;
  statusMessage.textContent = "분석 중입니다... ⏳";

  try {
    // 2-3. 백엔드 API 호출 (실제 서버!)
    const response = await fetch("http://127.0.0.1:8000/recommend", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        job_posting: jobPosting.value,       // 채용공고 전송
        career_summary: careerSummary.value, // 경력요약 전송
      }),
    });

    const data = await response.json();

    // 2-4. 결과 화면에 채우기
    renderResult(data);

    // 2-5. 상태 숨기고 결과 보여주기
    statusArea.hidden = true;
    resultArea.hidden = false;
  } catch (error) {
    // 2-6. 오류 처리
    statusMessage.textContent = "❌ 분석 중 오류가 발생했습니다.";
    console.error(error);
  }
});

// 3. 결과를 화면에 그리는 함수
function renderResult(data) {
  fillList(strengthsList, data.strengths);
  fillList(gapsList, data.gaps);
  fillList(nextActionsList, data.next_actions);
  fillList(evidenceList, data.evidence);
}

// 4. 배열을 받아 <li>로 채우는 도우미 함수
function fillList(ulElement, items) {
  ulElement.innerHTML = ""; // 기존 내용 비우기
  items.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    ulElement.appendChild(li);
  });
}


// ===== 여기부터 채팅 기능 =====

// 1. 채팅 요소 찾기
const chatInput = document.getElementById("chatInput");
const chatSendBtn = document.getElementById("chatSendBtn");
const chatMessages = document.getElementById("chatMessages");

// 2. 전송 버튼 클릭
chatSendBtn.addEventListener("click", sendChat);

// 3. 엔터키로도 전송 가능하게
chatInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") sendChat();
});

// 4. 채팅 전송 함수
async function sendChat() {
  const message = chatInput.value.trim();

  // 빈 입력 방지
  if (message === "") return;

  // 4-1. 사용자 질문 화면에 표시
  addMessage(message, "user");

  // 4-2. 입력창 비우기
  chatInput.value = "";

  // 4-3. "생각 중..." 표시
  const loadingMsg = addMessage("🤔 생각 중...", "bot");

  try {
    // 4-4. 백엔드 /chat 호출
    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: message,
        career_summary: careerSummary.value, // 위에 있는 경력 요약 재사용!
      }),
    });

    const data = await response.json();

    // 4-5. "생각 중..." 메시지 삭제
    loadingMsg.remove();

    // 4-6. Agent 답변 표시
    renderChatAnswer(data);
  } catch (error) {
    loadingMsg.remove();
    addMessage("❌ 오류가 발생했어요. 서버를 확인해주세요.", "bot");
    console.error(error);
  }
}

// 5. 메시지 화면에 추가하는 함수
function addMessage(text, sender) {
  const div = document.createElement("div");
  div.className = sender === "user" ? "chat-user" : "chat-bot";
  div.textContent = text;
  chatMessages.appendChild(div);

  // 자동으로 맨 아래로 스크롤
  chatMessages.scrollTop = chatMessages.scrollHeight;

  return div; // 나중에 삭제하려고 반환
}

// 6. Agent 답변을 도구별로 예쁘게 표시
function renderChatAnswer(data) {
  const tool = data.tool_used;
  const result = data.result;

  let answerText = "";

  // 도구별로 다르게 표시
  if (tool === "이력서분석") {
    answerText = "📋 이력서 분석 결과예요!\n\n";
    answerText += "💪 강점: " + result.strengths.join(", ") + "\n";
    answerText += "🔍 부족한 점: " + result.gaps.join(", ") + "\n";
    answerText += "✅ 다음 행동: " + result.next_actions.join(", ");
  } else if (tool === "직무검색") {
    answerText = "🔎 관련 직무를 찾았어요!\n\n";
    result.matched_jobs.forEach((job) => {
      answerText += `• ${job.title} (점수: ${job.score})\n`;
    });
  } else {
    // 일반상담
    answerText = result.answer;
  }

  // 답변 표시
  const botMsg = addMessage(answerText, "bot");

  // 사용한 도구 표시 (작은 글씨)
  const toolTag = document.createElement("div");
  toolTag.className = "chat-tool";
  toolTag.textContent = "🔧 사용한 도구: " + tool;
  botMsg.appendChild(toolTag);

  chatMessages.scrollTop = chatMessages.scrollHeight;
}