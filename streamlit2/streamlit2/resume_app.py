import streamlit as st

# Set Streamlit page configuration
st.set_page_config(
    page_title="이력서 및 자기소개",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Set custom theme (Streamlit 자체 다크모드 사용)
# st.markdown(
#     """
#     <style>
#     body { background-color: #121212; color: white; }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# 우성우
##### *반나서 반갑습니다.* 
''')

# image = Image.open('dp.png')
# st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Educator, Researcher and Administrator with almost twenty years of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
- Strong verbal and written communication skills as demonstrated by extensive participation as invited speaker at `10` conferences as well as publishing 149 research articles.
- Strong track record in scholarly research with H-index of `32` and total citation of 3200+.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Chanin Nantasenamat</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# 페이지 타이틀
# st.title("📄 나만의 이력서와 자기소개 사이트")

# 사이드바 네비게이션
with st.sidebar:
    st.header("메뉴")
    page = st.radio("이동", ["홈", "이력서 업로드", "자기소개 입력", "미리보기"])

# 홈 페이지
if page == "홈":
    st.header("환영합니다!")
    st.write("""
    이 웹사이트는 여러분의 이력서와 자기소개를 관리하고 표시할 수 있는 간단한 도구입니다. 
    사이드바 메뉴를 이용해 다양한 기능을 사용해 보세요.
    """)

# 이력서 업로드 페이지
elif page == "이력서 업로드":
    st.header("📂 이력서 업로드")
    uploaded_file = st.file_uploader("PDF 형식의 이력서를 업로드하세요", type="pdf")
    
    if uploaded_file is not None:
        st.success("이력서가 성공적으로 업로드되었습니다!")
        
        # 파일 내용을 메모리에 저장
        file_data = uploaded_file.read()
        
        # 다운로드 버튼 생성
        st.download_button(
            label="📄 이력서 다운로드",
            data=file_data,
            file_name="uploaded_resume.pdf",
            mime="application/pdf"
        )

# 자기소개 입력 페이지
elif page == "자기소개 입력":
    st.header("✍️ 자기소개 입력")

    # 폼 생성
    with st.form("self_intro_form"):
        name = st.text_input("이름", value=st.session_state.get("name", ""))
        job_title = st.text_input("직업 또는 역할", value=st.session_state.get("job_title", ""))
        about_me = st.text_area("자기소개", placeholder="여기에 자기소개를 작성하세요...", value=st.session_state.get("about_me", ""))
        contact_email = st.text_input("이메일", value=st.session_state.get("contact_email", ""))
        linkedin_url = st.text_input("LinkedIn 프로필 URL", value=st.session_state.get("linkedin_url", "https://linkedin.com/in/yourprofile"))
        github_url = st.text_input("GitHub URL", value=st.session_state.get("github_url", "https://github.com/yourusername"))

        # 폼 제출 버튼
        submitted = st.form_submit_button("저장")
        if submitted:
            # Session state에 데이터 저장
            st.session_state["name"] = name
            st.session_state["job_title"] = job_title
            st.session_state["about_me"] = about_me
            st.session_state["contact_email"] = contact_email
            st.session_state["linkedin_url"] = linkedin_url
            st.session_state["github_url"] = github_url

            st.success("자기소개가 저장되었습니다!")

# 미리보기 페이지
elif page == "미리보기":
    st.header("👀 미리보기")

    # 세션 상태에서 값 가져오기
    name = st.session_state.get("name", "이름을 입력하세요.")
    job_title = st.session_state.get("job_title", "직업/역할을 입력하세요.")
    about_me = st.session_state.get("about_me", "자기소개 내용을 입력하세요.")
    contact_email = st.session_state.get("contact_email", "이메일을 입력하세요.")
    linkedin_url = st.session_state.get("linkedin_url", "LinkedIn URL을 입력하세요.")
    github_url = st.session_state.get("github_url", "GitHub URL을 입력하세요.")

    # 미리보기 표시
    st.subheader("이름:")
    st.write(name)
    st.subheader("직업/역할:")
    st.write(job_title)
    st.subheader("자기소개:")
    st.write(about_me)
    st.subheader("연락처:")
    st.write(contact_email)
    st.subheader("링크:")
    st.write(f"[LinkedIn]({linkedin_url})")
    st.write(f"[GitHub]({github_url})")
