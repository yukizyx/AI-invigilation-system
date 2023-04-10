import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

export default function CreateExam() {
  const [formData, setFormData] = useState({
    name: "MATH 1A03 Final Exam",
    start: "yyyy/mm/dd/hh/mm",
    end: "yyyy/mm/dd/hh/mm",
  });
  const navigate = useNavigate();

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevFormData) => ({ ...prevFormData, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    navigate("/../../exam-info", { state: { formData } });
  };

  return (
    <div>
      <h1>Create Exam</h1>
      <form className="form-field" onSubmit={handleSubmit}>
        <div style={{ padding: "20px" }}>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            label="Name"
            value={formData.name}
            onChange={handleInputChange}
          />
        </div>

        <div style={{ padding: "20px" }}>
          <label htmlFor="start">Start Time:</label>
          <input
            type="text"
            id="start"
            name="start"
            value={formData.start}
            onChange={handleInputChange}
          />
        </div>

        <div style={{ padding: "20px" }}>
          <label htmlFor="start">End Time:</label>
          <input
            type="text"
            id="end"
            name="end"
            value={formData.end}
            onChange={handleInputChange}
          />
        </div>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
}
