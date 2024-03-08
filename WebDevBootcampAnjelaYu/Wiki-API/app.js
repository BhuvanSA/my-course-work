// jshint esversion:6

const mongoose = require("mongoose");
const express = require("express");

const app = express();
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));

mongoose.connect("mongodb://127.0.0.1:27017/wikiDB");

const articleSchema = {
	title: String,
	content: String,
};

const Article = mongoose.model("Article", articleSchema);

///// REQUESTS TARGETING ALL ARTICLES ///////
app
	.route("/articles")
	.get(function (req, res) {
		Article.find()
			.then((foundArticles) => {
				res.send(foundArticles);
			})
			.catch((err) => {
				console.log(`Error at / :${err}`);
				res.send(err);
			});
	})
	.post(function (req, res) {
		const title = req.body.title;
		const content = req.body.content;

		const newArticle = new Article({
			title: title,
			content: content,
		});

		newArticle
			.save()
			.then(() => {
				res.send("application received");
			})
			.catch((err) => {
				res.send("Error at /articles");
				console.log(err);
			});
	})
	.delete(function (req, res) {
		Article.deleteMany()
			.then(() => {
				res.send("Successfully deleted all articles");
			})
			.catch((err) => {
				res.send("Something went wrong");
				console.log(err);
			});
	});

///// REQUESTS TARGETING SPECIFIC ARTICLES ///////

app
	.route("/articles/:articleTitle")
	.get(function (req, res) {
		Article.find({ title: req.params.articleTitle })
			.then((foundArticle) => {
				if (!foundArticle) {
					res.send("No articles matching that title was found.");
				} else {
					res.send(foundArticle);
					console.log(foundArticle);
				}
			})
			.catch((err) => {
				res.send(err);
				console.log(err);
			});
	})
	.put(function (req, res) {
		Article.findOneAndUpdate(
			{ title: req.params.articleTitle },
			{ title: req.body.title, content: req.body.content },
			{ overwrite: true },
		)
			.then((article) => {
				if (!article) {
					res.send("Article not found");
				} else {
					res.send("Successfully updated the article");
				}
			})
			.catch((err) => {
				res.send(err);
				console.log(err);
			});
	})
	.patch(function (req, res) {
		Article.findOneAndUpdate(
			{ title: req.params.articleTitle },
			{ $set: req.body },
		)
			.then((article) => {
				if (!article) {
					res.send("Article not found");
				} else {
					res.send("Successfully patched the article");
				}
			})
			.catch((err) => {
				res.send(err);
				console.log(err);
			});
	})
	.delete(function (req, res) {
		Article.findOneAndDelete({
			title: req.params.articleTitle,
		})
			.then((article) => {
				if (!article) {
					res.send("Article not found");
				} else {
					res.send("Article deleted Successfully");
				}
			})
			.catch((err) => {
				res.send(err);
			});
	});

app.listen(3000, function () {
	console.log("Server has started on port 3000");
});
