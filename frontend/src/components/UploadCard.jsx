import "./UploadCard.css";

function UploadCard({
  category,
  setCategory,
  setFile,
  handleUpload,
  message
}) {

  return (
    <div className="upload-card">

      <h2>
        Upload CSV
      </h2>

      <select
        value={category}
        onChange={(e)=>
          setCategory(
            e.target.value
          )
        }
      >
        <option value="sap">
          SAP
        </option>

        <option value="utility">
          Utility
        </option>

        <option value="travel">
          Travel
        </option>
      </select>

      <input
        type="file"
        accept=".csv"
        onChange={(e)=>
          setFile(
            e.target.files[0]
          )
        }
      />

      <button
        className="upload-btn"
        onClick={
          handleUpload
        }
      >
        Upload CSV
      </button>

      <br />
      <br />

      <p>
        {message}
      </p>

    </div>
  );
}

export default UploadCard;