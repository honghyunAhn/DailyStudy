package com.anh288.board.vo;

import lombok.Data;

@Data
public class BoardVO {
	private int boardnum;
	private String id;
	private String contents;
	private String inputedate;
	private int hits;
	private String originalfile;
	private String savedfiles;
}
