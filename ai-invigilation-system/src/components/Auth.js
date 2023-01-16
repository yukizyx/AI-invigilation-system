import React from "react";
import "./Auth.css";
import { Link } from "react-router-dom";

export default function MainPage() {
  return (
    <div className="parent">
      <div className="header">AI Invigilator System</div>

      <div className="body">
        <div>User Authentication</div>
        <div>
          <button className="btn-usertype">Supervisor</button>
        </div>
        <div>
          <button className="btn-usertype">Staff</button>
        </div>
      </div>
    </div>
  );
}
