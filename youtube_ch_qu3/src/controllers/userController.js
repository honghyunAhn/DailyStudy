export const join = (req, res) => res.send("Join");
export const login = (req, res) => res.send("Login");
export const user = (req, res) => res.send("User");
export const editUser = (req, res) => res.send("Edit User");
export const userId = (req, res) => {
	res.send(`Id : ${req.params.id}`);
};