import TextField from "@mui/material/TextField";
import { Link } from "react-router-dom";

export default function CreateExam() {
  const onSubmitHandler = (e) => {
    e.preventDefault();
    this.props.history.push("./exam-info");
  };
  return (
    <div>
      <h1>Create Exam</h1>

      <form className="form-field" onSubmit={onSubmitHandler}>
        <div>
          <label for="field1">
            <span>Exam name : </span>
            <TextField
              id="demo-helper-text-misaligned-no-helper"
              label="Name"
            />
          </label>
        </div>

        <div>
          <label for="field2">
            <span>Start time : </span>
            <TextField
              id="demo-helper-text-misaligned-no-helper"
              label="yyyy/mm/dd/hh/mm"
            />
          </label>
        </div>

        <div>
          <label for="field3">
            <span>End time : </span>
            <TextField
              id="demo-helper-text-misaligned-no-helper"
              label="yyyy/mm/dd/hh/mm"
            />
          </label>
        </div>

        <div>
          <Link to="../../exam-info" target="_blank" className="btn-usertype">
            Save
          </Link>
        </div>
      </form>
    </div>
  );
}
