window.addEventListener("resize", function () {
    if (window.innerWidth > 1200) {
      document.body.style.background = "#ab47bc";
    } else if (window.innerWidth > 800) {
      document.body.style.background = "#fbc02d";
    } else {
      document.body.style.background = "#42a5f5";
    }
  });
  