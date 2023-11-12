import streamlit as st
import datetime

# 스타일링을 위한 CSS
st.markdown("""
<style>
.daily-task {
    font-size: 20px;
    font-weight: bold;
}
.complete-button {
    background-color: #0D6EFD;
    color: white;
    padding: 8px 16px;
    border-radius: 5px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# 제목 설정
st.title("매일 루틴 및 학습 계획")

# 현재 요일 가져오기
today = datetime.datetime.today().weekday()  # 월요일: 0, 일요일: 6

task_descriptions = {
    "책보기": "선택한 책을 읽고 주요 내용을 정리합니다.",
    "Freecamp org 강의": "Freecamp에서 제공하는 강의를 시청합니다.",
    "유튜브 강의 영상 정리": "유튜브 강의 영상의 핵심 내용을 요약합니다.",
    "Medium 정리(3개)": "Medium에서 읽은 글 중 3개를 정리합니다.",
    "블로그쓰기": "블로그에 논문 시리즈나 실수에서 배우는 시리즈를 작성합니다.",
    "유튜브 준비하기": "유튜브 콘텐츠 제작을 위한 준비 작업을 합니다.",
    "데이터 분석가 공부": "판다스 시작 머신러닝 딥러닝 까지  한바퀴 돌리고 최신 스택까지",
    "앱개발자 공부": "FLUTTER 한바퀴 돌리고 앱 개발 쭉쭉", 
    "백엔드 공부(fastapi, Go)": "(fastapi: BACKEND, Go: KUBER,DOCKER)",
    "데이터 엔지니어 공부": "SQL 부터 시작해서 쭊쭊 돌리고 최신 스택 쭊쭊 ", 
    "웹개발자 공부": "HTML 부터 시작해서 SASS 까지",
     "서버공부(arm)": "라즈베리파이, jetson (실 사용 프로젝트) : (목, 금)"
    # 여기에 다른 학습 항목에 대한 설명을 추가하세요...
}



# 요일별 학습 계획:q!
daily_routines = {
    0: ["책보기", "Freecamp org 강의", "유튜브 강의 영상 정리", "Medium 정리(3개)",
        "블로그쓰기", "유튜브 준비하기", "데이터 분석가 공부", "앱개발자 공부", "백엔드 공부(fastapi, Go)"],
    1: ["책보기", "Freecamp org 강의", "유튜브 강의 영상 정리", "Medium 정리(3개)",
        "블로그쓰기", "유튜브 준비하기", "데이터 분석가 공부", "앱개발자 공부", "백엔드 공부(fastapi, Go)"],
    2: ["책보기", "Freecamp org 강의", "유튜브 강의 영상 정리", "Medium 정리(3개)",
        "블로그쓰기", "유튜브 준비하기", "데이터 분석가 공부", "앱개발자 공부", "백엔드 공부(fastapi, Go)"],
    3: ["책보기", "Freecamp org 강의", "유튜브 강의 영상 정리", "Medium 정리(3개)",
        "블로그쓰기", "유튜브 준비하기", "데이터 엔지니어 공부", "웹개발자 공부", "서버공부(arm)"],

    # 다른 요일에 대한 학습 계획을 여기에 추가...
    6: ["마케팅 공부", "수학 공부", "BA 분석"]
}


# 오늘의 학습 계획 표시
st.header(f"{datetime.datetime.now().strftime('%A')}의 학습 계획")
for task in daily_routines.get(today, []):
    if st.checkbox(task):
        st.markdown(f'<p class="task-info">{task_descriptions.get(task, "상세 설명이 없습니다.")}</p>', unsafe_allow_html=True)

# 완료 버튼
if st.button('오늘의 학습 완료', key='complete'):
    st.balloons()
    st.success("오늘의 학습을 모두 완료했습니다!")

# 애플리케이션을 실행하기 위한 명령어: streamlit run <파일명>.py

