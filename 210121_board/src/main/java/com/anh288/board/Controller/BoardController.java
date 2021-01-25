package com.anh288.board.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.anh288.board.dao.BoardDAO;

@Controller
@RequestMapping("board")
public class BoardController {

	@Autowired
	BoardDAO dao;
	
	@RequestMapping(value="join", method=RequestMethod.GET)
	public String joinForm() {
		return "memberView/joinForm";
	}
}
