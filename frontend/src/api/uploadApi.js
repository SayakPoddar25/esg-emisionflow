import axios from "axios";

const BASE_URL =
  "http://127.0.0.1:8000/api/ingestion/";

export const uploadCSV =
  async (formData) => {

    const response =
      await axios.post(
        `${BASE_URL}upload/`,
        formData,
        {
          headers: {
            "Content-Type":
              "multipart/form-data",
          },
        }
      );

    return response.data;
  };