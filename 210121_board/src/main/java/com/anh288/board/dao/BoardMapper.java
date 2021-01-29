package com.anh288.board.dao;

import java.util.ArrayList;

import com.anh288.board.vo.BoardVO;
import com.anh288.board.vo.ReplyVO;

public interface BoardMapper {

	public ArrayList<BoardVO> boardlist();

	public int countBoard();

	public void insertBoard(BoardVO board);

	public BoardVO getBaord(int boardnum);

	public void hitBoard(int boardnum);

	public int delBoard(BoardVO board);

	public int editBoard(BoardVO board);

	public int insertReply(ReplyVO reply);
}
