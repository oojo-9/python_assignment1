# path : fileio\\fileio_mission.py
# module : fileio.fileio_mission

import pickle


def emp_process():
    prompt = '''
    *** 직원 정보 관리 서비스 ***
    1. 새 직원정보 추가
    2. 직원정보 삭제
    3. 전체 출력
    4. 파일에 저장
    5. 파일로 부터 직원정보 읽어오기
    9. 서비스 끝내기
    '''

    
    while True:
        print(prompt)
        no = int(input('입력 : '))

        if no == 1:
            emp_list()
        if no == 2:
            emp_del()
        if no == 3:
            emp_list_read()
        if no == 4:
            mk_list()
        if no == 5:
            rd_list()
        if no == 9:
            print('직원 정보 관리 서비스가 종료되었습니다.')
            break
#---------------------------------------------------------------------
# 1번 출력
emp_dict = {}

def emp_list():
    empid = input('사번 : ')
    empname = input('이름 : ')
    empno = input('주민번호 : ')
    email = input('이메일 : ')
    phone = input('전화번호 : ')
    salary = int(input('급여 : '))
    job = input('직급 : ')
    dept = input('부서 : ')

    emp_dict[empid] = [empid, empname, empno, email, phone, salary, job, dept]

#---------------------------------------------------------------------
# 2번 삭제
def emp_del():
    empid = input('삭제할 사번 : ')

    while True:
        if empid in emp_dict:
            emp_dict.pop(empid)
            print(f'{empid}번 사번의 직원 정보가 삭제되었습니다.')
            break
        print(f'{empid}번 사번의 직원 정보가 없습니다.')
        break

#---------------------------------------------------------------------
# 3번 전체 출력
def emp_list_read():
    for key,value in emp_dict.items():
        print(f'{key} : {value}')


#---------------------------------------------------------------------
# 4번 파일저장

def mk_list():
    name = input('저장할 파일명을 입력하세요 : ')
    f = open(name, 'ab')
    pickle.dump(emp_dict, f)
    f.close()
    print(f'{name} 파일에 성공적으로 저장되었습니다.')

#---------------------------------------------------------------------
# 5번 파일로 부터 정보읽기

def rd_list():
    name = input('읽을 파일명을 입력하세요 : ')
    f = open(name, 'rb')
    rd_data = pickle.load(f)
    f.close()

    emp_dict = rd_data
    print(emp_dict)

