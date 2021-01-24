package com.anh288.board.Controller;

import javax.servlet.http.HttpSession;

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
	public String joinForm() {
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
	
	@RequestMapping(value="idcheck", method=RequestMethod.GET)
	public String idCheck() {
		return "memberView/idCheck";
	}
	
	@RequestMapping(value="idcheck", method=RequestMethod.POST)
	public String idCheck(Model model, String searchId) {
		MemberVO member = dao.getMember(searchId);
		model.addAttribute("member", member);
		model.addAttribute("searchId", searchId);
		
		return "memberView/idCheck";
	}
	
	@RequestMapping(value="login", method=RequestMethod.GET)
	public String login() {
		return "memberView/login";
	}
	
	@RequestMapping(value="login", method=RequestMethod.POST)
	public String login(Model model, HttpSession session, String id, String pw) {
		MemberVO member = dao.getMember(id);
		
		if(member != null && member.getPassword().equals(pw)) {
			session.setAttribute("loginId", member.getId());
			session.setAttribute("loginName", member.getName());
			return "redirect:/";
		}
		else{
			model.addAttribute("errorMsg", "ID 또는 비밀번호가 틀립니다.");
			return "memberView/login";
		}
	}
	@RequestMapping(value="logout", method=RequestMethod.GET)
	public String logout(HttpSession session) {
		session.removeAttribute("loginId");
		session.removeAttribute("loginName");
		return "redirect:/";
	}
	@RequestMapping(value="update", method=RequestMethod.GET)
	public String update() {
		return "memberView/update";
	}
}
