<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>독일군에게 들키지마 README</title>
    <style>
        body {
            background-color: #1a1610;
            color: #f0e4c8;
            font-family: 'Courier New', Courier, monospace;
            line-height: 1.6;
            padding: 40px;
            max-width: 900px;
            margin: auto;
            border: 1px solid #c8a86b;
        }
        h1 {
            color: #c8a86b;
            text-align: center;
            border-bottom: 2px solid #c8a86b;
            padding-bottom: 10px;
            letter-spacing: 5px;
        }
        .subtitle {
            text-align: center;
            font-size: 1.2rem;
            color: #a08850;
            margin-top: -10px;
            margin-bottom: 40px;
        }
        h2 {
            background: #c8a86b;
            color: #1a1610;
            padding: 5px 15px;
            display: inline-block;
            margin-top: 30px;
        }
        h3 {
            color: #f2c870;
            border-left: 4px solid #f2c870;
            padding-left: 10px;
            margin-top: 20px;
        }
        ul {
            list-style-type: square;
        }
        .tech-stack {
            background: rgba(200, 168, 107, 0.1);
            padding: 15px;
            border-radius: 5px;
        }
        .ending-box {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
        }
        .ending-item {
            width: 45%;
            padding: 15px;
            border: 1px dashed #c8a86b;
            text-align: center;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 0.8rem;
            color: #7a6a50;
        }
    </style>
</head>
<body>

    <h1>🇩🇪 독일군에게 들키지마 (Metaphor for World)</h1>
    <div class="subtitle">"라디오 방송으로 연합군을 승리로 이끌어라"</div>

    <h2>1. 게임 배경</h2>
    <p>
        때는 1942년, 나치 독일의 점령 하에 놓인 유럽. 당신은 연합군의 승리를 위해 목숨을 걸고 활동하는 저항군 비밀 무전병입니다. 
        BBC 라디오 방송의 형식을 빌려 암호화된 메시지를 전달하고, 독일군의 삼엄한 검열을 피해 작전을 성공시켜야 합니다.
    </p>
    
    <h3>전술 상황 (Stages)</h3>
    <ul>
        <li><strong>Stage I - 루앙 공습 연기:</strong> 영국군 집결을 위해 미군의 폭격 계획을 하루 늦춰야 합니다.</li>
        <li><strong>Stage II - 디에프 기습 경고:</strong> 독일군 증강 배치가 확인된 디에프 항구로의 상륙 작전을 중단시켜야 합니다.</li>
        <li><strong>Stage III - 카세린 협곡 화력 집중:</strong> 분산된 아군 화력을 한 지점으로 모으기 위해 지휘 계통을 우회한 긴급 무전을 송출해야 합니다.</li>
    </ul>

    <h2>2. 게임 규칙</h2>
    <ul>
        <li><strong>직접적 군사 용어 금지:</strong> '폭격', '부대', '진격' 등 직접적인 단어 사용 시 독일군 검열국에 즉시 발각됩니다.</li>
        <li><strong>기상 및 천체 데이터 일치성:</strong> 위장 메시지에 포함된 날씨나 달의 밝기는 실제 API 데이터와 일치해야 합니다. (거짓 기상 보고는 반역으로 간주됩니다.)</li>
        <li><strong>의심도(Suspicion) 관리:</strong> 검열국 요원이 무전의 이상함을 감지할 때마다 의심도가 상승하며, 100에 도달하면 체포됩니다.</li>
        <li><strong>사상자(Casualty) 억제:</strong> 해독 점수가 낮아 메시지 전달이 늦어질수록 아군 사상자가 늘어납니다. 누적 1,000명 초과 시 작전은 실패합니다.</li>
    </ul>
    <blockquote>* TIP: 실시간 웨더맵을 확인하여 "비가 온다" 혹은 "달이 밝아 길 찾기가 좋다"는 식의 은유적 표현을 활용하십시오.</blockquote>

    <h2>3. 사용 기술</h2>
    <div class="tech-stack">
        <ul>
            <li><strong>LLM:</strong> GPT-4.1-mini (메시지 은유 판정 및 독일군 검열 에이전트 구현)</li>
            <li><strong>Weather API:</strong> OpenWeatherMap (현지 실시간 기상 데이터 연동)</li>
            <li><strong>Astronomy:</strong> ephem (날짜별 달의 위상 및 밝기 계산)</li>
            <li><strong>RAG:</strong> Pinecone (실제 역사적 작전 기록 및 전술 맥락 데이터베이스 활용)</li>
        </ul>
    </div>

    <h2>4. 게임 화면 설명</h2>
    <p>[여기에 준비하신 게임 구동 사진을 삽입하세요]</p>

    <h2>5. 게임 엔딩</h2>
    <div class="ending-box">
        <div class="ending-item">
            <h3 style="border:none; padding:0; color:#5dc45d;">🎖️ 연합군 승리</h3>
            <p>모든 스테이지의 무전을 성공적으로 송출하여 독일군을 무너뜨리고 유럽을 해방합니다.</p>
        </div>
        <div class="ending-item">
            <h3 style="border:none; padding:0; color:#c0392b;">🚨 작전 실패</h3>
            <p>게슈타포에게 체포되거나, 아군 사상자가 1,000명을 넘겨 전쟁의 패배자로 기록됩니다.</p>
        </div>
    </div>

    <h2>6. 향후 발전 및 한계점</h2>
    <ul>
        <li><strong>스테이지 확장성:</strong> 노르망디 상륙 작전, 벌지 전투 등 역사적 대전투를 기반으로 한 추가 스테이지 개발 필요성.</li>
        <li><strong>컨텐츠 제한 시스템:</strong> 더욱 고도화된 AI를 통해 단순한 문장이 아닌, 실제 라디오 방송 대본 형식을 갖추도록 강제하는 게임 메커니즘 고안.</li>
    </ul>

    <div class="footer">
        © 1942 Resistance Radio Project - Confidential Document
    </div>

</body>
</html>
