<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Board list</title>
<link rel="stylesheet" href="../resources/css/default.css">
<script>
function pagingFormSubmit(currentPage) {
	var form = document.getElementById('pagingForm');
	var page = document.getElementById('page');
	page.value = currentPage;
	form.submit();
}
</script>
</head>
<body>
	<div class="centerdiv">
		<h2>[ 게시판 ]</h2>
		
		<br>
		<table>
			<tr>
				<td class="white">
					전체 : ${count}
				</td>
				<td class="white" colspan="3"></td>
				<td class="white">
					<c:if test="${loginId != null}">
					<input type="button" value="글쓰기" onClick="location.href='write';">
					</c:if>
				</td>
				
			</tr>
			<tr>
				<th>번호</th>
				<th style="width:220px">제목</th>
				<th>작성자</th>
				<th>조회수</th>
				<th>등록일</th>
			</tr>
		
			<c:forEach var="board" items="${boardlist}">
			<tr>
				<td class="center">${board.boardnum}</td>
				<td>
					<a href="read?boardnum=${board.boardnum}">${board.title}</a>
				</td>
				<td class="center">${board.id}</td>
				<td class="center">${board.hits}</td>
				<td>${board.inputdate}</td>
			</tr>
			</c:forEach>
		</table>
		<br>
		<br>
		
		<div id="navigator">
			<a href="javascript:pagingFormSubmit(${navi.currentPage - navi.pagePerGroup})">◁◁ </a> &nbsp;&nbsp;
			<a href="javascript:pagingFormSubmit(${navi.currentPage - 1})">◀</a> &nbsp;&nbsp;

			<c:forEach var="counter" begin="${navi.startPageGroup}" end="${navi.endPageGroup}"> 
				<c:if test="${counter == navi.currentPage}"><b></c:if>
					<a href="javascript:pagingFormSubmit(${counter})">${counter}</a>&nbsp;
				<c:if test="${counter == navi.currentPage}"></b></c:if>
			</c:forEach>
			&nbsp;&nbsp;
			<a href="javascript:pagingFormSubmit(${navi.currentPage + 1})">▶</a> &nbsp;&nbsp;
			<a href="javascript:pagingFormSubmit(${navi.currentPage + navi.pagePerGroup})">▷▷</a>
			<br>
			<br>
			<form id="pagingForm" method="get" action="list">
				<input type="hidden" name="page" id="page" />
				제목 : <input type="text"  name="searchText" value="${searchText}" />
				<input type="button" onclick="pagingFormSubmit(1)" value="검색">
			</form>
		</div>
	</div>
</body>
</html>