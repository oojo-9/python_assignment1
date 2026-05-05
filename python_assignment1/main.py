import loop.while_mission as mssn
import fileio.fileio_mission as tt

def menu():
    prompt = '''
    *** 파이썬 과제 1 ***
    1. while 실습문제
    2. fileio 실습문제
    9. 과제 실행 테스트 끝내기
    '''

    while True:
        print(prompt)
        no = int(input('입력 : '))

        if no == 1:
            mssn.sungjuk_process()
        if no == 2:
            tt.emp_process()
        if no == 9:
            print('과제 실행 테스트가 종료되었습니다.')
            break

if __name__ == '__main__':
    menu()
    