const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

function handleConnection(req, res){
    res.statusCode = 200;
    if(req.method == "GET"){
        res.setHeader('Content-Type', 'text/plain');
        res.end('Premiere is alive');
    }
    if(req.method == "POST"){
        // download all body data (req only get header)
        let data = []
        req.on('data', function(chunk){
            data.push(chunk)
        })
        req.on('end', function(){
            console.log(JSON.parse(data)["to_eval"])
            // response
            res.setHeader('Content-Type', 'text/plain');
            res.end(JSON.stringify(monObject));
        })
    }
}

const server = http.createServer(handleConnection);

server.listen(port, hostname, function(){
  console.log('Server running at http://' + String(hostname) + ':' + String(port));
});


