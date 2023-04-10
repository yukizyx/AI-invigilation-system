import { useLocation } from "react-router-dom";
import React from "react";

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
