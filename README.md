# 프로그래머스 코딩테스트 문제 필터

코딩테스트 문제가 있는 프로그래머스 사이트의 문제 정보들을 긁어와서 원하는대로 필터링을 할 수 있게 만들어보자.  

현재 프로그래머스 사이트에는 필터기능이 있긴하지만, 레벨과 시행됐던 대회에 대해서 필터가능하다. 내가 원하는 것은 내가 푼 문제와 못 푼 문제도 한 눈에 볼 수 있고, 어떤 언어로 풀었는지 등 다양한 방면에서 필터를 하고싶다.


python 버젼 : Python 3.6.9

## 가상환경 설치하기  
가상환경 이름은 자주쓰이므로 간단하게!  
  
```bash  
current directory $ python3 -m venv myvenv # 가상환경 설치  
current directory $ source myvenv/bin/activate # 가상환경 실행  
```    
  
## 장고 설치 / 프로젝트 시작  
  
```bash
(myvenv) current directory $ pip3 install django~=2.0
(myvenv) current directory $ django-admin startproject mysite .
```
  
## 설정 변경  
`mysite/settings.py`  
```python  
TIME_ZONE = 'Asia/Seoul'    # time zone 변경

ALLOWED_HOSTS = ['127.0.0.1'] # 로컬 호스트 설정

STATIC_URL = '/static/' 
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # 정적파일 경로 설정
```  
  
```bash
(myvenv) current directory $ python3 manage.py migrate
```