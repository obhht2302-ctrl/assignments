import streamlit as st


st.set_page_config(
    page_title="Survey UI",
    page_icon="📝",
    layout="centered",
)

# 실습용 로그인 정보입니다.
LOGIN_ID = "student"
LOGIN_PASSWORD = "1234"


def init_state():
    """앱에서 사용할 로그인 상태와 화면 단계를 처음 한 번만 생성합니다."""
    st.session_state.setdefault("logged_in", False)
    st.session_state.setdefault("page", "login")
    st.session_state.setdefault("survey_result", {})


def logout():
    """로그인 정보와 설문 결과를 지우고 로그인 화면으로 돌아갑니다."""
    st.session_state["logged_in"] = False
    st.session_state["page"] = "login"
    st.session_state["survey_result"] = {}


def restart_survey():
    """로그인은 유지하면서 새로운 설문을 시작합니다."""
    st.session_state["page"] = "survey"
    st.session_state["survey_result"] = {}


init_state()

st.title("📝 개발 학습 설문조사")

# ------------------------------------------------
# 로그인 화면
if not st.session_state["logged_in"]:
    st.subheader("로그인")
    st.info("설문에 참여하려면 먼저 로그인해 주세요.")

    with st.form("login_form"):
        login_id = st.text_input("아이디")
        login_password = st.text_input("비밀번호", type="password")
        login_submitted = st.form_submit_button(
            "로그인",
            type="primary",
            use_container_width=True,
        )

    if login_submitted:
        if login_id == LOGIN_ID and login_password == LOGIN_PASSWORD:
            st.session_state["logged_in"] = True
            st.session_state["page"] = "survey"
            st.rerun()
        else:
            # 로그인 실패 시 상태를 변경하지 않으므로 로그인 화면이 계속 표시됩니다.
            st.error("아이디 또는 비밀번호가 올바르지 않습니다. 다시 로그인해 주세요.")

    with st.expander("실습용 로그인 정보"):
        st.code("아이디: student\n비밀번호: 1234")

# ------------------------------------------------
# 설문 화면
elif st.session_state["page"] == "survey":
    top_left, top_right = st.columns([4, 1])
    with top_left:
        st.success("로그인되었습니다. 아래 설문을 작성해 주세요.")
    with top_right:
        st.button("로그아웃", on_click=logout, use_container_width=True)

    with st.form("survey_form"):
        name = st.text_input(
            "이름 또는 닉네임 *",
            placeholder="이름을 입력해 주세요.",
        )

        topics = st.multiselect(
            "관심 있는 주제를 선택해 주세요. *",
            [
                "Python",
                "프론트엔드",
                "백엔드",
                "데이터베이스",
                "AI·LLM",
                "DevOps",
            ],
        )

        experience = st.radio(
            "개발 경험",
            ["처음입니다", "1년 미만", "1~3년", "3년 이상"],
            horizontal=True,
        )

        study_frequency = st.selectbox(
            "일주일 평균 학습 횟수",
            ["1회 이하", "2~3회", "4~5회", "매일"],
        )

        understanding = st.slider(
            "현재 수업 이해도",
            min_value=1,
            max_value=5,
            value=3,
        )

        wants_project = st.checkbox("팀 프로젝트에 참여하고 싶습니다.")
        wants_feedback = st.checkbox("개별 학습 피드백을 받고 싶습니다.")

        opinion = st.text_area(
            "추가 의견",
            placeholder="수업에서 기대하는 점을 자유롭게 작성해 주세요.",
        )

        survey_submitted = st.form_submit_button(
            "설문 제출",
            type="primary",
            use_container_width=True,
        )

    if survey_submitted:
        # 이름과 관심 주제는 필수 입력값으로 검사합니다.
        if not name.strip():
            st.warning("이름 또는 닉네임을 입력해 주세요.")
        elif not topics:
            st.warning("관심 주제를 한 개 이상 선택해 주세요.")
        else:
            st.session_state["survey_result"] = {
                "이름 또는 닉네임": name.strip(),
                "관심 주제": topics,
                "개발 경험": experience,
                "학습 횟수": study_frequency,
                "수업 이해도": understanding,
                "팀 프로젝트 참여": wants_project,
                "개별 피드백 희망": wants_feedback,
                "추가 의견": opinion.strip(),
            }
            st.session_state["page"] = "result"
            st.rerun()

# ------------------------------------------------
# 결과 화면: 설문 폼은 사라지고 제출한 결과만 표시됩니다.
elif st.session_state["page"] == "result":
    result = st.session_state["survey_result"]

    st.success("설문이 정상적으로 제출되었습니다.")
    st.subheader("📊 설문 결과")

    st.write(f'**이름 또는 닉네임:** {result["이름 또는 닉네임"]}')
    st.write(f'**관심 주제:** {", ".join(result["관심 주제"])}')
    st.write(f'**개발 경험:** {result["개발 경험"]}')
    st.write(f'**일주일 평균 학습 횟수:** {result["학습 횟수"]}')

    st.metric(
        "수업 이해도",
        f'{result["수업 이해도"]} / 5',
    )

    col1, col2 = st.columns(2)
    with col1:
        st.write(
            "**팀 프로젝트 참여:** "
            + ("희망" if result["팀 프로젝트 참여"] else "희망하지 않음")
        )
    with col2:
        st.write(
            "**개별 피드백:** "
            + ("희망" if result["개별 피드백 희망"] else "희망하지 않음")
        )

    st.write(f'**추가 의견:** {result["추가 의견"] or "작성하지 않음"}')

    button_left, button_right = st.columns(2)
    with button_left:
        st.button(
            "새 설문 작성",
            on_click=restart_survey,
            use_container_width=True,
        )
    with button_right:
        st.button(
            "로그아웃",
            on_click=logout,
            use_container_width=True,
        )
