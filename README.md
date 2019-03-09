#블로그 만들기
## 목적
1. 멋사 교육을 위하여 제작
    - 모든 코드에 주석을 달자
2. 나를 홍보하는 목적
    - 현재 내가 만든 프로젝트 연결
    - 내가 공부한 내용들을 수시로 정리할 것
    - (추후) 유튜브 관련 글들을 정리할 예정
    - 코딩 과외를 홍보 할 때 사용

## 일정
1. razo 템플릿 세팅 => 완료
2. 랜딩페이지 꾸미기
3. 로그인 기능 구현하기
4. 질문 게시판 구현
5. 스케줄링가능한 기능 넣기
6. 디플로이하기

## 모델
1. 게시판
- 제목
- 작성자
- 작성일자
- 수정일자
- 첨부파일(이미지, 파일)
- 내용
- 카테고리(공부, 멋사, 학교강의, 프로젝트, 유튜브, 코딩과외, 기타)
- 조회수
- 링크
- 좋아요

2. 댓글기능(QnA 답)
- 작성자
- 작성일자
- 게시판id

3. 회원
- 이름
- 자기소개


4. QnA
- 작성자
- 질문내용
- 작성일자
- 수정일자

5. 시간표
- 강좌이름
- 요일
- 시간대
- 칸번호

## 필요한 View 페이지
1. main 페이지들
    - HOME
         - 최근에 올린
         - 진행중인 프로젝트
         - Youtube
         - schedule 목록들
    - Project
         - 진행중인 프로젝트
         - 완료된 프로젝트
         - 예정된 프로젝트
    - EDUCATION
         - 교육 방식 및 커리큘럼
         - 멘토 신청하기
    - STUDY
         - Note 모두 보기
         - 글 자세히 보기
            - form
            - 댓글
            - 좋아요 버튼
         - 글 수정하기
         - 글 삭제하기
         
         - category(강의, 개인 정리) 별로 게시판 보기
         - tag 별로 게시판 보기
    - ABOUT
        - 딱히 미정 준비중
    - QNA
        - 질문 게시판(모든글 보기)
        - 질문 자세히 보기 및 자세히 보기
    
    - 로그인 및 회원가입
        
    
2. from
    - 게시글
    - 댓글
    - 로그인
    - 회원가입
    
## frame work API
~~~
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
~~~
기본 설정(setting.py) 
~~~
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
~~~

## phone_nuber_field
~~~
pip install django-phonenumber-field
pip install phonenumbers

INSTALLED_APPS = [
    ...
    'phonenumber_field',
    ...
]
~~~
## 일지
3.8 모델링 하다가 그만함

3.9 pipenv 환경에서 다시 세팅하기로 했다.
    모델링 완성!
    다음부터 gitignore 부터 세팅해주자
    페이지 계획해함
    form.py
    실수로 빼먹은 멘토 시청 model 추가하였음
    