import express from "express";

const PORT = 6000;

const app = express();

const handleHome = (req, res) => {
  return res.send("I still love you.");
};
const handleLogin = (req, res) => {
  return res.send("Login here.");
};
const handleAbout = (req, res) => {
  return res.send("About me.");
};
const handleContact = (req, res) => {
  return res.send("Contact me.");
};

app.get("/", handleHome);
app.get("/login", handleLogin);
app.get("/about", handleAbout);
app.get("/contact", handleContact);

const handleListening = () =>
  console.log(`Server listenting on port http://localhost:${PORT}`);

app.listen(PORT, handleListening);