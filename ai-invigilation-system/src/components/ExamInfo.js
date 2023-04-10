// import React, { Component } from "react";
import { useLocation } from "react-router-dom";
import React, { useEffect, useState } from "react";

// function ExamInfo(props) {

//   return (
//     <div className="parent">
//       <div className="header">AI Invigilator System</div>

//       <div className="body">
//         <h1>Exam Information</h1>

//         <p>{location.state.name}</p>

//         <p>Exam name : MATH 1A03 Final Examination</p>
//         <p>Start time : 2022/01/01 15:30</p>
//         <p>Start time : 2022/01/01 17:30</p>

//         <p>Time remaining : 2h 00min</p>
//       </div>
//     </div>
//   );
// }

// export default ExamInfo;

export default function ExamInfo() {
  const location = useLocation();
  const formData = location.state?.formData;

  return (
    <div className="parent">
      <div className="header">AI Invigilator System</div>

      <div className="body">
        <h1>Exam Information</h1>

        <p>Exam name : {formData?.name}</p>
        <p>Start time : {formData?.start}</p>
        <p>End time : {formData?.end}</p>
      </div>
    </div>
  );
}
