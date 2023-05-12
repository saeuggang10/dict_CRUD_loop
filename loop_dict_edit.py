#!/usr/bin/env python
# coding: utf-8

# * 이름, 나이, 주소 각각의 리스트 사용 (변수 이름은 직접 지정)
# * 최초에 각 리스트는 공백상태
# * 무한반복되도록 만듬 (종료문구는 직접 특정문자로 지정)
# 
# * 시나리오
#     ->아래 중 하나를 선택해 주세요(번호로 입력) :<
#     1. 데이터 생성하기
#     2. 데이터 수정하기
#     3. 데이터 삭제하기
#     4. 데이터 검색하기
#     5. 데이터 전체 조회하기
#     
#     
# * 구조
# 
# [{'name':'홍길동','age':23,'area':'서울'},
# 
# {'name':'이순신','age':33,'area':'광주'},
# 
# {'name':'김유신','age':50,'area':'부산'}]

# In[2]:


lis = []

while 1:
    print('='*15)
    print('1. 데이터 생성하기 \n2. 데이터 수정하기 \n3. 데이터 삭제하기 \n4. 데이터 검색하기 \n5. 데이터 전체 조회 \n※ 검색 종료시 q를 입력해 주세요')
    ty=input('아래 중 하나를 선택해 주세요(번호 입력) : ')
    print('='*15)
    
    if ty=='1':
        print('1. 데이터 생성하기')
        name=input('name : ')
        age=input('age : ')
        area=input('area : ')
        lis.append({'name':name,'age':age,'area':area})
        
    elif ty=='2':
        print('2. 데이터 수정하기')
        fix3=input('변경할 key : ')
        fix=input('수정 전 데이터 : ')
        fix2=input('수정 후 데이터 : ')
        for i in range(0, len(lis)):
            if fix in lis[i].values():
                lis[i][fix3] = fix2
            else:
                print('찾으시는 데이터가 존재하지 않습니다')
                
    elif ty=='3':
        print('3. 데이터 삭제하기')
        del1=input('삭제할 key : ')
        del2=input('삭제할 데이터 : ')
        for i in range(0, len(lis)):
            if del2 in lis[i][del1].values():
                del lis[i]
            else:
                print('찾으시는 데이터가 존재하지 않습니다')
                
    elif ty=='4':
        print('4. 데이터 검색하기')
        que=input('검색할 데이터 : ')
        for i in range(0, len(lis)):
            if que in lis[i].values():
                print(lis[i])
            else:
                print('찾으시는 데이터가 존재하지 않습니다')
                
    elif ty=='5':
        print('5. 데이터 전체 조회')
        print(lis)
        
    elif ty=='q':
        print('검색을 종료합니다')
        break
    
    else:
        print('잘못 입력하셨습니다')

