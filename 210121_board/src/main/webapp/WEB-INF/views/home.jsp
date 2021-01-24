<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
	<title>Board_Home</title>
</head>
<body>
<h1>SpringWeb5 -SE Bank Step 4</h1>
<ul>
<c:if test="${loginId == null}">
	<li><a href="member/join">회원가입</a></li>
	<li><a href="member/login">로그인</a></li>
</c:if>
<c:if test="${loginId != null}">
	<p>${loginName}(${loginId})님 로그인 중</p>
	<li><a href="member/logout">로그아웃</a></li>
	<li><a href="member/update">개인정보 수정</a></li>
</c:if>
	<li><a href="member/login">게시판</a></li>
</ul>
</body>
</html>
