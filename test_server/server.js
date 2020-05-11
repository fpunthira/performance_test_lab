const express = require("express");
const bodyParser = require('body-parser')


var app = express();
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))


var mysql = require('mysql');

// var con = mysql.createConnection({
//   host: "172.17.0.1",
//   user: "netapp",
//   password: "Netapp1!",
//   database: "db"
// });



// con.connect((err) => {
//     if (err) {
//         throw err;
//     }
//     console.log('Connected to database');
// });

function registerUser(data){

    var sql = 'INSERT INTO MyGuests set ?';
    con.query(sql,data, function (err, result) {
        if (err) throw err;
        console.log("1 record inserted");
    });

}

app.post("/url", (req, res, next) => {
    registerUser(req.body)
    res.json(req.body).status(200);
});


app.listen(3000, () => {
    console.log("Server running on port 3000");
});


