<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Board list</title>
<link rel="stylesheet" href="../resources/css/default.css">
</head>
<body>
	<div class="centerdiv">
		<h1>[ 게시판 ]</h1>
		<table>
			<tr>
				<td class="white">전체 : ${navi.totalRecordsCount}</td>
				<td class="white" colspan="3"></td>
				<td class="white">
					<input type="button" value="글쓰기" onClick="location.href='write';">
				</td>
			<tr>
				<td>번호</td>
				<th style="width:220px">제목</th>
				<td>작성자</td>
				<td>조회수</td>
				<td>등록일</td>
			</tr>
			<c:forEach var="board" items="${boardlist}">
			<tr>
				<td class="center">${board.boarnum}</td>
				<td><a href="read?boardnum=${board.boardnum}">${board.title}</a></td>
				<td class="center">${board.id}</td>
				<td class="center">${board.hits}</td>
				<td>${board.inputdate}</td>
			</tr>
			</c:forEach>
		</table>
		<br>
		<br>
	</div>
</body>
</html>