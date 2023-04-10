import React, { useState } from "react";
import axios from "axios";

export default function SetupCams() {
  const [tableData, setTableData] = useState([
    {
      id: 1,
      name: "Main Camera 1",
      status: true,
    },
    {
      id: 2,
      name: "Main Camera 2",
      status: true,
    },
  ]);

  const handleCheckboxChange = (event, id) => {
    const newData = tableData.map((row) => {
      if (row.id === id) {
        return { ...row, status: event.target.checked };
      } else {
        return row;
      }
    });
    setTableData(newData);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const selectedRows = tableData.filter((row) => row.status);
    axios
      .post("/supervisor-home/setup-cams", { selectedRows })
      .then((response) => console.log(response.data))
      .catch((error) => console.log(error));
  };

  return (
    <div>
      <h1>Setup Cameras</h1>
      <div>
        <form onSubmit={handleSubmit}>
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Hardware Name</th>
                <th scope="col">Status</th>
              </tr>
            </thead>
            <tbody>
              {tableData.map((row) => (
                <tr key={row.id}>
                  <td>{row.name}</td>
                  <td>
                    <input
                      type="checkbox"
                      checked={row.status}
                      onChange={(event) => handleCheckboxChange(event, row.id)}
                    />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  );
}
