import Checkbox from "@mui/material/Checkbox";

export default function SetTriggers() {
  return (
    <div>
      <h1>Set Triggers</h1>
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Trigger Type</th>
            <th scope="col">Parameters</th>
            <th scope="col">Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">1</th>
            <td>Head Position Trigger</td>
            <td>Out-of-boundary</td>
            <td>
              <Checkbox defaultChecked />
            </td>
          </tr>
          <tr>
            <th scope="row">2</th>
            <td>Head Position Trigger</td>
            <td>Offset 30%+</td>
            <td>
              <Checkbox />
            </td>
          </tr>
          <tr>
            <th scope="row">3</th>
            <td>Gaze Position Trigger</td>
            <td>Look around 10s+</td>
            <td>
              <Checkbox defaultChecked />
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}
