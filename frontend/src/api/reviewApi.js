import axios from "axios";

const BASE_URL =
  "http://127.0.0.1:8000/api/review/";

export const getReviews =
  async () => {

    const response =
      await axios.get(
        BASE_URL
      );

    return response.data;
  };


export const approveReject =
  async (
    emissionId,
    action
  ) => {

    const response =
      await axios.post(

        `${BASE_URL}${emissionId}/`,

        {
          action
        }
      );

    return response.data;
  };


export const getDashboardStats =
  async () => {

    const response =
      await axios.get(
        `${BASE_URL}stats/`
      );

    return response.data;
  };