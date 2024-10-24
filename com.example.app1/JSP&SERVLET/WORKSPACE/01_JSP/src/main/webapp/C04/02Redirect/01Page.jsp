<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
    <%@page import="java.net.*" %>
	<%
		String username=request.getParameter("username");
		String password=request.getParameter("password");
		System.out.println("----------01PAGE-------------");
		System.out.println("username : " + username);
		System.out.println("password : " + password);
		System.out.println("-----------------------------");
		
		//request 속성 추가
		//request.setAttribute("01PAGE","01VALUE");
		
		//Redirect처리
		//URLEncoder.encode()
		response.sendRedirect("02Page.jsp?username="+URLEncoder.encode(username,"UTF-8")+"&password="+password+"&01PAGE=01VALUE");
		
	%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	
	<h1>01PAGE</h1>
	USERNAME : <%=username %><br>
	PASSWORD : <%=password %><br>

</body>
</html>