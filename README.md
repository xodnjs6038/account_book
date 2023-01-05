﻿# PAYHERE_ACCOUNTBOOK

- Language

  ![python](https://img.shields.io/badge/python-3.10.9-3670A0?logo=python&logoColor=white)

- FrameWork

  ![Django](https://img.shields.io/badge/django-4.1.5-%23092E20?&logo=Django&logoColor=white)
  ![DjangoRest](https://img.shields.io/badge/DJANGOREST-3.14.0-ff1709?logo=django&logoColor=white&color=ff1709&labelColor=gray)
  
- DataBase 

  ![MySQL](https://img.shields.io/badge/mysql-5.7-0073ca.svg?logo=mysql&logoColor=white)

### 요구사항

1. 고객은 이메일과 비밀번호 입력을 통해서 회원 가입을 할 수 있습니다. 
2. 고객은 회원 가입이후, 로그인과 로그아웃을 할 수 있습니다. 
3. 고객은 로그인 이후 가계부 관련 아래의 행동을 할 수 있습니다. 
    1. 가계부에 오늘 사용한 돈의 금액과 관련된 메모를 남길 수 있습니다. 
    2. 가계부에서 수정을 원하는 내역은 금액과 메모를 수정 할 수 있습니다. 
    3. 가계부에서 삭제를 원하는 내역은 삭제 할 수 있습니다. 
    4. 가계부에서 이제까지 기록한 가계부 리스트를 볼 수 있습니다. 
    5. 가계부에서 상세한 세부 내역을 볼 수 있습니다. 
    6. 가계부의 세부 내역을 복제할 수 있습니다.
    7. 가계부의 특정 세부 내역을 공유할 수 있게 단축 URL을 만들 수 있습니다.
    (단축 URL은 특정 시간 뒤에 만료되어야 합니다.)

로그인하지 않은 고객은 가계부 내역에 대한 접근 제한 처리가 되어야 합니다.

### 기능 구현

유저
- 회원가입
- 로그인, 로그아웃
- JWT(DRF) 적용
- postman API request test & Documentation

앱
- 가계부 Read, Create, Update, Delete 구현
- 가계부 데이터 상세 내역 Read, Create, Update, Delete, Copy 구현


### 구현 내용
DB관련된 DDL 파일 /DDL.txt
