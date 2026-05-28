import "./Dashboard.css";
import Navbar from
"../../components/Navbar";

import {
  useEffect,
  useState
}
from "react";

import {
  getDashboardStats
}
from "../../api/reviewApi";

function Dashboard() {

  const [stats,
    setStats] =
    useState({

      fuel: 0,
      utility: 0,
      travel: 0,
      pending: 0,
      approved: 0,
      rejected: 0
    });

  useEffect(() => {

    fetchStats();

  }, []);

  const fetchStats =
    async () => {

      try {

        const data =
          await
          getDashboardStats();

        setStats(data);

      } catch (error) {

        console.log(error);
      }
    };

  return (

    <div>

      <Navbar />

      <div className=
        "dashboard">

        <div className=
          "card">
          <div>
            <h2>
              Fuel Data
            </h2>

            <h1>
              {stats.fuel}
            </h1>
          </div>
        </div>

        <div className=
          "card">
          <div>
            <h2>
              Utility Data
            </h2>

            <h1>
              {stats.utility}
            </h1>
          </div>
        </div>

        <div className=
          "card">
          <div>
            <h2>
              Travel Data
            </h2>

            <h1>
              {stats.travel}
            </h1>
          </div>
        </div>

        <div className=
          "card">
          <div>
            <h2>
              Pending
            </h2>

            <h1>
              {stats.pending}
            </h1>
          </div>
        </div>

        <div className=
          "card">
          <div>
            <h2>
              Approved
            </h2>

            <h1>
              {stats.approved}
            </h1>
          </div>
        </div>

        <div className=
          "card">
          <div>
            <h2>
              Rejected
            </h2>

            <h1>
              {stats.rejected}
            </h1>
          </div>
        </div>

      </div>

    </div>
  );
}

export default Dashboard;