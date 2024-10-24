<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
    <%
    String cookieName = request.getParameter("cookieName");
    Cookie cookie = new Cookie(cookieName,"");
    cookie.setMaxAge(0);
    response.addCookie(cookie);
    
    %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>쿠키제거하기</h1>
쿠키제거완료!!!<br>
<a href="./getCookie.jsp">확인 </a>

</body>
</html>