<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
 <%
 	//request Attribute 값 추가
 	request.setAttribute("ID1", "USER1");
 	request.setAttribute("PW1", "1234");
 	
 	//session Attribute 값 추가
 	session.setAttribute("ID2", "USER2");
 	session.setAttribute("PW2", "5678");
 	
 %>   
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

	<a href="./getSession.jsp">속성 정보 확인하기</a>
	
	

</body>
</html>