package CH02;

public class C03변수상수자료형 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 수(Data) : 선 저장 / 후 처리
		// 변수 : 개발자의 유지보수 측면에서 바뀔 가능성이 있는 수
		// 변수명 : 저장되어져 있는 변수 공간에 접근하기 위한 문자형태의 주소
		// 자료형 : 수(Data) 를 저장하고 데이터의 유형을 제한하기 위해 사용되는 예약어
		// ctrl + shift + f (코드라인정리)
		
		int n1;		//4byte 정수만 저장될 공간 형선 -> n1 이름부여(변수 정의)
		n1 = 10;	//10 리터럴상수값을 상수Pool공간에 저장한다음 n1공간에 대입 
		int n2 = 4;	//4 리터럴상수값을 상수Pool공간에 저장한다음 4byte공간 생성->n2이름부여->4 대입(초기화)
		int n3 = n1 + n2; //n1안의 값과 n2안의 값의 덧셈결과를 4byte공간 생성->n3이름부여->결과값 대입(초기화)
		System.out.println(n3);	//함수내에 변수명이 사용되면 변수안의 값으로 해석

	}

}
