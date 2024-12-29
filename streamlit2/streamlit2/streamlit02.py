import streamlit as st
import pandas as pd
import numpy as np

st.title("데이터프레임 튜토리얼 입니다.")

# DataFrame 생성 
dataframe = pd.DataFrame({
    'first column':[1,2,3,4],
    'second_column': [10,20,30,40]
})

# 데이터프레임 출력
# use_container_width 기능은 데이터프레임을 컨테이너 크기에 확장할 때 사용합니다.
st.dataframe(dataframe, use_container_width=False)

# 테이블(static)
# DataFrame과는 다르게 interactive 한 UI를 제공하지 않습니다.
st.table(dataframe)

# # 메트릭
st.metric(label="온도", value="10도", delta="1.2도")
st.metric(label="삼성전자", value="61,000원", delta="-1200원")

#컬럼으로 영역을 나누어 표기한 경우
col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1,228원", delta="-12.00원")
col2.metric(label="일보JYP(100엔)", value="950.20원", delta="-10.00원")
col3.metric(label="유럽연합EUR", value="1,520.22원", delta="11.44원")
