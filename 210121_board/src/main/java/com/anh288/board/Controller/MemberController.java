package com.anh288.board.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.anh288.board.dao.MemberDAO;
import com.anh288.board.vo.MemberVO;

@Controller
@RequestMapping("member")
public class MemberController {

	@Autowired
	MemberDAO dao;
	
	@RequestMapping(value="join", method=RequestMethod.GET)
	public String joinForm(Model model) {
		return "memberView/joinForm";
	}
	
	@RequestMapping(value="join", method=RequestMethod.POST)
	public String join(Model model, MemberVO member) {
		int result = dao.insert(member);
		if (result != 1) {
			return "memberView/joinForm";
		}
		return "redirect:/";
	}
}
