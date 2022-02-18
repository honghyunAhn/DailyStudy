import express from "express";
import { user, editUser, userId } from "../controllers/userController";

const userRouter = express.Router();

userRouter.get("/", user);
userRouter.get("/edit-profile", editUser);
userRouter.get("/:id", userId);

export default userRouter;