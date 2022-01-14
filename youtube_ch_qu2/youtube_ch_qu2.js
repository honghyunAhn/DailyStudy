import express from "express";

const app = express();

const urlLogger = (req, res, next) => {
  console.log(`Path: ${req.url}`);
  next();
};
const timeLogger = (req, res, next) => {
  let day = new Date();
  let year = day.getFullYear(); // 년도
  let month = day.getMonth() + 1; // 월
  let date = day.getDate();
  console.log(`Time: ${year}.${month}.${date}`);
  next();
};
const securityLogger = (req, res, next) => {
  if (req.protocol === "https") {
    console.log(`Insecure`);
  } else {
    console.log(`Insecure ❌`);
  }
  next();
};
const protectorMiddleware = (req, res, next) => {
  const url = req.url;
  if (url === "/protected") {
    return res.send("<h1>Not Allowed</h1>");
  }
  next();
};

app.enable("trust proxy");
app.use(urlLogger);
app.use(timeLogger);
app.use(securityLogger);
app.use(protectorMiddleware);

app.get("/", (req, res) => res.send("<h1>Home</h1>"));
app.get("/protected", (req, res) => res.send("<h1>Protected</h1>"));

// Codesandbox gives us a PORT :)
app.listen(process.env.PORT, () => `Listening!✅`);
