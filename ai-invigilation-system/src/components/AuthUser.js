import { React, useEffect, useState } from "react";
import "./Auth.css";

export function AuthSupervisor() {
  return (
    <div className="parent">
      <div className="header">AI Invigilator System</div>

      <div className="body">
        <div>Supervisor Authentication</div>

        <form action="http://localhost:5000/auth-supervisor" method="post">
          <div className="form-field">
            <label for="field1">
              <span>Institution ID :</span>
              <input type="text" name="id" />
            </label>
            <label>
              <input value="Send Code" className="btn-usertype" />
            </label>
          </div>
          <div className="form-field">
            <label for="field2">
              <span>Code :</span>
              <input type="password" name="code" />
            </label>
            <label>
              <input type="submit" value="Log In" className="btn-usertype" />
            </label>
          </div>
        </form>
      </div>
    </div>
  );
}

export function AuthStaff() {
  return (
    <div className="parent">
      <div className="header">AI Invigilator System</div>

      <div className="body">
        <div>Staff Authentication</div>

        <form action="http://localhost:5000/auth-staff" method="post">
          <div className="form-field">
            <label for="field1">
              <span>Institution ID :</span>
              <input type="text" name="id" />
            </label>
            <label>
              <input value="Send Code" className="btn-usertype" />
            </label>
          </div>
          <div className="form-field">
            <label for="field2">
              <span>Code :</span>
              <input type="password" name="code" />
            </label>
            <label>
              <input type="submit" value="Log In" className="btn-usertype" />
            </label>
          </div>
        </form>
      </div>
    </div>
  );
}
