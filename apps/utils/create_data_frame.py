import pandas as pd


def create_data_frame(data):
    df_data = pd.DataFrame(data["status"])
    df_data.columns = [
        "name_id",
        "geographic_name",
        "geometry",
        "site_type",
        "date_mod",
        "dictionary",
        "geo_database",
        "google_maps",
        "open_street_maps",
        "aerial_photograph",
        "cartographic_sheet",
        "longitude",
        "latitude",
    ]

    df_data = df_data[
        [
            "name_id",
            "geographic_name",
            "dictionary",
            "geo_database",
            "google_maps",
            "open_street_maps",
            "aerial_photograph",
            "cartographic_sheet",
            "longitude",
            "latitude",
        ]
    ]

    sources = [
        "dictionary",
        "geo_database",
        "google_maps",
        "open_street_maps",
        "aerial_photograph",
        "cartographic_sheet",
    ]

    for source in sources:
        df_data[source] = df_data[source].apply(lambda x: "✔️" if x == "true" else "❌")

    return df_data


def get_map_data(data):
    data = data[
        [
            "name_id",
            "geographic_name",
            "longitude",
            "latitude",
        ]
    ]
    dicts = data.to_dict("records")

    return dicts
