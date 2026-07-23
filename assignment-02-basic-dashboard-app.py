"""Streamlit의 sidebar, columns, tabs를 활용한 기본 대시보드 앱입니다."""

import streamlit as st


# 넓은 화면을 사용해 여러 지표가 한눈에 보이도록 설정합니다.
st.set_page_config(
    page_title="학습 현황 대시보드",
    page_icon="📊",
    layout="wide",
)

# 사이드바는 사용자가 대시보드의 기준값을 설정하는 입력 영역입니다.
with st.sidebar:
    st.header("⚙️ 대시보드 설정")
    st.write("사용자 정보와 이번 주 학습 현황을 입력해 주세요.")

    user_name = st.text_input(
        "사용자 이름",
        placeholder="이름을 입력해 주세요.",
    )
    weekly_goal = st.slider(
        "주간 목표 학습 시간",
        min_value=1,
        max_value=40,
        value=10,
        step=1,
        help="이번 주에 달성하고 싶은 총 학습 시간입니다.",
    )
    completed_hours = st.slider(
        "현재까지 학습한 시간",
        min_value=0,
        max_value=40,
        value=0,
        step=1,
        help="이번 주에 실제로 학습한 시간을 입력합니다.",
    )
    focus_area = st.selectbox(
        "집중 학습 분야",
        ["Streamlit", "Python", "Supabase", "LLM API", "데이터 분석"],
    )

# 입력값을 이용해 대시보드에 표시할 값을 계산합니다.
achievement_rate = min(completed_hours / weekly_goal, 1.0)
achievement_percent = round((completed_hours / weekly_goal) * 100)
remaining_hours = max(weekly_goal - completed_hours, 0)

display_name = user_name.strip() or "학습자"

st.title("📊 학습 현황 대시보드")
st.write(
    f"{display_name}님의 주간 학습 목표와 진행 상황을 한눈에 확인할 수 있습니다."
)

# columns를 사용해 핵심 지표를 가로로 배치합니다.
goal_column, completed_column, remaining_column = st.columns(3)

with goal_column:
    st.metric("주간 목표", f"{weekly_goal}시간")

with completed_column:
    st.metric(
        "완료한 학습",
        f"{completed_hours}시간",
        delta=f"{achievement_percent}% 달성",
    )

with remaining_column:
    st.metric("남은 학습", f"{remaining_hours}시간")

st.divider()

# tabs를 사용해 요약 정보와 상세 정보를 구분합니다.
overview_tab, detail_tab = st.tabs(["📝 개요", "🔍 상세 내용"])

with overview_tab:
    st.subheader("이번 주 학습 개요")
    st.write("목표 대비 현재 학습 진행률입니다.")
    st.progress(achievement_rate)
    st.caption(f"목표 달성률: {achievement_percent}%")

    # 이름과 달성률에 따라 서로 다른 안내 메시지를 보여 줍니다.
    if not user_name.strip():
        st.warning("사이드바에 사용자 이름을 입력해 주세요.")
    elif completed_hours >= weekly_goal:
        st.success(
            f"{display_name}님, 주간 목표를 달성했습니다! 훌륭합니다. 🎉"
        )
    elif achievement_percent >= 70:
        st.success(
            f"{display_name}님, 목표까지 {remaining_hours}시간 남았습니다. 거의 다 왔습니다!"
        )
    elif achievement_percent >= 30:
        st.info(
            f"{display_name}님, 꾸준히 진행 중입니다. 다음 학습도 이어가 보세요."
        )
    else:
        st.warning(
            f"{display_name}님, 목표 달성을 위해 이번 주 학습을 시작해 보세요."
        )

with detail_tab:
    st.subheader("학습 설정 상세")
    st.write("사이드바에서 입력한 설정값을 자세히 확인할 수 있습니다.")

    st.write(f"**사용자:** {display_name}")
    st.write(f"**집중 학습 분야:** {focus_area}")
    st.write(f"**주간 목표 시간:** {weekly_goal}시간")
    st.write(f"**완료한 학습 시간:** {completed_hours}시간")
    st.write(f"**남은 학습 시간:** {remaining_hours}시간")

    if completed_hours > weekly_goal:
        extra_hours = completed_hours - weekly_goal
        st.success(f"목표보다 {extra_hours}시간 더 학습했습니다!")
    else:
        st.info(
            "사이드바의 값을 변경하면 지표와 안내 메시지가 즉시 변경됩니다."
        )
