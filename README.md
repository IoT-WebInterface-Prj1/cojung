## 🛠Cojung 
### 코딩문제 풀이 사이트
---
* `코딩 관련 문제`를 **업로드** 
  * 문제에서 허용 가능한 `언어` 선택
  * `첨부파일` 업로드 가능
  * `문제 풀이` 작성 및 공유
* `질문 게시판`
  * 코딩 문제와 관련된 질문 가능
  * 그외 질문 업로드 가능
  * 첨부파일 업로드 가능
  
---
### 실행방법

* `conda` 실행
* `db`가`sqlight` 로 되어있음 
  * 다른 db로 설정할 경우 *[./config/settings.py](./config/settings.py)*  에서 **DATABASES** 수정
* `db` 가 ignore 되어있음
  * ```python manage.py migrate``` 와 ```python manage.py makemigrations``` 를 이용하여 db 활성화
  * 모델 수정시 **마이그레이션** 필요
* ```python manage.py runserver``` 을 이용하여 서버 작동
  * IP 추가시 *[./config/settings.py](./config/settings.py)* 에서 `ALLOWED_HOSTS = []` 에 IP 추가
  * 서버 실행시 ```python manage.py runserver IP:PORT```  로 실행