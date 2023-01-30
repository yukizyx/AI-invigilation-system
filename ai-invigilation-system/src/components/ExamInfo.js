import React, { Component } from "react";
import { useLocation } from "react-router-dom";
import { withRouter } from "react-router";

function ExamInfo(props) {
  // const exam_name = props.location.param1;
  // let location = useLocation();

  // console.log(location);

  return (
    <div className="parent">
      <div className="header">AI Invigilator System</div>

      <div className="body">
        <h1>Exam Information</h1>

        <p>Exam name : MATH 1A03 Final Examination</p>
        <p>Start time : 2022/01/01 15:30</p>
        <p>Start time : 2022/01/01 17:30</p>

        <p>Time remaining : 2h 00min</p>
      </div>
    </div>
  );
}

export default ExamInfo;
