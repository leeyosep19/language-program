<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

     <div class="wrapper">
     	<header></header>
     	<main style="width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center;">
     	<form action="./LoginProc.jsp" style="width: 300px; padding: 20px; border: 1px solid; border-radius: 10px;">
     <div>
     	<h2 style="text-align: center;">LOGIN</h2>
     </div>
     <div class="m-2">
     	<label  for=""></label>
     	<input type="text" class="from-control" name="username"/>
     </div>
     <div class="m-2">
     	<label  for=""></label>
     	<input type="text" class="from-control" name="password"/>
     </div>
     <div class="m-2">
     
     	<input type="checkbox" class="form-check-input" name="idchr"/><label for="" class="form-check-label">ID저장</label>
     </div>
     
     <div class="m-2">
     	<button class="but btu-primary w-100" >로그인</button>
     </div>
     
     <div class="m-2">
     	<button class="but btu-primary w-100">회원가입</button>
     </div>
     
     <div class="m-2" style="text-align:center;font-size:.8rem;color:orange;">
			${message}
	</div>		
     </form>
     </main>
     </div>

</body>
</html>