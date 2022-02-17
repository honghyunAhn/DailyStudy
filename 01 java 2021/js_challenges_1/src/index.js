// <⚠️ DONT DELETE THIS ⚠️>
const colors = ["#1abc9c", "#3498db", "#9b59b6", "#f39c12", "#e74c3c"];
// <⚠️ /DONT DELETE THIS ⚠️>

/*
✅ The text of the title should change when the mouse is on top of it.
✅ The text of the title should change when the mouse is leaves it.
✅ When the window is resized the title should change.
✅ On right click the title should also change.
✅ The colors of the title should come from a color from the colors array.
✅ DO NOT CHANGE .css, or .html files.
✅ ALL function handlers should be INSIDE of "superEventHandler"
*/
const title = document.querySelector("h2");
const superEventHandler = {
  handleMouseOver: function () {
    title.innerHTML = "The mouse is here!";
    title.style.color = colors[0];
  },
  handleMouseOut: function () {
    title.innerHTML = "The mouse is gone!";
    title.style.color = colors[1];
  },
  handleResize: function () {
    title.innerHTML = "You just resized!";
    title.style.color = colors[2];
  },
  handleContextMenu: function () {
    title.innerHTML = "That was a right click!";
    title.style.color = colors[3];
  }
};

title.addEventListener("mouseover", superEventHandler.handleMouseOver);
title.addEventListener("mouseout", superEventHandler.handleMouseOut);
window.addEventListener("resize", superEventHandler.handleResize);
window.addEventListener("contextmenu", superEventHandler.handleContextMenu);
