package com.anh288.board.vo;

import lombok.Data;

@Data
public class BoardVO {
	private int boardnum;
	private String id;
	private String title;
	private String contents;
	private String inputdate;
	private int hits;
	private String originalfile;
	private String savedfiles;
}
