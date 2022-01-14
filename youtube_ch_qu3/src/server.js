import express from "express";

const app = express();

const globalRouter = express.Router();

const handleHome = (req, res) => res.send("Home");

globalRouter.get("/", handleHome);


const userRouter = express.Router();

const handleEditUser = (req, res) => res.send("Edit User");

userRouter.get("/edit-profile", handleEditUser);


const storyRouter = express.Router();

const handleEditStory = (req, res) => res.send("Edit Story");

storyRouter.get("/edit", handleEditStory);


app.use("/", globalRouter);
app.use("/users", userRouter);
app.use("/stories/:id", storyRouter);
// Codesanbox does not need PORT :)
app.listen(() => console.log(`Listening!`));
