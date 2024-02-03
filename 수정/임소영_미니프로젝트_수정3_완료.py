# ===============================================================================================
# ===============================================================================================
# 그전 파일과 달라진 점
# - 내 함수 파일에서 종료 멘트 함수 호출
# - 내 함수 파일에서 happything 함수 호출
# ===============================================================================================
# ===============================================================================================

import YSY_func as ysy

# =====================================================
# 함수 기능: 기분을 기록하기 위해 설문조사해서 점수 계산하기
# 함수 이름: newMood
# 매개 변수: 없음
# 함수 결과: 점수 결과 및 해결책 보여주기
# =====================================================
def newMood():
    # 설문지에 이용자가 자신의 답 입력하기 ------------------------------------------------
    print('🟢 모든 질문에는 0~5점 사이로 입력하기')
    print('🟢 0은 전혀아니다. 5는 매우그렇다 \n')

    h1 = 'Q1. 오늘 하루 크게 박장대소 했나요?: '
    q_happy(h1)
    h2 = 'Q2. 오늘 당신을 기분 좋게 하는 것을 느꼈나요?: '
    q_happy(h2)
    h3 = 'Q3. 내일도 오늘과 같은 하루가 되었으면 하나요?: '
    q_happy(h3)
    print()

    a1 = 'Q4. 오늘 인상을 찌푸린 적이 있나요?: '
    q_angry(a1)
    a2 = 'Q5. 당신을 화나게 만든 무언가가 곁에 얼마나 있나요?: '
    q_angry(a2)
    a3 = 'Q6. 오늘 하루가 생각대로 흐르지 않는 것이 나를 힘들게 하나요?: '
    q_angry(a3)
    print()

    d1 = 'Q7. 오늘 하루 대부분의 기분이 공허한가요?: '
    q_depressed(d1)
    d2 = 'Q8. 오늘 하루가 아무 의미없다고 느껴지나요?: '
    q_depressed(d2)
    d3 = 'Q9. 내일도 오늘과 같은 하루가 되기 싫은가요?: '
    q_depressed(d3)
    print('\n')

    print('❕오늘의 감정 기록은 끝났습니다 :)')
    print()

    # 주관식으로 이용자가 자신의 짧은 일기 적기 --------------------------------------------
    global writeValue
    while writeValue:
        more = input('\n❔오늘 하루 있었던 일을 적어볼까요? \n🟢 Y/N 중 하나 입력: ')
        if more in ['Y', 'y']:
            write()
            print()
        elif more in ["N", 'n']:
            print('❕오늘의 일기 기록은 종료합니다 :)')
            print()
            break
        else:
            print('⚠️재입력하세요.')



    # 계산된 점수를 이용해서 기준치와 비교하기 ----------------------------------------------
    if happy >= 8 and angry < 8 and depressed < 8 :
        print('\n\n == [ 총 평 ] == \n')
        print(f'당신의 행복 점수는 15점 만점에 {happy}점')
        print(f'당신의 짜증 점수는 15점 만점에 {angry}점')
        print(f'당신의 우울 점수는 15점 만점에 {depressed}점')

        print('''
|￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
|    당신은 오늘 행복한 편이군요😉॰   |
|＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿|
　　         ᕱ ᕱ  ||
　         ( ᴖ ‧̫ ᴖ ||
  　        /　つ  Φ

￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣

        ''')
        print()




    else :
        print('\n\n ==[ 총 평 ] ')
        print(f'당신의 행복 점수는 15점 만점에 {happy}점')
        print(f'당신의 짜증 점수는 15점 만점에 {angry}점')
        print(f'당신의 우울 점수는 15점 만점에 {depressed}점\n')
        while True:
            print('❔당신의 기분을 개선시킬만한 게 있을까요?')
            print('❔없다면 조금 추천해드릴까요?')
            curious = input('🟢Y/N로 대답하세요: ')
            if curious in ['Y','y']:
                ysy.happything()
                break
            elif curious in ['N', 'n']:
                print('그럼 오늘의 기록은 종료됩니다. :)')
                print('\n')
                break
            else:
                print('⚠️재입력하세요.')

# =====================================================
# 함수 기능: 질문지에 사용자의 답변 넣기1
# 함수 이름: q_happy
# 매개 변수: q
# 함수 결과: 0~5 범위의 정수 출력
# =====================================================
def q_happy(q):

    while True:
        qAnswer = input(q)
        if qAnswer.isdecimal():

            q = int(qAnswer)

            if 0 <= q <= 5:
                # 설문조사 점수 계산하기
                global happy
                happy += q
                return happy

            else:
                print('⚠️답은 0~5 사이의 정수에서 입력하세요.\n')
        else:
            print('⚠️정수를 입력하세요.\n')
            q_happy(q)


