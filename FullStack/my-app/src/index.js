import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Welcome from './Welcome';
import Contador from './Contador';
import Clock from './Clock';
import NameForm from './Form2';
import Form from './Form3';


// criando as duas variaveis que será usado no arquivo Welcome repare que dentro do root.render quando rederizamos o welcome nos colocamos as duas variáveis dentro do welcome 
const name = "Guilherme";
const data = new Date().toISOString();

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
     <Welcome name={name} data={data} />
     <Contador />
     <Clock />
     <NameForm />
     <Form />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
