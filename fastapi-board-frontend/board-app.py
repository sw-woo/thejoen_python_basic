# frontend/streamlit_app.py

import streamlit as st
import requests
from typing import List, Optional
from dataclasses import dataclass

# API 기본 URL
API_URL = "http://127.0.0.1:8000"

# Pydantic 스키마와 유사한 데이터 클래스 정의
@dataclass
class PostCreate:
    title: str
    content: str

@dataclass
class PostResponse:
    id: int
    title: str
    content: str
    created_at: str  # ISO 형식의 문자열

# API와 상호작용하는 헬퍼 함수들
def get_posts(skip: int = 0, limit: int = 10, order: Optional[str] = "asc", sort_by: Optional[str] = "id") -> List[PostResponse]:
    params = {
        "skip": skip,
        "limit": limit,
        "order": order,
        "sort_by": sort_by
    }
    response = requests.get(f"{API_URL}/posts/", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"게시물 조회 실패: {response.status_code}")
        return []

def get_post(post_id: int) -> Optional[PostResponse]:
    response = requests.get(f"{API_URL}/posts/{post_id}")
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        st.warning("게시물을 찾을 수 없습니다.")
        return None
    else:
        st.error(f"게시물 조회 실패: {response.status_code}")
        return None

def create_post_api(post: PostCreate) -> Optional[PostResponse]:
    response = requests.post(f"{API_URL}/posts/", json=post.__dict__)
    if response.status_code in [200, 201]:
        st.success("게시물이 성공적으로 생성되었습니다!")
        return response.json()
    else:
        error_detail = response.json().get('detail', '알 수 없는 오류가 발생했습니다.')
        st.error(f"게시물 생성 실패: {error_detail}")
        return None

def update_post_api(post_id: int, post: PostCreate) -> Optional[PostResponse]:
    response = requests.put(f"{API_URL}/posts/{post_id}", json=post.__dict__)
    if response.status_code == 200:
        st.success("게시물이 성공적으로 수정되었습니다!")
        return response.json()
    elif response.status_code == 404:
        st.warning("게시물을 찾을 수 없습니다.")
        return None
    else:
        error_detail = response.json().get('detail', '알 수 없는 오류가 발생했습니다.')
        st.error(f"게시물 수정 실패: {error_detail}")
        return None

def delete_post_api(post_id: int) -> bool:
    response = requests.delete(f"{API_URL}/posts/{post_id}")
    if response.status_code == 200:
        st.success("게시물이 성공적으로 삭제되었습니다!")
        return True
    elif response.status_code == 404:
        st.warning("게시물을 찾을 수 없습니다.")
        return False
    else:
        st.error(f"게시물 삭제 실패: {response.status_code}")
        return False

# Streamlit 애플리케이션 레이아웃
def main():
    st.title("📋 FastAPI 게시판")

    menu = ["게시물 보기", "게시물 생성", "게시물 수정", "게시물 삭제"]
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == "게시물 보기":
        st.header("📰 모든 게시물 보기")

        # 사이드바 필터 설정
        st.sidebar.subheader("필터")
        skip = st.sidebar.number_input("건너뛸 게시물 수", min_value=0, value=0, step=1)
        limit = st.sidebar.number_input("조회할 게시물 수", min_value=1, value=10, step=1)
        order = st.sidebar.selectbox("정렬 순서", ["asc", "desc"])
        sort_by = st.sidebar.selectbox("정렬 기준", ["id", "created_at", "title"])

        posts = get_posts(skip=skip, limit=limit, order=order, sort_by=sort_by)

        if posts:
            for post in posts:
                st.subheader(f"### {post['title']} (ID: {post['id']})")
                st.write(f"**작성일:** {post['created_at']}")
                st.write(post['content'])
                st.markdown("---")
        else:
            st.info("게시물이 없습니다.")

    elif choice == "게시물 생성":
        st.header("📝 새로운 게시물 생성")

        with st.form(key='create_post_form'):
            title = st.text_input("제목")
            content = st.text_area("내용")
            submit_button = st.form_submit_button(label='게시물 생성')

        if submit_button:
            if title and content:
                post = PostCreate(title=title, content=content)
                create_post_api(post)
            else:
                st.warning("제목과 내용을 모두 입력해주세요.")

    elif choice == "게시물 수정":
        st.header("🔄 게시물 수정")

        post_id = st.number_input("수정할 게시물 ID 입력", min_value=1, step=1)
        post = get_post(post_id)

        if post:
            with st.form(key='update_post_form'):
                new_title = st.text_input("새 제목", value=post['title'])
                new_content = st.text_area("새 내용", value=post['content'])
                update_button = st.form_submit_button(label='게시물 수정')

            if update_button:
                if new_title and new_content:
                    updated_post = PostCreate(title=new_title, content=new_content)
                    update_post_api(post_id, updated_post)
                else:
                    st.warning("제목과 내용을 모두 입력해주세요.")

    elif choice == "게시물 삭제":
        st.header("🗑️ 게시물 삭제")

        post_id = st.number_input("삭제할 게시물 ID 입력", min_value=1, step=1)
        post = get_post(post_id)

        if post:
            st.write(f"**제목:** {post['title']}")
            st.write(f"**내용:** {post['content']}")
            st.write(f"**작성일:** {post['created_at']}")

            delete_button = st.button("게시물 삭제")

            if delete_button:
                delete_post_api(post_id)

if __name__ == '__main__':
    main()
