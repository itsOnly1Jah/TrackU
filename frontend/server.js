import express from 'express'
import axios from 'axios'

const app = express()
const port = 3000

app.use(express.static('src'))

app.get('/chart', (req, res) => {
  axios.get('http://127.0.0.1:5000/chart')
  .then((flask) => {
    res.send(flask.data)
  })
  .then((error) => console.log(error));
});

app.get('/list', (req, res) => {
  axios.get('http://127.0.0.1:5000/list')
  .then((flask) => {
    res.send(flask.data)
  })
  .then((error) => console.log(error));
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`)
})
