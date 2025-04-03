# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 04:33:53 2025

@author: tuesv
"""
### 다나와 검색 페이지 접속 ###

# selenium으로 다나와 검색 결과 URL에 접속
from selenium import webdriver
driver = webdriver.Chrome()
url = "http://search.danawa.com/dsearch.php?query=무선청소기&tab=main"
driver.get(url)


### 다나와 검색 웹 페이지에서 상품 정보 가져오기 ###

# 웹 페이지의 HTML 정보 가져오기
from bs4 import BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 페이지에 대한 무선청소기 정보 가져오기


# 상품명 정보 가져오기


# 스펙 목록 정보 가져오기


# 가격 정보 가져오기



# 반복문으로 검색 결과의 1페이지에 대한 상품 정보 추출
# 진행시 에러가 발생할 경우(광고 상품 등) 넘어가기


# 상품 정보 태그에서 원하는 정보를 추출하는 함수



# 상품 정보를 가져오는 함수 테스트


### 여러 페이지에 걸친 다나와 검색 페이지 크롤링 ###

## 다나와 검색 결과 페이지 URL 분석 ##
# 다나와 검색 URL을 만들어주는 함수 




## 여러 페이지에 걸친 상품 정보 수집 ##
## 암묵적으로 웹 자원 로드를 위해 3초까지 기다림
# driver.implicitly_wait(3)

keyword = '무선청소기'
total_page = 10



## 수집 데이터 저장 ##
# './files/danawa_crawling_result.xlsx'





























