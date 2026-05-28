

import {
  useState
} from "react";

import Navbar from
"../../components/Navbar";

import UploadCard from
"../../components/UploadCard";

import {
  uploadCSV
}
from "../../api/uploadApi";

function Upload() {

  const [category,
    setCategory] =
    useState("sap");

  const [file,
    setFile] =
    useState(null);

  const [message,
    setMessage] =
    useState("");

  const handleUpload =
    async () => {

      if (!file) {

        setMessage(
          "Please select CSV file"
        );

        return;
      }

      try {

        const formData =
          new FormData();

        formData.append(
          "file",
          file
        );

        formData.append(
          "category",
          category
        );

        await uploadCSV(
          formData
        );

        setMessage(
          "CSV uploaded successfully"
        );

      } catch (error) {

        console.log(error);

        setMessage(
          "Upload failed"
        );
      }
    };

  return (

    <div>

      <Navbar />

      <div className=
        "upload-page">

        <UploadCard

          category={
            category
          }

          setCategory={
            setCategory
          }

          setFile={
            setFile
          }

          handleUpload={
            handleUpload
          }

          message={
            message
          }

        />

      </div>

    </div>
  );
}

export default Upload;