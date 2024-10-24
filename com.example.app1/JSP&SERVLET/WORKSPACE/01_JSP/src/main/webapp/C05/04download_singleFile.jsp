<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@page import="java.io.*" %>
<%

	//Dir경로 생성
	String dirPath = pageContext.getServletContext().getRealPath("/")+"C05\\downloads\\";
	System.out.println("dirPath : " + dirPath);
	//Dir없으면 생성
	//File dir = new File(dirPath);
	//if(!dir.exists())
	//	dir.mkdirs();
	//
	try{
		//파일 InputStream 생성
		FileInputStream in = new FileInputStream(dirPath+"TEST.vbox-extpack");
		
		//내장객체(Out)정리
		out.clear();					//response outStream을 닫고 버퍼를 비움
		out = pageContext.pushBody(); 	//현재페이지에 Body 연결
		
		//OutStream 가져오기
		ServletOutputStream bout = response.getOutputStream();
		
		//response의 Header변경(중요!)
		response.setHeader("Content-Type","application/octet-stream;charset-utf-8");
		response.setHeader("Content-Disposition","attachment; filename=TEST.vbox-extpack");
		
		//inOutStream 전송
		byte [] buffer = new byte[4096];
		while(true){
			int data = in.read(buffer);
			if(data==-1)
				break;
			bout.write(buffer,0,data);
			bout.flush();		
		}
		bout.close();
		in.close();
		
	}catch(Exception e){
		e.printStackTrace();
	}
%>
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<title>Document</title>
</head>
<body>
	HELLO WORLD
</body>
</html>