# =====================================================
# 함수 기능: 질문지에 사용자의 답변 넣기2
# 함수 이름: q_angry
# 매개 변수: q
# 함수 결과: 0~5 범위의 정수 출력
# =====================================================
def q_angry(q):

    while True:
        qAnswer = input(q)
        if qAnswer.isdecimal():

            q = int(qAnswer)

            if 0 <= q <= 5:
                # 설문조사 점수 계산하기
                global angry
                angry += q
                return angry

            else:
                print('⚠️답은 0~5 사이의 정수에서 입력하세요.\n')
        else:
            print('⚠️정수를 입력하세요.\n')
            q_angry(q)




# =====================================================
# 함수 기능: 질문지에 사용자의 답변 넣기3
# 함수 이름: q_depressed
# 매개 변수: q
# 함수 결과: 0~5 범위의 정수 출력
# =====================================================
def q_depressed(q):
    while True:
        qAnswer = input(q)
        if qAnswer.isdecimal():

            q = int(qAnswer)

            if 0 <= q <= 5:
                # 설문조사 점수 계산하기
                global depressed
                depressed += q
                return depressed

            else:
                print('⚠️답은 0~5 사이의 정수에서 입력하세요.\n')
        else:
            print('⚠️정수를 입력하세요.\n')
            q_depressed(q)


# =====================================================
# 함수 기능: 짧은 일기 써서 저장하기
# 함수 이름: write
# 매개 변수: 없음
# 함수 결과: 없음
# =====================================================
from datetime import date, datetime

def write():
    while True:
        print('\n❕입력된 내용은 저장소에 보관됩니다.')
        diary = input('오늘의 나는 무슨 일이 있었을까?\n === 입력하기 ===\n')

        global diaryList
        diaryList.append(diary)

        # 일기 작성해서 파일에 저장하기
        filename = 'user_diary.txt'
        file = open(filename, mode = 'a' ,encoding = 'utf-8')
        file.write(diary)

        today = date.today()
        file.write(str(today))
        file.write('\n\n')



        print()

        print('❔더 입력을 원하시나요?')
        writeAnswer = input('🟢 Y와 N 중에서 입력하세요: ')
        if writeAnswer in ['Y', 'y']:
            write()
        elif writeAnswer in ['N', 'n']:
            print('오늘의 기록은 종료됩니다!')
            global writeValue
            writeValue = False
            break
        else:
            print('⚠️재입력하세요.')



# =====================================================
# 함수 기능: 저장된 시퀀스에서 데이터 꺼내오기
# 함수 이름: lookMood
# 매개 변수: 없음
# 함수 결과: 데이터 print
# =====================================================
def lookMood():
    print('당신의 일기 기록을 볼까요?')
    print('🟢 프로그램 시작한 후 바로 기록을 볼 경우 기록이 없습니다')
    print('🟢 만약 종료를 원하신다면 0을 입력해주세요. \n')

    diaryNum = int(input('당신의 몇 개의 기록을 보고싶나요?: '))
    if diaryNum > len(diaryList):
        print('⚠️조금 더 작은 수를 입력해주세요!')

    elif diaryNum == 0:
        print('일기 기록 보기는 종료됩니다.')

    else:
        for i in diaryList[-diaryNum:]:
            print('📜')
            print(i)
    print()




# ==========================================================================================================
# ==========================================================================================================
#                                   본 무대
# ==========================================================================================================
# ==========================================================================================================

import time

# 필요한 변수 선언
begin = True
diaryList = []
writeValue = True
happy = 0
angry = 0
depressed = 0



while begin:
    for repeat in range(1):
        print()
        programName = '''
▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀
▄▀   당신의 오늘 기분은?     ▄▀
▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀
        '''
        print(programName)

        print('      M E N U  ')
        print('  1. 오늘의 기분을 기록하기')
        print('  2. 짧은 일기 작성하기')
        print('  3. 지난 날의 일기 보기')
        print('  4. 종료 \n')

        # 사용자에게서 메뉴 입력 받기 ------------------------------------------------
        user = input('+++ 사용할 메뉴의 번호를 입력하세요: ')
        print()

        # 입력받은 것이 정수이면 메뉴별 기능 실행---------------------------------------
        if user.isdecimal():
            if user == '1' :
                print('💠오늘의 기분 기록하기💠')
                newMood()

                time.sleep(5)

            elif user == '2' :
                print('💠오늘의 짧은 일기 작성하기💠')
                write()

                time.sleep(3)

            elif user == '3' :
                print('💠지난 날의 일기 보기💠')
                lookMood()

                time.sleep(3)

            elif user == '4' :
                ysy.print_end()

                begin = False
            else :
                print('⚠️메뉴 속 번호를 입력하세요\n\n\n')

        else:
            print('⚠️숫자를 입력하세요.\n\n\n')



            # 첫 실행 후 메뉴 재실행 여부 -------------------------------------------
            if user == 4:
                pass

            else :
                print('❔메뉴를 다시 보시겠습니까?')
                menu_again = input('🟢Y 또는 N으로 입력하세요: ')

                if menu_again in ['Y', 'y']:
                    print('메뉴로 돌아갑니다!')

                elif menu_again in ['N', 'n']:
                    ysy.print_end()

                    begin = False
