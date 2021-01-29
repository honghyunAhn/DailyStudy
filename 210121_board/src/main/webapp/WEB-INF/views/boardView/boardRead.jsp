<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE HTML>
<html>
<head>
<title>Board Read</title>
<link rel="stylesheet" type="text/css" href="../resources/css/default.css" />
<script type="text/javascript">
function deleteCheck(boardnum){
	if(confirm("정말 삭제하시겠습니까?")){
		location.href = 'delete?boardnum=' + boardnum;
	}
}
function replyFormCheck() {
	var retext = document.getElementById('retext');
	if (retext.value.length < 5) {
		alert('리플 내용을 입력하세요.');
		retext.focus();
		retext.select();
		return false;
	}
	return true;			
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
			<td>${board.inputdate }</td>
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
	<br>
	
	<c:if test="${loginId != null}">
	<form id="replyform" action="replyWrite" method="post" onSubmit="return replyFormCheck();">
		리플내용
		<input type="hidden" name="boardnum" value="${board.boardnum}" />
		<input type="text" name="text" id="retext" style="width:500px;" />
		<input type="submit" value="확인" />
	</form>
	</c:if>
	<br>

	<table class="reply">
	<c:forEach var="reply" items="${replylist}">
		<tr>
			<td class="replyid">
				<b>${reply.id}</b>
			</td>
			<td class="replytext">
				${reply.text}
			</td>
			<td class="replybutton">
				<c:if test="${loginId == reply.id}">
					[<a href="javascript:replyEditForm(${reply.replynum}, ${reply.boardnum}, '${reply.text}')">수정</a>]
				</c:if>
			</td>
			<td class="replybutton">
				<c:if test="${loginId == reply.id}">
					[<a href="javascript:replyDelete(${reply.replynum}, ${reply.boardnum })">삭제</a>]
				</c:if>
			</td>
		</tr>	
		<tr>
			<td class="white" colspan="4"><div id="div${reply.replynum}"></div></td>
		</tr>
	</c:forEach>
	</table>
	<br><br><br>
</div>
</body>
</html>