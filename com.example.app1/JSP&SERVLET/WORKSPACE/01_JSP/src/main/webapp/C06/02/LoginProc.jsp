<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

    
<%
	String userid = request.getParameter("userid");
	String password = request.getParameter("password");
	
	//유효성체크(NULL)
	if(userid.isEmpty()){
		//out.println("<script>alert('userID를 입력하세요.');location.href='./Login.jsp'</script>");
		request.setAttribute("userid_msg", "Id를 입력하세요.");
		request.getRequestDispatcher("./Login.jsp").forward(request,response);
		return ;
	}
	if(password.isEmpty()){
		//out.println("<script>alert('Password를 입력하세요.');location.href='./Login.jsp'</script>");
		request.setAttribute("password_msg", "Password를 입력하세요.");
		request.getRequestDispatcher("./Login.jsp").forward(request,response);
		return ;
	}

	//DB에 저장된 데이터 확인(생략)
	
	
	//세션에 사용자 인증정보 저장
	session.setAttribute("id", userid);
	session.setAttribute("isLogined", true);
	session.setAttribute("role", "ROLE_USER");
	session.setMaxInactiveInterval(30); //기본 1800초(30분) , 30초 설정
	
	out.println("<script>alert('로그인 성공! MainPage로 이동합니다.');location.href='Main.jsp'</script>");
		
%>

