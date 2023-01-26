import Checkbox from "@mui/material/Checkbox";

export default function SetupCams() {
  return (
    <div>
      <h1>Setup Cameras</h1>
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Hardware Name</th>
            <th scope="col">Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">1</th>
            <td>Main Camera 1</td>
            <td>
              <Checkbox defaultChecked />
            </td>
          </tr>
          <tr>
            <th scope="row">2</th>
            <td>Main Camera 2</td>
            <td>
              <Checkbox />
            </td>
          </tr>
          <tr>
            <th scope="row">3</th>
            <td>Main Camera 3</td>
            <td>
              <Checkbox defaultChecked />
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}
