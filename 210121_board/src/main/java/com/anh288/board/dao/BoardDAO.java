package com.anh288.board.dao;

import java.util.ArrayList;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.anh288.board.vo.BoardVO;

@Repository
public class BoardDAO {

	@Autowired
	SqlSession sqlSession;

	public ArrayList<BoardVO> listBoard() {
		BoardMapper mapper = sqlSession.getMapper(BoardMapper.class);
		ArrayList<BoardVO> list = null;
		try {
			list = mapper.boardlist();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return list;
	}

	public int countlist() {
		BoardMapper mapper = sqlSession.getMapper(BoardMapper.class);
		int res = 0;
		try {
			res = mapper.countBoard();
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
}
