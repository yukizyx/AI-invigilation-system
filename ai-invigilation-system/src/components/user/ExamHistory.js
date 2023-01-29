export default function ExamHistory() {
  return (
    <div>
      <h1>Exam History</h1>
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">Date</th>
            <th scope="col">Exam Name</th>
            <th scope="col">Recording</th>
            <th scope="col">Reports</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">2022/01/01</th>
            <td>MATH 1A03 Final Exam</td>
            <td>Open</td>
            <td>Open</td>
          </tr>
          <tr>
            <th scope="row">2021/11/20</th>
            <td>MATH 1A03 Midterm Exam</td>
            <td>Open</td>
            <td>Open</td>
          </tr>
          <tr>
            <th scope="row">2021/07/26</th>
            <td>MATH 1B03 Midterm Exam</td>
            <td>Open</td>
            <td>Open</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}
