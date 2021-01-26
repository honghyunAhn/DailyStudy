package com.anh288.board.Controller;

import java.util.ArrayList;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.multipart.MultipartFile;

import com.anh288.board.dao.BoardDAO;
import com.anh288.board.util.FileService;
import com.anh288.board.vo.BoardVO;

@Controller
@RequestMapping("board")
public class BoardController {

	@Autowired
	BoardDAO dao;
	
	final String uploadPath = "/boardfile";
	
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
	
	@RequestMapping(value="write", method=RequestMethod.POST)
	public String boardWrite(BoardVO board, HttpSession session, MultipartFile upload) {
		String id = (String) session.getAttribute("loginId");
		board.setId(id);
		if (!upload.isEmpty()) {
			String savedfile = FileService.saveFile(upload, uploadPath);
			board.setOriginalfile(upload.getOriginalFilename());
			board.setSavedfiles(savedfile);
		}
		System.out.println(board);
		dao.insertBoard(board);
		return "redirect:list";
	}
	
	@RequestMapping(value="read", method=RequestMethod.GET)
	public String boardRead(int boardnum, Model model) {
		BoardVO board = dao.getBoard(boardnum);
		System.out.println(board);
		model.addAttribute("board", board);
		return "boardView/boardRead";
	}
}
