<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Board Edit</title>
<link rel="stylesheet" type="text/css" href="../resources/css/default.css">
<script type="text/javascript">
function formCheck() {
	var title = document.getElementById('title');
	var contents = document.getElementById('contents');
	
	if (title.value.length < 5) {
		alert("제목을 입력하세요.");
		title.focus();
		title.select();
		return false;
	}
	if (contents.value.length < 5) {
		alert("내용을 입력하세요.");
		contents.focus();
		contents.select();
		return false;
	}
	return true;
}
</script>
</head>
<body>
<div class="centerdiv">
	<h2>[ 글수정 ]</h2>
	<form id="writeform" action="edit"  method="post" enctype="multipart/form-data" onsubmit="return formCheck();">
		<input type="hidden" name="boardnum" value="${board.boardnum }">
		<table>
			<tr>
				<td>제목</td>
				<td>
					<input type="text" name="title" id="title" style="width:400px;" value="${board.title}">
				</td>
			</tr>
			<tr>
				<td>내용</td> 
				<td>
					<textarea name="contents" id="contents" style="width:400px;height:200px;resize:none;">${board.contents}</textarea>
				</td>
			</tr>
			<tr>
				<td>파일첨부</td> 
				<td>
					<input type="file" name="upload" size="30">
					${board.originalfile}
				</td>
			</tr>
			<tr>
				<td colspan="2" class="white center">
					<input type="submit" value="수정">
				</td> 
			</tr>
		</table>
	</form>
</div>
</body>
</html>