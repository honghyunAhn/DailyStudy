package com.anh288.board.dao;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.anh288.board.vo.MemberVO;

@Repository
public class MemberDAO {

	@Autowired
	SqlSession sqlSession;

	public int insert(MemberVO member) {
		MemberMapper mapper = sqlSession.getMapper(MemberMapper.class);
		int result = 0;
		
		try {
			result = mapper.insertMember(member);
		}
		catch (Exception e){
			e.printStackTrace();
		}
		return result;
	}

	public MemberVO getMember(String searchId) {
		MemberMapper mapper = sqlSession.getMapper(MemberMapper.class);
		MemberVO member = null;
		
		try {
			member = mapper.getMember(searchId);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return member;
	}

	public int updateMember(MemberVO member) {
		MemberMapper mapper = sqlSession.getMapper(MemberMapper.class);
		int result = 0;
		
		try {
			result = mapper.updateMember(member);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return result;
	}
}
