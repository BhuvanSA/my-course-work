import React from "react";
import ReactDOM from "react-dom";
import App from "./components/App";
import emojiopedia from "./emojipedia";

function element(obj) {
	// console.log(obj.meaning);

	return obj.meaning.substring(0, 100);
}

const list = emojiopedia.map(element);
console.log(list);

ReactDOM.render(<App />, document.getElementById("root"));
