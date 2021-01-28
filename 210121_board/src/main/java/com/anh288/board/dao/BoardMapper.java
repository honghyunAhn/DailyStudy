package com.anh288.board.dao;

import java.util.ArrayList;

import com.anh288.board.vo.BoardVO;

public interface BoardMapper {

	public ArrayList<BoardVO> boardlist();

	public int countBoard();

	public void insertBoard(BoardVO board);

	public BoardVO getBaord(int boardnum);

	public void hitBoard(int boardnum);

	public int delBoard(BoardVO board);

}
