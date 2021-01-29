package com.anh288.board.Controller;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.util.ArrayList;

import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.FileCopyUtils;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.multipart.MultipartFile;

import com.anh288.board.HomeController;
import com.anh288.board.dao.BoardDAO;
import com.anh288.board.util.FileService;
import com.anh288.board.vo.BoardVO;
import com.anh288.board.vo.ReplyVO;

@Controller
@RequestMapping("board")
public class BoardController {

	@Autowired
	BoardDAO dao;
	
	private static final Logger logger = LoggerFactory.getLogger(HomeController.class);
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
		ArrayList<ReplyVO> replylist = dao.getReply(boardnum);
		model.addAttribute("replylist", replylist);
		model.addAttribute("board", board);
		return "boardView/boardRead";
	}
	
	@RequestMapping(value = "download", method = RequestMethod.GET)
	public String fileDownload(int boardnum, Model model, HttpServletResponse response) {
		BoardVO board = dao.getBoard(boardnum);
		
		//원래의 파일명
		String originalfile = new String(board.getOriginalfile());
		try {
			response.setHeader("Content-Disposition", " attachment;filename="+ URLEncoder.encode(originalfile, "UTF-8"));
		} catch (UnsupportedEncodingException e) {
			e.printStackTrace();
		}
		
		//저장된 파일 경로
		String fullPath = uploadPath + "/" + board.getSavedfiles();
		
		//서버의 파일을 읽을 입력 스트림과 클라이언트에게 전달할 출력스트림
		FileInputStream filein = null;
		ServletOutputStream fileout = null;
		
		try {
			filein = new FileInputStream(fullPath);
			fileout = response.getOutputStream();
			
			//Spring의 파일 관련 유틸
			FileCopyUtils.copy(filein, fileout);
			
			filein.close();
			fileout.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return null;
	}
	
	@RequestMapping(value="delete", method=RequestMethod.GET)
	public String boardDelete(int boardnum, Model model, HttpSession session) {
		String id = (String) session.getAttribute("loginId");
		BoardVO board = new BoardVO();
		board.setBoardnum(boardnum);
		board.setId(id);
		
		String savedfile = dao.getBoard(boardnum).getSavedfiles();
		
		int res = dao.delBoard(board);
		
		if(res == 1 && savedfile != null) {
			FileService.deleteFile(uploadPath + "/" + savedfile);
		}
		model.addAttribute("res", res);
		
		return "redirect:list";
	}
	
	@RequestMapping(value="edit", method=RequestMethod.GET)
	public String boardEdit(int boardnum, Model model) {
		BoardVO board = dao.getBoard(boardnum);
		model.addAttribute("board",board);
		return "boardView/boardEdit";
	}
	
	@RequestMapping(value="edit", method=RequestMethod.POST)
	public String boardEdit(BoardVO board, Model model,MultipartFile upload, HttpSession session) {
		String id = (String) session.getAttribute("loginId");
		BoardVO oldBoard = dao.getBoard(board.getBoardnum());
		if(oldBoard == null || !oldBoard.getId().equals(id)) {
			return "redirect:list";
		}
		board.setId(id);
		logger.debug("Board : {}", board);
		
		if(!upload.isEmpty()) {
			String savedfile = oldBoard.getSavedfiles();
			
			if(savedfile != null) {
				FileService.deleteFile(uploadPath + "/" + savedfile);
			}
			savedfile = FileService.saveFile(upload, uploadPath);
			
			board.setOriginalfile(upload.getOriginalFilename());
			board.setSavedfiles(savedfile);
		}
		int result = dao.editBoard(board);
		model.addAttribute("result", result);
		return "redirect:read?boardnum=" + board.getBoardnum();
	}
	@RequestMapping(value="replyWrite", method=RequestMethod.POST)
	public String replyWrite(ReplyVO reply, Model model, HttpSession session) {
		String id = (String) session.getAttribute("loginId");
		reply.setId(id);
		int result = dao.insertReply(reply);
		logger.debug("result : {}", result);
		model.addAttribute("result", result);
		return "redirect:read?boardnum=" + reply.getBoardnum();
	}
}
