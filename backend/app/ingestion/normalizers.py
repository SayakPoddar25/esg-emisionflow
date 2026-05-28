from datetime import datetime


def normalize_row(row):

    raw_date = str(
        row.get(
            "date",
            ""
        )
    ).strip()

    try:

        parsed_date = datetime.strptime(
            raw_date,
            "%Y-%m-%d"
        ).date()

    except:

        parsed_date = None

    normalized = {

        "source":
        str(
            row.get(
                "source",
                ""
            )
        ).strip().lower(),

        "unit":
        str(
            row.get(
                "unit",
                ""
            )
        ).strip().lower(),

        "value":
        float(
            row.get(
                "value",
                0
            )
        ),

        "date":
        parsed_date
    }

    return normalized