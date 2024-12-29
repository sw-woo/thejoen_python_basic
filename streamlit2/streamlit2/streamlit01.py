import streamlit as st

# 타이틀 적용 예시 
st.title("이것은 타이틀 입니다.")

st.title('스마일 :sunglasses:')

# Header 적용 
st.header("헤더를 입력할 수 있어요! :sparkles:")

# Subheader 적용 
st.subheader("서브 헤더 입니다. :star:")

# 캡션 적용 
st.caption("캡션을 한 번 넣어 봤습니다.")


# 코드 표시
sample_code = '''
def function():
    print('hello world')
'''

st.code(sample_code, language='python')

# 일반 텍스트 
st.text("일반 텍스트를 입력할 수 있습니다.")

# Markdown 적용
st.markdown("마크다운을 입력할 수 있습니다. :smile:")

# 컬러코드 적용: blue, green, red, yellow, black
st.markdown("<span style='color: blue'>파란색 텍스트</span>", unsafe_allow_html=True)
st.markdown(":green[$\sqrt{x^2+y^2}=1$] 와 같이 latex 문법의 수식 표현도 가능합니다 :pencil:")

# LaTex 수식 지원 
st.latex(r'\sqrt{a^2 + b^2} = 1')