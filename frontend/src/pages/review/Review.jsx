import "./Review.css";

import Navbar from
"../../components/Navbar";

import ReviewTable from
"../../components/ReviewTable";

function Review() {
  return (
    <div>

      <Navbar />

      <div className="review-page">

        <h1>
          Analyst Review
        </h1>

        <ReviewTable />

      </div>

    </div>
  );
}

export default Review;