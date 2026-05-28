# ESG EmissionFlow

AI-assisted ESG emission ingestion and review workflow system.

## Features

- CSV Upload
- Emission Data Normalization
- Dynamic Review Table
- Approve / Reject Workflow
- Dashboard Statistics
- ESG Emission Tracking

## Tech Stack

### Frontend
- React
- Vite
- Axios

### Backend
- Django
- Django REST Framework
- SQLite

## Workflow

CSV Upload
→ Backend Ingestion
→ Normalization
→ Emission Save
→ Review Workflow
→ Approve / Reject
→ Dashboard Stats

## Supported CSV Format

```csv
source,date,unit,value
sap,2026-05-01,kgco2,120
```

## Run Frontend

```bash
npm install
npm run dev
```

## Run Backend

```bash
python manage.py runserver
```


## API Routes

### Upload CSV

```text
/api/ingestion/upload/
```

### Review Data

```text
/api/review/
```

### Dashboard Stats

```text
/api/review/stats/
```

## Status

Prototype Complete 