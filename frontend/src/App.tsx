import { useEffect, useState } from 'react';
import './App.css';
import { SchoolService, Student } from './clientapi';




function App() {
  const [students, setStudents] = useState<Student[] | undefined>()

  useEffect(() => {
    SchoolService.getSchoolStudent({name: "SCHOOL1"}).then(r => setStudents(r))
  }, [])


  return (
    <div className="App">
      <header className="App-header">
        <h2>Here are the students of SCHOOL1</h2>
        <pre>
          {JSON.stringify(students, null, 2)}
        </pre>
      </header>
    </div>
  );
}

export default App;
