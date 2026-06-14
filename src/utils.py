def sort_breweries(breweries):
    """
    Sort breweries by name in ascending order.
    """

    return sorted(
        breweries,
        key=lambda brewery:
            brewery.get("name", "").lower()
    )


def filter_breweries(
    breweries,
    country="",
    brewery_type=""
):
    """
    Filter breweries based on country
    and brewery type.
    """

    if country:

        breweries = filter(
            lambda brewery:
            brewery.get("country", "").lower()
            == country.lower(),

            breweries
        )

    if brewery_type:

        breweries = filter(
            lambda brewery:
            brewery.get("brewery_type", "").lower()
            == brewery_type.lower(),

            breweries
        )

    return list(breweries)