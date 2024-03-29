package com.anh288.board.dao;

import java.util.ArrayList;

import org.apache.ibatis.session.RowBounds;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.anh288.board.vo.BoardVO;
import com.anh288.board.vo.ReplyVO;

@Repository
public class BoardDAO {
	
	@Autowired
	SqlSession sqlSession;

	public ArrayList<BoardVO> listBoard(String searchText, int startRecord, int countPerPage) {
		BoardMapper mapper = sqlSession.getMapper(BoardMapper.class);
		RowBounds rb = new RowBounds(startRecord, countPerPage);
		ArrayList<BoardVO> list = null;
		try {
			list = mapper.boardlist(searchText, rb);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return list;
	}

	public int countlist(String searchText) {
		BoardMapper mapper = sqlSession.getMapper(BoardMapper.class);
		int res = 0;
		try {
			res = mapper.countBoard(searchText);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return res;
	}

	public void insertBoard(BoardVO board) {
		BoardMapper mapper = sqlSession.getMapper(BoardMapper.class);
		try {
			mapper.insertBoard(board);
		} catch (Exception e) {
			e.printStackTrace();
		}
		
	}

	public BoardVO getBoard(int boardnum) {
		BoardMapper mapper = sqlSession.getMapper(BoardMapper.class);
		BoardVO board = null;
		try {
			mapper.hitBoard(boardnum);
			board = mapper.getBaord(boardnum);
		}catch (Exception e) {
			e.printStackTrace();
		}
		return board;
	}

	public int delBoard(BoardVO board) {
		BoardMapper mapper = sqlSession.getMapper(BoardMapper.class);
		int res = 0;
		try {
			res = mapper.delBoard(board);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return res;
	}

	public int editBoard(BoardVO board) {
		BoardMapper mapper = sqlSession.getMapper(BoardMapper.class);
		int result = 0;
		try {
			result = mapper.editBoard(board);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return result;
	}

	public int insertReply(ReplyVO reply) {
		BoardMapper mapper = sqlSession.getMapper(BoardMapper.class);
		int result = 0;
		try {
			result = mapper.insertReply(reply);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return result;
	}

	public ArrayList<ReplyVO> getReply(int boardnum) {
		BoardMapper mapper = sqlSession.getMapper(BoardMapper.class);
		ArrayList<ReplyVO> replylist = null;
		try {
			replylist = mapper.getReply(boardnum);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return replylist;
	}

	public int replyEdit(ReplyVO reply) {
		BoardMapper mapper = sqlSession.getMapper(BoardMapper.class);
		int result = 0;
		try {
			result = mapper.replyEdit(reply);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return result;
	}

	public int replyDelete(ReplyVO reply) {
		BoardMapper mapper = sqlSession.getMapper(BoardMapper.class);
		int result = 0;
		try {
			result = mapper.replyDelete(reply);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return result;
	}
}
