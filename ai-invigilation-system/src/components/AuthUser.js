import React from "react";
import "./Auth.css";
import { Link } from "react-router-dom";

export function AuthSupervisor() {
  return (
    <div className="parent">
      <div className="header">AI Invigilator System</div>

      <div className="body">
        <div>Supervisor Authentication</div>

        <form action="" method="post">
          <div className="form-field">
            <label for="field1">
              <span>Institution ID :</span>
              <input type="text" class="input-field" name="field1" value="" />
            </label>
            <label>
              <span> </span>
              <input type="submit" value="Send Code" />
            </label>
          </div>
          <div className="form-field">
            <label for="field2">
              <span>Code :</span>
              <input
                type="password"
                class="input-field"
                name="field2"
                value=""
              />
            </label>
            <label>
              {/* <span> </span> */}

              {/* <input type="submit" value="Log In" /> */}
              <Link to="../supervisor-home" className="btn-usertype">
                Login
              </Link>
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
