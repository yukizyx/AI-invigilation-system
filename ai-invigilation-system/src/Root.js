import React from "react";

import "./Root.css";

import { Outlet } from "react-router-dom";
import Footer from "./components/Footer";

export default function Root() {
  return (
    <div className={"root"}>
      <div className={"rootUpper"}>
        <div className={"outlet"}>
          <Outlet />
        </div>
      </div>
      <Footer />
    </div>
  );
}
