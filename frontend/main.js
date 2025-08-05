const logWindow = document.getElementById('log-window');
const btn1 = document.getElementById('btn1');
const btn2 = document.getElementById('btn2');
const btn3 = document.getElementById('btn3');

// WebSocket for real-time logs
let ws;
function connectWebSocket() {
  ws = new WebSocket('ws://localhost:8000/ws/logs');
  ws.onopen = () => {
    appendLog('[WebSocket 연결됨]');
  };
  ws.onmessage = (event) => {
    appendLog(event.data);
  };
  ws.onclose = () => {
    appendLog('[WebSocket 연결 종료, 2초 후 재연결]');
    setTimeout(connectWebSocket, 2000);
  };
  ws.onerror = (e) => {
    appendLog('[WebSocket 오류]');
  };
}
connectWebSocket();

function appendLog(text) {
  logWindow.textContent += text + '\n';
  logWindow.scrollTop = logWindow.scrollHeight;
}

// Button click handlers
btn1.onclick = () => sendButtonClick(1);
btn2.onclick = () => sendButtonClick(2);
btn3.onclick = () => sendButtonClick(3);

function sendButtonClick(num) {
  fetch(`http://localhost:8000/button/${num}`, { method: 'POST' })
    .then(res => {
      if (!res.ok) throw new Error('서버 오류');
    })
    .catch(() => {
      appendLog(`[버튼 ${num} 요청 실패]`);
    });
}
