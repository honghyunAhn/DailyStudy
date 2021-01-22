package com.anh288.board.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.anh288.board.dao.memberDAO;

@Controller
@RequestMapping("member")
public class MemberController {

	@Autowired
	memberDAO dao;
	
	@RequestMapping(value="join", method=RequestMethod.GET)
	public String joinForm(Model model) {
		return "memberView/joinForm";
	}
	
}
