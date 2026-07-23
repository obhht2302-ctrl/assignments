"""Streamlit으로 만드는 자기소개 카드 앱입니다."""

import streamlit as st


# 브라우저 탭에 표시할 제목과 아이콘을 설정합니다.
st.set_page_config(page_title="자기소개 앱", page_icon="👋")

st.title("👋 자기소개 앱")
st.write("아래 내용을 입력하면 나만의 자기소개 카드가 완성됩니다.")

# 사용자에게 자기소개 카드에 필요한 정보를 입력받습니다.
name = st.text_input(
    "이름",
    placeholder="이름을 입력해 주세요.",
)
interest = st.selectbox(
    "관심 분야",
    [
        "선택해 주세요.",
        "인공지능",
        "백엔드 개발",
        "프론트엔드 개발",
        "데이터 분석",
        "서비스 기획",
    ],
)
introduction = st.text_area(
    "자기소개",
    placeholder="자신을 소개하는 문장을 입력해 주세요.",
    height=120,
)

# 입력 영역과 결과 영역을 구분합니다.
st.divider()
st.subheader("자기소개 카드")

# 공백만 입력한 경우도 빈 값으로 처리합니다.
clean_name = name.strip()
clean_introduction = introduction.strip()
interest_selected = interest != "선택해 주세요."

missing_fields = []
if not clean_name:
    missing_fields.append("이름")
if not interest_selected:
    missing_fields.append("관심 분야")
if not clean_introduction:
    missing_fields.append("자기소개")

# 모든 값이 입력된 경우에만 완성된 자기소개 카드를 출력합니다.
if not missing_fields:
    with st.container(border=True):
        st.header(clean_name)
        st.write(f"**관심 분야:** {interest}")
        st.info(clean_introduction)
        st.success("자기소개 카드가 완성되었습니다!")
else:
    missing_text = ", ".join(missing_fields)
    st.warning(f"다음 항목을 입력해 주세요: {missing_text}")
