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
          <Link to="../auth-supervisor" className="btn-usertype">
            Supervisor
          </Link>
        </div>
        <div>
          <Link to="../auth-staff" className="btn-usertype">
            Staff
          </Link>
        </div>
      </div>
    </div>
  );
}
