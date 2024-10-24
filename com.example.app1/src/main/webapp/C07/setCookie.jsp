<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<!-- 
    문자열 데이터만 저장 가능
    4kbyte 이하의 공간을 차지
    여러개의 쿠키 설정 가능(최대 300개)
    도메인당 20개까지 저장 가능
    저장한도 초과하면 최근에 사용되지 않은 쿠키부터 자동 삭제    
-->

<%
    // Creating the first cookie
    Cookie cookie1 = new Cookie("myCookie1", "myCookie1Value");
    cookie1.setMaxAge(30); // Cookie will expire after 30 seconds
    response.addCookie(cookie1); // Add cookie1 to the response

    // Creating the second cookie
    Cookie cookie2 = new Cookie("myCookie2", "myCookie2Value");
    cookie2.setMaxAge(60 * 5); // Cookie will expire after 5 minutes
    response.addCookie(cookie2); // Add cookie2 to the response
%>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Insert title here</title>
</head>
<body>

    <a href="getCookie.jsp"> 쿠키확인</a>

</body>
</html>
