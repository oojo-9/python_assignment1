# path : loop\\while_mission.py
# module : loop.while_mission

# 함수명 : sungjuk_process()

sungjuk_list = [[12, '홍길동', 98],[15, '김유신', 87],[23, '황지니', 45]]

def sungjuk_process():
    prompt = '''
    *** 원하는 메뉴 번호를 선택하세요. ***
    1. 추가
    2. 삭제
    3. 출력
    4. 끝내기
    '''

    while True:
        print(prompt)
        no = int(input('입력 : '))

        if no == 1:
            add_list()
        if no == 2:
            del_list()
        if no == 3:
            save_list()
        if no == 4:
            print('성적관리 프로그램이 종료되었습니다.')
            break

#---------------------------------------------------------------------
# 1번 추가 선택 시 실행 내용
def add_list():
    sno = input('번호 : ')
    sname = input('이름 : ')
    score = input('점수 : ')
    sungjuk_list.append([sno, sname, score])
    print('새로운 학생정보가 추가되었습니다.')

#----------------------------------------------------------------------
# 2번 삭제 선택 시 실행 내용
def del_list():
    print(f'현재 저장된 아이템의 갯수는 {len(sungjuk_list)}개 입니다.')


    while True:
        lst = int(input('제거할 아이템의 순번 : '))

        if lst <= int(len(sungjuk_list)):
            sungjuk_list.remove(sungjuk_list[lst-1])
            print(f'{lst}번 위치의 아이템이 제거되었습니다.')
            print(f'현재 저장된 아이템의 갯수는 {len(sungjuk_list)}개 입니다.')
            break

        else:
            print('순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.')

#----------------------------------------------------------------------
# 3번 출력
def save_list():
    num = 0

    while True:
        print(f'{num} : {sungjuk_list[num]}' )
        num += 1
        if num >= len(sungjuk_list):
            break
#----------------------------------------------------------------------
# 4번 종료


