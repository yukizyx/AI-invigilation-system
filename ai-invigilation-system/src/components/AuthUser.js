import React from "react";
import axios from "axios";
import "./Auth.css";
import { Link } from "react-router-dom";

export function AuthSupervisor() {
  const formLogin = (e) => {
    e.preventDefault();
    axios
      .post("http://localhost:5000/auth-supervisor", {
        email: document.getElementById("email").value,
      })
      .then((res) => {
        console.log(res.data);
      });
  };
  return (
    <div className="parent">
      <div className="header">AI Invigilator System</div>

      <div className="body">
        <div>Supervisor Authentication</div>

        <form
          onSubmit={formLogin}
          action="http://localhost:5000/auth-supervisor"
          method="post"
        >
          <div className="form-field">
            <label for="field1">
              <span>Institution ID :</span>
              <input type="text" id="email" />
            </label>
            <label>
              {/* <span> </span> */}
              <input type="submit" value="Send Code" className="btn-usertype" />
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
  const formLogin = (e) => {
    e.preventDefault();
    axios
      .post("http://localhost:5000/auth-staff", {
        email: document.getElementById("email").value,
      })
      .then((res) => {
        console.log(res.data);
      });
  };
  return (
    <div className="parent">
      <div className="header">AI Invigilator System</div>

      <div className="body">
        <div>Staff Authentication</div>

        <form
          onSubmit={formLogin}
          action="http://localhost:5000/auth-staff"
          method="post"
        >
          <div className="form-field">
            <label for="field1">
              <span>Institution ID :</span>
              <input type="text" id="email" />
            </label>
            <label>
              {/* <span> </span> */}
              <input type="submit" value="Send Code" className="btn-usertype" />
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
              <Link to="../staff-home" className="btn-usertype">
                Login
              </Link>
            </label>
          </div>
        </form>
      </div>
    </div>
  );
}
