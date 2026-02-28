import statistics


def analyze_numbers(values: list) -> dict:
    """
    Analyze numerical values and return statistical insights.
    """

    # Handle invalid or empty input safely
    if not values or not isinstance(values, list):
        return {
            "count": 0,
            "average": 0,
            "median": 0,
            "min": 0,
            "max": 0,
            "range": 0,
            "volatility_level": "Low",
            "trend_indicator": "Insufficient Data"
        }

    try:
        count = len(values)
        average = statistics.mean(values)
        median = statistics.median(values)
        min_value = min(values)
        max_value = max(values)
        value_range = max_value - min_value

        # Volatility classification
        if value_range < 3:
            volatility = "Low"
        elif 3 <= value_range <= 7:
            volatility = "Moderate"
        else:
            volatility = "High"

        # Trend classification
        if average > 15:
            trend = "Strong Growth"
        elif 8 <= average <= 15:
            trend = "Moderate Growth"
        else:
            trend = "Slow Growth"

        return {
            "count": count,
            "average": round(average, 2),
            "median": round(median, 2),
            "min": round(min_value, 2),
            "max": round(max_value, 2),
            "range": round(value_range, 2),
            "volatility_level": volatility,
            "trend_indicator": trend
        }

    except Exception:
        return {
            "count": 0,
            "average": 0,
            "median": 0,
            "min": 0,
            "max": 0,
            "range": 0,
            "volatility_level": "Low",
            "trend_indicator": "Insufficient Data"
        }