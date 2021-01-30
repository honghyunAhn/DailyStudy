package com.anh288.board.dao;

import java.util.ArrayList;

import org.apache.ibatis.session.RowBounds;

import com.anh288.board.vo.BoardVO;
import com.anh288.board.vo.ReplyVO;

public interface BoardMapper {

	public ArrayList<BoardVO> boardlist(String searchText, RowBounds rb);

	public int countBoard(String searchText);

	public void insertBoard(BoardVO board);

	public BoardVO getBaord(int boardnum);

	public void hitBoard(int boardnum);

	public int delBoard(BoardVO board);

	public int editBoard(BoardVO board);

	public int insertReply(ReplyVO reply);

	public ArrayList<ReplyVO> getReply(int boardnum);

	public int replyEdit(ReplyVO reply);

	public int replyDelete(ReplyVO reply);
}
