package com.anh288.board.Controller;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.anh288.board.dao.BoardDAO;
import com.anh288.board.vo.BoardVO;

@Controller
@RequestMapping("board")
public class BoardController {

	@Autowired
	BoardDAO dao;
	
	@RequestMapping(value="list", method=RequestMethod.GET)
	public String boardlist(Model model) {
		ArrayList<BoardVO> boardlist = dao.listBoard();
		int count = dao.countlist();
		model.addAttribute("boardlist",boardlist);
		model.addAttribute("count", count);
		return "boardView/boardlist";
	}
	
	@RequestMapping(value="write", method=RequestMethod.GET)
	public String boardWrite() {
		return "boardView/write";
	}
}
