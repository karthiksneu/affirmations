const http = require('http');
const httpProxy = require('http-proxy');

const proxy = httpProxy.createProxyServer();
const targetServer = 'http://localhost:5000'; // Replace with your backend server URL

const server = http.createServer((req, res) => {
    console.log(`Proxying request for: ${req.url}`);
    proxy.web(req, res, { target: targetServer });

    res.setHeader('Access-Control-Allow-Origin', '*'); // Replace with your frontend URL
    res.setHeader('Access-Control-Allow-Methods', '*');
    res.setHeader('Access-Control-Allow-Headers', '*'); // Adjust as per your headers needed
});

proxy.on('error', (err, req, res) => {
    console.error('Proxy Error:', err);
    res.writeHead(500, { 'Content-Type': 'text/plain' });
    res.end('Proxy Error');
});


const PORT = 3001; // Port for your proxy server
server.listen(PORT, () => {
    console.log(`Proxy server listening on port ${PORT}`);
});
