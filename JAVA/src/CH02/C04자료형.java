package CH02;

public class C04자료형 {

	public static void main(String[] args) {
//		//--------------------
//		//정수 int - 4byte 정수 부호 o
//		//--------------------
//		int n1 = 0b10101101;	//2진수값
//		int n2 = 173;			//10진정수값
//		int n3 = 0255;			//8진수
//		int n4 = 0xad;			//16진수
//		System.out.printf("%d %d %d %d\n", n1,n2,n3,n4);
		//--------------------
		//정수 byte - 1byte 정수 부호 o
		//--------------------
//		byte n5 = (byte)129;
//		byte n6 = -30;
//		byte n7 = 30;
//		byte n8 = 127;
//		byte n9 = (byte)129;	//왜?? 컴파일에러가??
//		System.out.printf("%d\n", n5); //왜 ?? 
//		System.out.println(0b10101101); //왜 ?? 음수아냐?
//		System.out.println(Integer.toBinaryString(-129));
		
//		//--------------------
//		//정수 short-2byte정수 부호o | char-2byte정수 부호x(양수만)
//		//--------------------
//		char n1 = 65535;  //(0~2^16-1)	(0~65535)
//		short n2 = 32767; //(-2^15 ~ +2^15-1)(-32768 ~ + 32767)
//		
//		char n3=60000;
//		short n4 = (short)n3; //문제발생... 왜??
//		
//		System.out.printf("%d\n",n4);		
		
//		//--------------------
//		//정수 long-8byte 정수 부호o
//		//--------------------
//		
//		long n1 = 10000000000L;
//		long n2 = 20;	//L,l (리터럴접미사) : long 자료형 사용하여 값 저장 
//		
//		long n3 = 10000000000L;//문제발생.. 왜?
//		long n4 = 10000000000L;
		
//		//--------------------
//		//실수
//		//--------------------
//		//유리수와 무리수의 통칭
//		//소숫점이하값을 가지는 수 123.456
//		//float : 4byte 실수(6-9자리)
//		//double : 8byte 실수(15-18자리),기본자료형
//		
//		//정밀도 확인
//		float n1 = 0.123456789123456789F; //f,F:float형 접미사
//		double n2 = 0.123456789123456789;
//		
//		System.out.println("Float : "+(0.44444444444444444444F));
//		System.out.println("Float : "+(0.77777777777777777777777777777777F));
//		System.out.println("Float : "+(0.99999999999999999999999999999999F));
//		System.out.println("Float : "+(0.22222222222222222222222222222222F));
//		System.out.println(0.77777777777777777777777777777777);
//		System.out.println("Double : "+(0.99999999999999999999999999999999));
//		System.out.println("Double : "+(0.22222222222222222222222222222222));
//		
//		System.out.println(n1);
//		System.out.println(n2);

//		//--------------------
//		//단일문자 char 2byte 정수
//		//--------------------
//		char ch1 = 'a';
//		System.out.println(ch1);
//		System.out.println((int)ch1); // 011000001
//
//		char ch2 = 98;
//		System.out.println(ch2);
//		System.out.println((int)ch2); // 011000010
//		
//		char ch3 = 'b'+1;
//		System.out.println(ch3);
//		System.out.println((int)ch3); // 011000011
//		
//		int ch4 = 'c'+2;
//		System.out.println((char)ch4);
//		System.out.println(ch4); // 011000011		
//		
//		char ch5 = 0xac00;
//		char ch6 = 44035;
//		System.out.println(ch5);
//		System.out.println(ch6);
//		System.out.println((char)0b01110111);
//		
//		
//		System.out.printf("%c \n",'\uac00');
		
		//--------------------
		//boolean : 논리형(true/false 저장)
		//--------------------		
//		boolean flag = (10>11); 	// 참(긍정)
//		if(flag) 
//		{
//			System.out.println("참인경우 실행");
//		}
//		else 
//		{
//			System.out.println("거짓인경우 실행");
//		}	
		
		//--------------------
		//문자열 : String (클래스자료형)
		//--------------------
//		
//		//기본자료형(원시타입)
////		byte n1;
////		short n2;
////		double n3;
////		long n4;
//		
//		//클래스자료형
//		//클래스자료형으로 만든변수는 '참조변수'라고 하고
//		//참조변수는 데이터가 저장된 위치정보(메모리주소값)이 저장된다.
//		int n1 = 10;
//		byte n2 = 20;
//		char n3 = 40;
//		
//		String name = "홍길동";
//		String job = "프로그래머";
//		System.out.println(name);
//		System.out.println(job);
//		System.out.printf("%x",System.identityHashCode(name));
		

		

	}

}
