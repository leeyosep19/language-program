<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%@page import="java.io.*" %>
	<%
		/* Redirect */
		//response.sendRedirect("02Request.jsp");
		
		//response.sendError(HttpServletResponse.SC_REQUEST_TIMEOUT,"요청시간(TIMEOUT)을 초과하였습니다");
		//response.sendError(HttpServletResponse.SC_OK,"정상처리완료");
		//response.sendError(HttpServletResponse.SC_NOT_FOUND,"해당페이지를 찾을수없습니다"); //404 - Client
		//response.sendError(HttpServletResponse.SC_FORBIDDEN,"해당페이지를 찾을수없습니다"); //403 - Client
		
		response.sendError(HttpServletResponse.SC_BAD_GATEWAY,"서버장애발생");
		
		/* 새로고침 */
		//response.setIntHeader("Refresh", 3);
		
		//OutStream 추출
		/*
		ServletOutputStream bout =  response.getOutputStream();
		bout.write('a');
		bout.write(98);
		bout.flush();
		bout.close();
		*/
		
		//PrintWriter 사용(Out내장객체와 유사)
		/*
		PrintWriter o = response.getWriter();
		o.println("<h1>TEST</h1>");
		//
		out.write("<h2>TEST2</h2>");
		*/
		
		
		
	%>
	
	<%@page import="java.util.*" %>
	<%=new Date() %>

</body>
</html>