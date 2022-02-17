<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>LogIn</title>
<link rel="stylesheet" type="text/css" href="../resources/css/default.css" />
<script type="text/javascript">
function onlogin(){
	var id = document.getElementById("id");
	var pw = document.getElementById("pw");
	
	if(id.value.length < 3 || id.value.length > 10){
		alert("ID는 3~10자로 입력하세요.");
		id.focus();
		id.select();
		return false;
	}
	if(pw.value.length < 3 || pw.value.length > 10){
		alert("비밀번호는 3~10자로 입력하세요.");
		id.focus();
		id.select();
		return false;
	}
	return true;
}
</script>
</head>
<body>
	<div class="centerdiv">
		<h1>로그인</h1>
		<form id="login" action="login" method="post" onsubmit="return onlogin();">
			<table>
				<tr>
					<th>ID</th>
					<td><input type="text" id="id" name="id"></td>
				</tr>
				<tr>
					<th>PW</th>
					<td><input type="password" id="pw" name="pw"></td>
				</tr>
				<tr>
					<td class="white"></td>
					<td class="white">
						<div class="errorMsg">${errorMsg}</div>
					</td>
				</tr>
				<tr>
					<td colspan="2" class="center white"><input type="submit" value="Login" /></td>
				</tr>
			</table>
		</form>
	</div>
</body>
</html>