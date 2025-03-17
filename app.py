import streamlit as st

st.set_page_config(page_title="Income Percentile | ISU 3", layout="centered")

def income_percentile_calculator():
    st.title("Income Percentile Calculator (Canada/US)")
    st.markdown("[test](https://www.google.com)")
    st.write("Calculates in what percentile you rank in terms of income.")
    
    country = st.selectbox("Country:", ["Canada", "United States"])
    income = st.number_input("Annual Income (in country's currency):", min_value=0.01, format="%.2f")
    
    income_brackets = {
        "Canada": {
            "Top 0.01%": 1_200_000,
            "Top 0.1%": 600_000,
            "Top 0.5%": 400_000,
            "Top 1%": 270_000,
            "Top 2%": 220_000,
            "Top 3%": 190_000,
            "Top 5%": 160_000,
            "Top 7%": 135_000,
            "Top 10%": 110_000,
            "Top 15%": 95_000,
            "Top 20%": 85_000,
            "Top 25%": 81_000,
            "Top 30%": 75_000,
            "Top 40%": 65_000,
            "Top 50%": 50_000,
            "Bottom 50%": 0
        },
        "United States": {
            "Top 0.01%": 2_500_000,
            "Top 0.1%": 1_000_000,
            "Top 0.5%": 700_000,
            "Top 1%": 500_000,
            "Top 2%": 400_000,
            "Top 3%": 320_000,
            "Top 5%": 250_000,
            "Top 7%": 200_000,
            "Top 10%": 160_000,
            "Top 15%": 130_000,
            "Top 20%": 105_000,
            "Top 25%": 90_000,
            "Top 30%": 75_000,
            "Top 40%": 60_000,
            "Top 50%": 45_000,
            "Bottom 50%": 0
        }
    }
    
    percentile = "Below 50%"
    for bracket, threshold in income_brackets[country].items():
        if income >= threshold:
            percentile = bracket
            break
    
    st.success(f"You rank in the {percentile} of earners in {country}.")
    
    st.write(f"\n### Income Percentile in {country}")
    for bracket, threshold in income_brackets[country].items():
        st.write(f"- {bracket}: ${threshold:,}+")
    
    st.write("\n### Sources:")
    st.markdown("- Canada: [Statista - Income Distribution in Canada](https://www.statista.com/statistics/484838/income-distribution-in-canada-by-income-level/)")
    st.markdown("- United States: [DQYDJ - U.S. Income Percentiles](https://dqydj.com/2023-average-median-top-individual-income-percentiles/)")

if __name__ == "__main__":
    income_percentile_calculator()
