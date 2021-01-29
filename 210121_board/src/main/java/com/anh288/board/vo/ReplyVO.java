package com.anh288.board.vo;

import lombok.Data;

@Data
public class ReplyVO {
	private int replynum;
	private int boardnum;
	private String id;
	private String text;
	private String inputdate;
}
