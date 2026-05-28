import axios from "axios";

const BASE_URL =
  "http://127.0.0.1:8000/api/accounts/";

export const loginUser =
  async (userData) => {

    const response =
      await axios.post(
        `${BASE_URL}login/`,
        userData
      );

    return response.data;
  };