# dict_CRUD_loop
---
# D+5
* 4일차 만들었던 무한루프와 비슷한 조건으로 5일차에 배운 dict타입을 활용하여 무한루프문 만들기

 Q, dict형식으로 list에 넣어 입력, 수정, 삭제, 검색이 가능한 무한루프문을 만들어라

---
# 발전
1. 데이터 수정하기

>기존 : 어떤 list의 값을 수정하고자 하는지 선택하는 부분이 추가적으로 수정이 필요하였다.
변경 : key값을 input으로 받아들여 그부분만 수정되도록 코드를 바꾸었다.


2. 데이터 삭제하기

기존 : name값을 받아 같은 index인 age, area 데이터도 삭제

변경 : 찾을 key 선택. key가 있는 dict 전체 삭제
