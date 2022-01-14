import express from "express";
import { editStory, deleteStory, story } from "../controllers/storyController";

const storyRouter = express.Router();

storyRouter.get("/:id", story);
storyRouter.get("/:id/edit", editStory);
storyRouter.get("/:id/delete", deleteStory);

export default storyRouter;