import { useEffect, useState } from 'react';
import './App.css';
import { School, SchoolService, Student } from './clientapi';


function App() {
  const [students, setStudents] = useState<Student[] | undefined>()
  const [school, setSchool] = useState<School | null>()

  useEffect(() => {
    SchoolService.getSchoolStudent({name: "SCHOOL1"}).then(r => setStudents(r))
    SchoolService.getSchool({name: "SCHOOL2"}).then(r => setSchool(r))
  }, [])


  return (
    <div className="App">
      <header className="App-header">
        <h2>Here are the students of SCHOOL1</h2>
        <p>
          Students: {students?.map(s => s.firstName).join(", ")}
        </p>
        <p>
          Second school students: {school?.students.map(s => s.firstName).join(", ")}
        </p>
      </header>
    </div>
  );
}

export default App;
