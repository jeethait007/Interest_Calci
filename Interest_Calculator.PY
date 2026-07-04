import streamlit as st
import pandas as pd

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Simple Interest Calculator",
    page_icon="💰",
    layout="centered"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#F4F8FB;
}

.title{
    text-align:center;
    color:#0E4C92;
    font-size:42px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

.result-box{
    padding:20px;
    border-radius:15px;
    background:#E8F4FD;
    border:1px solid #C5E3F6;
}

.stButton>button{
    width:100%;
    height:55px;
    font-size:20px;
    border-radius:12px;
    background:#0E4C92;
    color:white;
    font-weight:bold;
}

.stMetric{
    background-color:#ffffff;
    padding:15px;
    border-radius:12px;
    border:1px solid #ECECEC;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    "<div class='title'>💰 Simple Interest Calculator</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Calculate your investment growth instantly</div>",
    unsafe_allow_html=True
)

# -----------------------------
# INPUT SECTION
# -----------------------------
st.subheader("📥 Investment Details")

col1, col2 = st.columns(2)

with col1:

    principal = st.number_input(
        "Principal Amount (₹)",
        min_value=0.0,
        value=100000.0,
        step=1000.0
    )

    rate = st.number_input(
        "Interest Rate (%)",
        min_value=0.0,
        value=7.5,
        step=0.1
    )

with col2:

    years = st.number_input(
        "Years",
        min_value=0,
        value=5
    )

    months = st.number_input(
        "Months",
        min_value=0,
        max_value=11,
        value=0
    )

st.write("")

# -----------------------------
# BUTTON
# -----------------------------
if st.button("📊 Calculate Interest"):

    time = years + months/12

    interest = (principal * rate * time)/100

    maturity = principal + interest

    st.success("Calculation Completed Successfully!")

    st.divider()

    # Metrics

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "💰 Interest Earned",
            f"₹ {interest:,.2f}"
        )

    with c2:
        st.metric(
            "🏦 Maturity Amount",
            f"₹ {maturity:,.2f}"
        )

    st.divider()

    # Pie Chart

    st.subheader("📈 Investment Distribution")

    chart_data = pd.DataFrame(
        {
            "Category":["Principal","Interest"],
            "Amount":[principal,interest]
        }
    )

    st.pyplot(
        chart_data.plot.pie(
            y="Amount",
            labels=chart_data["Category"],
            autopct="%1.1f%%",
            figsize=(5,5),
            legend=False
        ).get_figure()
    )

    st.divider()

    # Summary

    st.subheader("📋 Investment Summary")

    st.info(f"""
**Principal Amount:** ₹ {principal:,.2f}

**Interest Rate:** {rate:.2f}% per annum

**Investment Duration:** {years} Year(s) {months} Month(s)

**Simple Interest:** ₹ {interest:,.2f}

**Maturity Amount:** ₹ {maturity:,.2f}
""")

    # Formula

    with st.expander("🧮 Show Formula"):

        st.latex(r"Simple\ Interest=\frac{Principal \times Rate \times Time}{100}")

        st.write(f"""
Principal = ₹ {principal:,.2f}

Rate = {rate:.2f}%

Time = {time:.2f} Years

Interest = ₹ {interest:,.2f}
""")

    # Download

    result = pd.DataFrame({

        "Principal":[principal],
        "Rate (%)":[rate],
        "Years":[years],
        "Months":[months],
        "Interest":[interest],
        "Maturity Amount":[maturity]

    })

    csv = result.to_csv(index=False)

    st.download_button(
        "📥 Download Result (CSV)",
        csv,
        file_name="Simple_Interest_Result.csv",
        mime="text/csv"
    )

st.divider()

st.caption("Made with ❤️ using Streamlit")