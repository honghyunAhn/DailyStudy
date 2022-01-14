package com.anh288.board.dao;

import com.anh288.board.vo.MemberVO;

public interface MemberMapper {

	public int insertMember(MemberVO member);

	public MemberVO getMember(String searchId);

	public int updateMember(MemberVO member);

}
