import React, { useState, useEffect } from 'react';
// import logo from './logo.svg';
import './App.css';
import Form from "./Form.jsx"; 

function App() {
  const [student, setStudent] = useState(0);

  useEffect(() => {
    fetch('/db_version').then(res => res.json()).then(data => {
      console.log(data)
      setStudent(data);
    });
  
  }, []);

  return (
    <Form />
  );
}

export default App;