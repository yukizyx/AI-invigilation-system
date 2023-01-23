import { Link } from "react-router-dom";

export default function LogOut() {
  return (
    <div>
      <Link to="../../" className="btn-usertype">
        Log Out
      </Link>
    </div>
  );
}
