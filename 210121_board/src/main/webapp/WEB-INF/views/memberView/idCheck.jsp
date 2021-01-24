<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet" type="text/css" href="../resources/css/default.css" />
<script type="text/javascript">
	function selectId(id) {
		opener.document.getElementById('id').value = id;
		this.close();
	}
</script>
</head>
<body>
<div class="centerdiv">
<h1>[ ID 확인 ]</h1>
<form action="idcheck" method="post">
검색할 ID <input type="text" name="searchId" id="searchId">
		<input type="submit" value="검색" />
</form>
<c:if test="${searchId != null}">
	<c:if test="${member == null}">
		<p>${searchId} : 사용할 수 있는 ID입니다.</p>
		<p><input type="button" value="ID사용하기" onclick="selectId('${searchId}')"></p>
	</c:if>
	<c:if test="${member != null}">
		<p>${searchId} : 이미 사용중인 ID입니다. </p>
	</c:if>
</c:if>

</div>
</body>
</html>