import React, { useState } from "react";
import axios from "axios";

export default function SetTriggers() {
  const [tableData, setTableData] = useState([
    {
      id: 1,
      type: "Head Position Trigger",
      parameter: "is mouth open",
      status: true,
    },
    {
      id: 2,
      type: "Head Position Trigger",
      parameter: "head yaw",
      status: false,
    },
    {
      id: 3,
      type: "Head Position Trigger",
      parameter: "head pitch",
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
      .post("/supervisor-home", { selectedRows })
      .then((response) => console.log(response.data))
      .catch((error) => console.log(error));
  };

  return (
    <div>
      <h1>Set Triggers</h1>
      <div>
        <form onSubmit={handleSubmit}>
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Trigger Type</th>
                <th scope="col">Parameters</th>
                <th scope="col">Status</th>
              </tr>
            </thead>
            <tbody>
              {tableData.map((row) => (
                <tr key={row.id}>
                  <td>{row.type}</td>
                  <td>{row.parameter}</td>
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
