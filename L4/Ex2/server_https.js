const protocol = require("https");
const fs = require("fs");
const host = "localhost";
const port = 443;

const options = {
    key: fs.readFileSync("privkeyA.pem"),
    cert: fs.readFileSync("certA.crt")
};

protocol.createServer(options, (req, res) => 
{
	res.writeHead(200);
	res.end("Hello world\n");
}).listen(port, host);

console.log(`server running on https://${host}:${port}`)	
