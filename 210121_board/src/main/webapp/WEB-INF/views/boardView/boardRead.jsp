<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Board Read</title>
<link rel="stylesheet" href="../resources/css/default.css">
<script type="text/javascript">
function deleteCheck(boardnum){
	if(confirm("정말 삭제하시겠습니까?")){
		location.href = 'delete?boardnum=' + boardnum;
	}
}
</script>
</head>
<body>
	<div class="centerdiv">
	
		<h2>[ 게시판 글읽기 ]</h2>
	
		<table>
			<tr>
				<th style="width:100px;">작성자 </th>
				<td style="width:600px;">${board.id}</td>
			</tr>
			<tr>
				<th>작성일 </th>
				<td>${board.inputdate}</td>
			</tr>
			<tr>
				<th>조회수 </th>
				<td>${board.hits}</td>
			</tr>
			<tr>
				<th>제목 </th>
				<td>${board.title}</td>
			</tr>
			<tr>
				<th>내용 </th> 
				<td><pre>${board.contents}</pre></td>
			</tr>
			<tr>
				<th>파일첨부 </th> 
				<td>
					<c:if test="${board.originalfile != null}">
					<a href="download?boardnum=${board.boardnum}">
						${board.originalfile}
					</a>
					</c:if>
				</td>
			</tr>
		</table>
	
		<div id="navigator">
			<c:if test="${loginId == board.id}">
			<a href="javascript:deleteCheck(${board.boardnum})">삭제</a>
			<a href="edit?boardnum=${board.boardnum}">수정</a>
		</c:if>
		<a href="list">목록보기</a>
		</div>
	</div>
</body>
</html>