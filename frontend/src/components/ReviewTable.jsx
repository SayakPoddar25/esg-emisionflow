import "./ReviewTable.css";

import {
  useEffect,
  useState
}
from "react";

import {
  getReviews,
  approveReject
}
from "../api/reviewApi";

function ReviewTable() {

  const [reviews,
    setReviews] =
    useState([]);

  useEffect(() => {
    fetchReviews();
  }, []);

  const fetchReviews =
    async () => {

      try {

        const data =
          await getReviews();

        setReviews(data);

      } catch (error) {

        console.log(error);
      }
    };

  const handleAction =
    async (
      id,
      action
    ) => {

      try {

        await approveReject(
          id,
          action
        );

        fetchReviews();

      } catch (error) {

        console.log(error);
      }
    };

  return (

    <div className=
      "table-wrapper">

      <table>

        <thead>
          <tr>

            <th>ID</th>
            <th>Source</th>
            <th>Value</th>
            <th>Unit</th>
            <th>Status</th>
            <th>Action</th>

          </tr>
        </thead>

        <tbody>

          {reviews.map(
            (item) => (

            <tr key=
              {item.id}>

              <td>
                {item.id}
              </td>

              <td>
                {item.source}
              </td>

              <td>
                {item.value}
              </td>

              <td>
                {item.unit}
              </td>

              <td>
                {item.status}
              </td>

              <td>

                <button
                  className=
                  "approve-btn"

                  onClick={() =>
                    handleAction(
                      item.id,
                      "approved"
                    )
                  }
                >
                  Approve
                </button>

                <button
                  className=
                  "reject-btn"

                  onClick={() =>
                    handleAction(
                      item.id,
                      "rejected"
                    )
                  }
                >
                  Reject
                </button>

              </td>

            </tr>
          ))}

        </tbody>

      </table>

    </div>
  );
}

export default
ReviewTable;