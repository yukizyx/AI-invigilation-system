import TextField from "@mui/material/TextField";
import { Link } from "react-router-dom";
import { useState } from "react";
import React, { Component } from "react";

// export default class CreateExam extends Component {
//   state = {
//     name: "rajdeep singh",
//     love: "coding",
//     earn: "null",
//   };

//   render() {
//     return (
//       <>
//         <div>
//           <h1>Create Exam</h1>

//           <form className="form-field">
//             <div>
//               <label for="field1">
//                 <span>Exam name : </span>
//                 <TextField
//                   onChange={(newValue) =>
//                     this.setState({ name: newValue.target.value })
//                   }
//                   value={this.state.name}
//                   id="name-field"
//                   label="Name"
//                 />
//               </label>
//             </div>
//             <div>
//               <p>{this.state.name}</p>
//             </div>

//             <div>
//               <label for="field2">
//                 <span>Start time : </span>
//                 <TextField
//                   id="demo-helper-text-misaligned-no-helper"
//                   label="yyyy/mm/dd/hh/mm"
//                 />
//               </label>
//             </div>

//             <div>
//               <label for="field3">
//                 <span>End time : </span>
//                 <TextField
//                   id="demo-helper-text-misaligned-no-helper"
//                   label="yyyy/mm/dd/hh/mm"
//                 />
//               </label>
//             </div>
//           </form>

//           <div>
//             {/* <Link to={info} target="_blank" className="btn-usertype"> */}
//             {/* <Link to={{ pathname: "/../../exam-info", state: this.state }}> */}
//             <Link
//               to={"/../../exam-info"}
//               state="111111"
//               target="_blank"
//               className="btn-usertype"
//             >
//               Save
//             </Link>
//           </div>
//         </div>
//       </>
//     );
//   }
// }

export default function CreateExam() {
  const [name, setName] = useState("");

  let state = {
    name: "rajdeep singh",
    love: "coding",
    earn: "null",
  };

  const info = {
    pathname: "/../../exam-info",
    param1: `${name}`,
    // param2: `${lastName}`,
    // param3: `${email}`
  };

  return (
    <div>
      <h1>Create Exam</h1>

      <form className="form-field">
        <div>
          <label for="field1">
            <span>Exam name : </span>
            <TextField
              onChange={(newValue) => setName(newValue.target.value)}
              value={name}
              id="name-field"
              label="Name"
            />
          </label>
        </div>
        {/* <div>
          <p>{name}</p>
        </div> */}

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
      </form>

      <div>
        {/* <Link to={info} target="_blank" className="btn-usertype"> */}
        {/* <Link to={{ pathname: "/../../exam-info", state: state }}> */}
        <Link
          to={"/../../exam-info"}
          state={{ exam_name: name }}
          target="_blank"
          className="btn-usertype"
        >
          Save
        </Link>
      </div>
    </div>
  );
}
