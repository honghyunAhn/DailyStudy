export const home = (req, res) => res.send("Home");
export const trending = (req, res) => res.send("Trending");
export const storyNew = (req, res) => res.send("New");
export const story = (req, res) => {
	res.send(`Story ${req.params.id}`);
}
export const editStory = (req, res) => {
	res.send(`Edit Story ${req.params.id}`);
}
export const deleteStory = (req, res) => {
	res.send(`Delete Story ${req.params.id}`);
}
