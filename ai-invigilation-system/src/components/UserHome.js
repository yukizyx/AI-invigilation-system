import React from "react";
import "./Auth.css";
import "./UserHome.css";
import { Link, NavLink, Outlet, useNavigate } from "react-router-dom";

export function SupervisorHome() {
  return (
    <div className="parent">
      <div className="header">AI Invigilator System</div>

      <div className="body">
        <div className={"SupervisorHome"}>
          <div className={"leftSidebar nav nav-pills"}>
            <NavLink to={"/supervisor-home"} end={true} className="nav-link">
              Set Triggers
            </NavLink>
            <NavLink to={"/supervisor-home/create-exam"} className="nav-link">
              Create Exam
            </NavLink>
            <NavLink to={"/supervisor-home/exam-history"} className="nav-link">
              Exam History
            </NavLink>
            <NavLink to={"/supervisor-home/setup-cams"} className="nav-link">
              Setup Cameras
            </NavLink>
            <NavLink to={"/supervisor-home/log-out"} className="nav-link">
              Log Out
            </NavLink>
          </div>

          <div className={"rightPanel"}>
            <Outlet />
          </div>
        </div>
      </div>
    </div>
  );
}

export function StaffHome() {
  return (
    <div className="parent">
      <div className="header">AI Invigilator System</div>

      <div className="body">
        <div className={"StaffHome"}>
          <div className={"leftSidebar nav nav-pills"}>
            <NavLink to={"/staff-home"} end={true} className="nav-link">
              Setup Cameras
            </NavLink>
            <NavLink to={"/staff-home/log-out"} className="nav-link">
              Log Out
            </NavLink>
          </div>

          <div className={"rightPanel"}>
            <Outlet />
          </div>
        </div>
      </div>
    </div>
  );
}
