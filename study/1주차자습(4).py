"""
클래스 선언과 객체 생성

함수와 클래스 비유적 비교
    함수: 각각 덧셈, 뺄셈, 곱셈 등
    클래스: 사칙연산 클래스
    라이브러리: 클래스의 묶음
     예시)수학 라이브러리 = 사칙연산 클래스 + 미분 클래스 + 적분 클래스 (...)
"""

class Calculator:
    
    def __int__(self):
        self.result = 0 #result값을 초기화하는 메소드
    #init이란?
    #객체, 인스턴스 생성할 때 데이터를 초기화하는 메소드
    #
