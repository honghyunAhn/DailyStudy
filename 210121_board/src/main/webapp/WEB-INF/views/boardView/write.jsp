<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Board Write</title>
<link rel="stylesheet" type="text/css" href="../resources/css/default.css" />

<script>
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
		<h1>[ 글쓰기 ]</h1>
		<form id="writeform" action="write"  method="post" onsubmit="return formCheck();">
			<table>
				<tr>
					<th>제목</th>
					<td>
						<input type="text" name="title" id="title" style="width:400px;">
					</td>
				</tr>
				<tr>
					<th>내용</th> 
					<td>
						<textarea name="contents" id="contents" style="width:400px;height:200px;resize:none;"></textarea>
					</td>
				</tr>
				<tr>
					<th>파일첨부</th> 
					<td>
						<input type="file" name="upload" size="30">
					</td>
				</tr>
				<tr>
					<td colspan="2" class="white center">
						<input type="submit" value="저장" />
					</td> 
				</tr>
			</table>
		</form>
	</div>
</body>
</html>