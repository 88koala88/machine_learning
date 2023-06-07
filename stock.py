

import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver_ = webdriver.Safari()


def print_car(driver_):

    elems_ = driver_.find_elements(By.XPATH, "//font[@style='font-size:8pt;']")
    for i, elem_ in enumerate(elems_):
        if i % 2 == 1:
            print(elem_.text)
    print()

def main():

    url_="http://www.j123.co.kr/search01/totalsearch.asp"

    driver_.get(url_)

    # 차량 선택 후 검색
    driver_.find_element(By.ID,"Checkbox34").click()
    driver_.find_element(By.XPATH,"//img[@alt='검색하기']").click()

    # 로딩시간 대기
    time.sleep(1)

    # 총 페이지 수 확인
    elems_ = driver_.find_elements(By.XPATH,"//table[@id='Table1']//td")
    p_ = r"\d+"
    max_page_ = int(re.findall(p_,elems_[len(elems_)-3].text.lstrip().rstrip())[0])//20 +1

    print("페이지 1")
    print_car(driver_)


    for i in range(2,max_page_+1):
        time.sleep(1)
        print(f"페이지 {i}")
        func_ = f"javascript:submit_chk({i})"
        driver_.execute_script(func_)
        time.sleep(1)
        print_car(driver_)



if __name__=="__main__":

    main()

    while True:
        time.sleep(10000)

