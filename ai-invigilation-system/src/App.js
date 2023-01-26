import React from "react";

import { createBrowserRouter, RouterProvider, Route } from "react-router-dom";

import MainPage from "./components/Auth.js";
import { AuthSupervisor, AuthStaff } from "./components/AuthUser.js";
import { SupervisorHome, StaffHome } from "./components/UserHome.js";

import CreateExam from "./components/user/CreateExam.js";
import SetTriggers from "./components/user/SetTriggers.js";
import LogOut from "./components/user/LogOut.js";
import ExamHistory from "./components/user/ExamHistory.js";
import SetupCams from "./components/user/SetupCams.js";

import ErrorPage from "./components/ErrorPage";
import Root from "./Root";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "",
        element: <MainPage />,
      },
      {
        path: "auth-supervisor",
        element: <AuthSupervisor />,
      },
      {
        path: "auth-staff",
        element: <AuthStaff />,
      },
      {
        path: "supervisor-home",
        element: <SupervisorHome />,
        children: [
          {
            path: "create-exam",
            element: <CreateExam />,
          },
          {
            path: "",
            element: <SetTriggers />,
          },
          {
            path: "exam-history",
            element: <ExamHistory />,
          },
          {
            path: "setup-cams",
            element: <SetupCams />,
          },
          {
            path: "log-out",
            element: <LogOut />,
          },
        ],
      },
      {
        path: "staff-home",
        element: <StaffHome />,
        children: [
          {
            path: "",
            element: <SetupCams />,
          },
          {
            path: "log-out",
            element: <LogOut />,
          },
        ],
      },
    ],
  },
]);

function App() {
  return (
    <React.StrictMode>
      <RouterProvider router={router} />
    </React.StrictMode>
  );
}

export default App;
