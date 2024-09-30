package CH19;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class C01Ex {
	static Scanner sc = new Scanner(System.in);

	public static void func1(List<String> list) {
		// 키보드로 부터 입력받는 수중에 짝수값만 list에 저장하세요

		Integer tmp = 0;

		while (tmp != -1) {
			try {
				System.out.print("입력(종료:-1) :");
	
				tmp = sc.nextInt();
				if (tmp % 2 == 0)
					list.add(String.valueOf(tmp));
				else
					System.out.println("[EXCEPTION]짝수만 입력하세요!");			
			
			}catch(InputMismatchException e) {
				System.out.println("[EXCEPTION]숫자만 입력하세요!");
				sc.next();//
			}
			
			
		}

		System.out.println("입력을 마쳤습니다.");
	}

	public static List<String> func2(List<String> list) {
		// ArrayList에 있는 문자열 중에서 길이가 5보다 큰 문자열만 필터링해서 리턴하는 함수를 만드세요
		List<String> returndList = new ArrayList();
		for (String el : list) {
			if (el.length() >= 5) {
				returndList.add(el);
			}
		}
		return returndList;
	}

	public static int func3(List<String> list) {
		// ArrayList에 있는 문자열 중에서 숫자형 데이터만 추출해서 합을 구해보세요
		int sum = 0;
		for (String el : list) {
			sum += Integer.parseInt(el);
		}
		return sum;
	}

	public static void main(String[] args) {
		List<String> li = new ArrayList();
		func1(li);
		List<String> returndList = func2(li);
		returndList.forEach(el -> System.out.print(el + " "));
		System.out.println();

		int sum = func3(li);
		System.out.println(sum);
	}

}
