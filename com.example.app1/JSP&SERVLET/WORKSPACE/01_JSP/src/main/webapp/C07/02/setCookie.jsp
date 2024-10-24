<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
    <!--  
    	Cookie
    	문자열 데이터만 저장가능
    	4Kbyte 이하의 공간을 차지
    	여러개의 쿠키 설정가능(최대 300개)
    	도메인당 20개까지 저장가능
    	저장한도를 초과하면 최근에 사용되지 않는 쿠키부터 자동삭제
    -->
<%
	Cookie cookie1 = new Cookie("c1","v1");
	cookie1.setMaxAge(60*10);  
	cookie1.setPath("/");	//현재 도메인 내 모든 URI에 전달(모든 페이지로 해당 쿠키 전달)				
							
	Cookie cookie2 = new Cookie("c2","v2");
	cookie2.setMaxAge(60*10);
	cookie2.setPath("./");	//현재 패키지 내에 있는 페이지로만 전달
	
	Cookie cookie3 = new Cookie("c3","v3");
	cookie3.setMaxAge(60*10);
	cookie3.setPath("/01_JSP/C07/02/getCookie.jsp");	//지정된 페이지로만 전달
	
	response.addCookie(cookie1);
	response.addCookie(cookie2);
	response.addCookie(cookie3);
	
	
%>    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

	<a href="./getCookie.jsp">쿠키확인하기</a>

</body>
</html>