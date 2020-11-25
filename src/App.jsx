import React, { useState, useEffect } from 'react';
// import logo from './logo.svg';
import './App.css';

function App() {
  const [student, setStudent] = useState(0);

  useEffect(() => {
    fetch('/').then(res => res.json()).then(data => {
      console.log(data)
      setStudent(data.student);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">

        ... no changes in this part ...

        <p> Student Information is: {student}.</p>
      </header>
    </div>
  );
}

export default App;