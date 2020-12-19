const protocol = require("http");
const fs = require("fs");
const host = "localhost";
const port = 80;

const options = {
    key: fs.readFileSync("privkeyA.pem"),
    cert: fs.readFileSync("certA.crt")
};

protocol.createServer(options, (req, res) => 
{
	res.writeHead(200);
	res.end("Hello world\n");
}).listen(port, host);

console.log(`Server running on http://${host}:${port}`)
