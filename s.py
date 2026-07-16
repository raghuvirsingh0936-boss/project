import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import plotly.express as px       
import pandas as pd
df=pd.read_csv("raghu.csv")
df.info()
df1=pd.read_csv("d2.csv")
df.info()
st.set_page_config(page_title="PROJECT", page_icon=":fire:", layout="wide")
st.markdown("""
<style>
/* Remove top padding from the main content */
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
}

/* Remove extra margin from the title */
h1 {
    margin-top: 0rem !important;
    padding-top: 0rem !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
/* Remove Extra Top Space */
.block-container{
    padding-top:0rem;
    padding-bottom:3rem;
    padding-left:2rem;
    padding-right:2rem;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

.stApp{
    background:
    radial-gradient(circle at top right,#1F2937 0%,transparent 35%),
    radial-gradient(circle at bottom left,#1A1F2E 0%,transparent 40%),
    #0D1117;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
[data-testid="stHeadingWithActionElements"] h1{
    color:#FF5A1F  !important;
    font-size:42px;
    font-weight:800;
    letter-spacing:1px;
    text-transform:uppercase;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

[data-testid="stHeadingWithActionElements"] h2,
[data-testid="stHeadingWithActionElements"] h3{
   color:#FB8500 !important;
    font-weight:800;
    letter-spacing:0.5px;
}

</style>
""", unsafe_allow_html=True)

#not 
st.markdown("""
<style>

/* Streamlit Buttons */
.stButton > button {
    background:#1A1A1A;
    color: white;
    border: 2px solid #555555;
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    transition: all 0.3s ease;
}

/* Hover Effect */
.stButton > button:hover {
    background: linear-gradient(135deg, #FF3B30, #DC143C);
    border-color: #555555;
    transform: scale(1.05);
    box-shadow: 0px 0px 15px rgba(220, 20, 60, 0.7);
    color: white;
}

/* Click Effect */
.stButton > button:active {
    transform: scale(0.98);
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Metric Card */
div[data-testid="stMetric"]{
    background-color: #1A1A1A;
    border: 2px solid #555555;
    border-radius: 12px;
    padding: 18px;
    transition: all 0.3s ease;
    cursor: pointer;
}

/* Hover Effect */
div[data-testid="stMetric"]:hover{
    border-color: #D3D3D3;
    background-color: #222222;
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(220,20,60,0.35);
}

/* Metric Label */
div[data-testid="stMetricLabel"]{
    color: #BDBDBD;
    font-weight: 600;
}

/* Metric Value */
div[data-testid="stMetricValue"]{
    color: white;
    font-size: 28px;
    font-weight: bold;
}

/* Metric Delta */
div[data-testid="stMetricDelta"]{
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Slider Track */
.stSlider [data-baseweb="slider"] {
    padding-top: 10px;
    padding-bottom: 10px;
}

/* Slider Rail (Background) */
.stSlider [role="slider"] {
    background-color: #DC143C !important;
    border: 2px solid #555555;
}

/* Slider Label */
.stSlider label {
    color: #E0E0E0 !important;
    font-weight: 600;
}

/* Slider Value */
.stSlider p {
    color: #FFFFFF !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Text Input, Number Input, Text Area */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #1A1A1A;
    color: #FFFFFF;
    border: 2px solid #555555;
    border-radius: 8px;
}

/* Hover */
.stTextInput input:hover,
.stNumberInput input:hover,
.stTextArea textarea:hover {
    border-color: #DC143C;
}

/* Focus */
.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border-color: #DC143C !important;
    box-shadow: 0 0 8px rgba(220,20,60,0.4);
}

/* Selectbox & Multiselect */
.stSelectbox div[data-baseweb="select"],
.stMultiSelect div[data-baseweb="select"] {
    background-color: #1A1A1A;
    border: 2px solid #555555;
    border-radius: 8px;
}

.stSelectbox div[data-baseweb="select"]:hover,
.stMultiSelect div[data-baseweb="select"]:hover {
    border-color: #DC143C;
}

/* Labels */
label {
    color: #E0E0E0 !important;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Tabs Container */
.stTabs [data-baseweb="tab-list"]{
    gap: 12px;
    background-color: #111111;
    padding: 10px;
    border-radius: 10px;
}

/* Individual Tab */
.stTabs [data-baseweb="tab"]{
    background-color: #1A1A1A;
    color: #D3D3D3;
    border: 2px solid #555555;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: 600;
    transition: all 0.3s ease;
}

/* Hover Effect */
.stTabs [data-baseweb="tab"]:hover{
    background-color: #222222;
    border-color: #DC143C;
    color: #FFFFFF;
}

/* Selected Tab */
.stTabs [aria-selected="true"]{
    background-color: #DC143C !important;
    color: white !important;
    border: 2px solid #DC143C !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* DataFrame & Table */
[data-testid="stDataFrame"] {
    border: 2px solid #555555;
    border-radius: 10px;
    overflow: hidden;
}

/* Header */
[data-testid="stDataFrame"] thead tr th {
    background-color: #DC143C !important;
    color: white !important;
    font-weight: bold !important;
    text-align: center !important;
}

/* Table Cells */
[data-testid="stDataFrame"] tbody tr td {
    background-color: #1A1A1A !important;
    color: white !important;
    border-bottom: 1px solid #555555 !important;
}

/* Row Hover */
[data-testid="stDataFrame"] tbody tr:hover td {
    background-color: #2A2A2A !important;
}

/* Table */
table {
    background-color: #1A1A1A !important;
    color: white !important;
    border: 2px solid #555555 !important;
    border-radius: 10px;
}

table th {
    background-color: #DC143C !important;
    color: white !important;
}

table td {
    border: 1px solid #555555 !important;
}

</style>
""", unsafe_allow_html=True)    

with st.sidebar:
    st.markdown("""
<style>

/* ===========================
   SIDEBAR
=========================== */

[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#141922,#0D1117);
    border-right:2px solid rgba(251,133,0,.15);
}

/* Sidebar Title */
[data-testid="stSidebar"] h2{
    color:#FFD700;
    font-weight:800;
    text-align:center;
    letter-spacing:1px;
}

/* ===========================
   OPTION MENU
=========================== */

.nav{
    padding-top:15px;
}

/* Menu Item */

.nav-link{

    font-size:16px !important;

    font-weight:600 !important;

    color:#D8DEE9 !important;

    border-radius:14px !important;

    margin:8px 8px !important;

    padding:14px 18px !important;

    transition:.35s;

    background:rgba(255,255,255,.03);

    border:1px solid rgba(255,255,255,.04);

}

/* Hover */

.nav-link:hover{

    background:rgba(251,133,0,.15) !important;

    color:#FFD700 !important;

    transform:translateX(8px);

    border:1px solid rgba(251,133,0,.35);

}

/* Active */

.nav-pills .nav-link.active{

    background:linear-gradient(
    90deg,
    #FB8500,
    #F97316);

    color:white !important;

    font-weight:700 !important;

    border-radius:14px;

    box-shadow:
    0 6px 20px rgba(251,133,0,.35);

}

/* Icons */

.nav-link i{

    color:#FFB86B !important;

    font-size:19px !important;

    margin-right:12px;

}

.nav-pills .nav-link.active i{

    color:white !important;

}

/* Divider */

hr{

    border:1px solid rgba(255,255,255,.06);

}

</style>
""", unsafe_allow_html=True)
    
    st.markdown("""
    <h2 style='text-align:center;
               color:#FB8500;
               font-weight:800;'>
    🇮🇳 India Tourism Analytics
    </h2>
    """, unsafe_allow_html=True)
    st.markdown("---")
    opt = option_menu(
        menu_title=None,
        options=[
            "Home",
            "Dataset",
            "Visualization",
            "COVID-19 Impact",
            "Search Tourist Place",
            "Insights",
            "About"
        ],
        icons=[
            "house-fill",
            "database-fill",
            "bar-chart-fill",
            "virus",
            "search",
            "lightbulb-fill",
            "info-circle-fill"
        ],
        default_index=0,
    )

if opt=="Home":
    
    st.title("Indian Tourism Trend Analysis")
    st.markdown("<h4 style='text-align:center;color:gray;'>Discover • Analyze • Explore India's Tourism</h4>",unsafe_allow_html=True)
    image_list=['img1.png','img2.png','img3.png','img4.png','img6.png','img11.png','im7.png']
    st.image(image=image_list,width=150)
   
    col1,col2,col3,col4=st.columns(4)
    col1.metric("📍 Tourist Places",len(df))
    col2.metric("🏛 Monuments",len(df1))
    col3.metric("🗺 States",28)
    col4.metric("⭐ Avg Rating",round(df["google_review_rating"].mean(),2))
   
    st.subheader("📖 Project Overview")

    st.info("""
This dashboard provides interactive analysis of Indian tourist places
and historical monuments. It explores visitor trends, ratings,
COVID-19 impact, and key tourism insights using visual analytics.
""")
    
    col1,col2,col3=st.columns(3)
    with col1:          
       st.success("""
📊 Interactive Charts

📈 Trend Analysis

🔍 Search
""")   
    with col2:  
      st.success("""
🏛 Monument Analysis

🗺 Tourist Places

🌍 State Analysis
""")  
    with col3:
      st.success("""
🦠 COVID Impact

🤖  Insights

📂 Dataset Overview
""")
   
    st.subheader("🚀 Explore Dashboard")

    c1,c2,c3=st.columns(3)

    with c1:
      st.button("🦠COVID-19 Impact",use_container_width=True)

    with c2:
      st.button("📈Visualization",use_container_width=True)

    with c3:
      st.button("💡Insights",use_container_width=True)
      
    st.image('im01.png',width=900)
     
    st.subheader("🗂 Dataset Summary")

    col1,col2=st.columns(2)
    
    with col1:
     with st.container(border=True):
      st.write(f"📍 Tourist Places : {len(df)}")
     with st.container(border=True): 
      st.write(" 🗺 States :28")

    with col2:
     with st.container(border=True):   
      st.write(f"🏛 Monuments : {len(df1)}")
     with st.container(border=True): 
      st.write(f"🏙 Cities : {df['city'].nunique()}")
   
elif opt=="Dataset":
    st.title("Dataset")
    t1,t2,t3,t4,t5=st.tabs(["Data","Columns","Summary","Before-Processing","After-Processing"])

    with t1:
        st.title("FIRST DATASET")
        st.dataframe(df)
        
        st.title("SECOND DATASET")
        st.dataframe(df1)
    with t2:
        st.title("FIRST DATASET")
        st.write(df.columns)
        
        st.title("SECOND DATASET")
        st.write(df1.columns)

    with t3:
        st.title("FIRST DATASET")
        st.write(df.describe())
        
        st.title("SECOND DATASET")
        st.write(df1.describe())
    with t4:
        st.title("FIRST DATASET")
        st.write(df.isna().sum())
        
        st.title("SECOND DATASET")
        st.write(df1.isna().sum())

    with t5:
        st.title("FIRST DATASET")
        df.drop(columns=["unnamed:_0","weekly_off"],inplace=True)
        df.dropna(inplace=True)
        df.reset_index(drop=True,inplace=True)
        st.write(df.isna().sum())
        
        st.title("SECOND DATASET")
        df1.dropna(inplace=True)
        df1.reset_index(drop=True,inplace=True)
        st.write(df1.isna().sum())

elif opt=="Visualization":
    st.title("Visualization")
    df.drop(columns=["unnamed:_0","weekly_off"],inplace=True)
    df.dropna(inplace=True)
    df.reset_index(drop=True,inplace=True)
    
    df1.dropna(inplace=True)
    df1.reset_index(drop=True,inplace=True)
        
    t1,t2,t3,t4=st.tabs(["🗺️ State & Zone Analysis","🏛️ Monument Analysis","📈 Trend Analysis","📷 Tourist Facilities"])

    with t1:
        
     st.subheader("🏆 Top Tourist Places")
     
     top_n = st.number_input(
    "Enter number of tourist places:",
    min_value=1,
    max_value=len(df),
    value=10,
    step=1
)

     top_places = df.sort_values(
    "number_of_google_review_in_lakhs",
    ascending=False
).head(top_n)


     fig = px.bar(
    top_places,
    x="number_of_google_review_in_lakhs",
    y="name",
    orientation="h",
    color="number_of_google_review_in_lakhs",
    color_continuous_scale="Viridis",
    text="number_of_google_review_in_lakhs",
    title=f"Top {top_n} Tourist Places by Google Reviews"
)

     fig.update_layout(
    template="plotly_white",
     title_x=0.5,
     height=500,
     xaxis_title="Google Review Count in lakhs",
     yaxis_title="Tourist Place",
     coloraxis_showscale=False,
   yaxis=dict(categoryorder="total ascending")
    )
     fig.update_traces(textposition="outside")

     st.plotly_chart(fig, use_container_width=True) 
        
        
        
     state = df["state"].value_counts().reset_index()
     state.columns = ["State", "Count"]

     fig1 = px.line(
    state,
    x="State",
    y="Count",
    markers=True,
    title="🗺️ Tourist Places by State"
)

     fig1.update_layout(
    template="plotly_white",
    title_x=0.5,
    xaxis_tickangle=-45
)
     st.plotly_chart(fig1, use_container_width=True)
        
     fig0=px.sunburst(df,path=["zone","state","name"],values="google_review_rating",title="🌍 Tourism Hierarchy: Zone → State → Tourist Place")
     st.plotly_chart(fig0) 
      
     
     
    with t2:
     df1= df1[
     ~df1["Name of the Monument "].isin(["Total", "Grand Total"])
     ]
     
     st.subheader("🏛️ Top Monuments: Domestic vs Foreign Visitors")


     top_n = st.slider(
    "Select Number of Monuments",
    min_value=5,
    max_value=20,
    value=10
)

# Top monuments based on domestic visitors
     top = (
    df1.sort_values("Domestic-2019-20", ascending=False)
       .head(top_n)
)

# Convert to long format
     plot_df = top.melt(
    id_vars="Name of the Monument ",
    value_vars=["Domestic-2019-20", "Foreign-2019-20"],
    var_name="Visitor Type",
    value_name="Visitors"
)

     plot_df["Visitor Type"] = plot_df["Visitor Type"].replace({
    "Domestic-2019-20": "Domestic",
    "Foreign-2019-20": "Foreign"
})
     fig = px.bar(
    plot_df,
    x="Name of the Monument ",
    y="Visitors",
    color="Visitor Type",
    barmode="group",
    text="Visitors",
    color_discrete_sequence=["#1E88E5", "#FF6B35"],
    title=f"🏛️ Top {top_n} Monuments: Domestic vs Foreign Visitors (2019–20)"
)

     fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    height=600,
    xaxis_title="Monument",
    yaxis_title="Visitors",
    xaxis_tickangle=-45,
    legend_title="Visitor Type"
)

     fig.update_traces(texttemplate="%{text:,}", textposition="outside")

     st.plotly_chart(fig, use_container_width=True)
     
     comparison = top.melt(
    id_vars="Name of the Monument ",
    value_vars=["Domestic-2019-20","Foreign-2019-20"],
    var_name="Type",
    value_name="Visitors"
)

     fig = px.line(
    comparison,
    x="Name of the Monument ",
    y="Visitors",
    color="Type",
    markers=True,
    title="🏛️ Domestic vs Foreign Visitors"
)
     st.plotly_chart(fig, use_container_width=True)
     
     
     df1["Total Visitors"] = (
    df1["Domestic-2019-20"] +
    df1["Foreign-2019-20"]
)

     top10 = df1.sort_values("Total Visitors", ascending=False).head(10)

     fig = px.pie(
    top10,
    names="Name of the Monument ",
    values="Total Visitors",
    hole=0.4,
    title="🏛️Total Visitors by Top 10 Monuments"
)

     fig.update_layout(
    template="plotly_white",
    title_x=0.5
)

     st.plotly_chart(fig, use_container_width=True)

    with t3:    
        
    
        
        
     st.subheader("📈 Visitor Recovery Analysis")


     df1["Total Visitors (2019-20)"] = (
    df1["Domestic-2019-20"] +
    df1["Foreign-2019-20"]
)

     df1["Total Visitors (2020-21)"] = (
    df1["Domestic-2020-21"] +
    df1["Foreign-2020-21"]
)

     df1["Recovery %"] = (
    df1["Total Visitors (2020-21)"] /
    df1["Total Visitors (2019-20)"] * 100
).round(2)

# Top 10 recovered monuments
     top10 = (
    df1.sort_values("Recovery %", ascending=False)
       .head(10)
)

     fig = px.bar(
    top10,
    x="Recovery %",
    y="Name of the Monument ",
    orientation="h",
    color="Recovery %",
    color_continuous_scale="Greens",
    text="Recovery %",
    title="📈 Top 10 Monuments by Visitor Recovery"
)
     fig.update_layout(template="plotly_white",title_x=0.5,height=600,xaxis_title="Recovery (%)",yaxis_title="Monument",coloraxis_showscale=False,yaxis=dict(categoryorder="total ascending"))
     fig.update_traces(texttemplate="%{text:.1f}%",textposition="outside")
     st.plotly_chart(fig, use_container_width=True)
   
     
     
     comparison = pd.DataFrame({
    "Period": ["2019-20", "2020-21"],
    "Domestic": [
        df1["Domestic-2019-20"].sum(),
        df1["Domestic-2020-21"].sum()
    ],
    "Foreign": [
        df1["Foreign-2019-20"].sum(),
        df1["Foreign-2020-21"].sum()
    ]})
     fig = px.bar(comparison,x="Period",y=["Domestic", "Foreign"],barmode="group",title="📉 Tourism Overview")
     fig.update_layout(template="plotly_white",title_x=0.5)
     st.plotly_chart(fig, use_container_width=True)  
     
     
    with t4:
        dslr_sig = (df.groupby(["significance", "dslr_allowed"]).size().reset_index(name="Count"))
        fig7 = px.bar(dslr_sig,x="significance",y="Count",color="dslr_allowed",barmode="group",text="Count",color_discrete_map={    "Yes": "#2E8B57",    "No": "#E74C3C"},
       title="📷 DSLR Permission by Significance")
        fig7.update_layout(template="plotly_white",title_x=0.5,xaxis_title="Significance",yaxis_title="Number of Tourist Places",height=500)
        st.plotly_chart(fig7, use_container_width=True)  
        
        
        fig8= px.box(df, x="state", y="entrance_fee_in_inr", color="state", title="💰 Entrance Fee Distribution by State")
        fig8.update_layout(template="plotly_white",title_x=0.5,height=600,showlegend=False,xaxis_tickangle=-45)
        st.plotly_chart(fig8, use_container_width=True)

        fig0=px.sunburst(df,path=["significance","type","city"],values="google_review_rating",title="Places Significance And Type")
        st.plotly_chart(fig0) 
      
      
      
elif opt=="COVID-19 Impact":
    st.title("🦠 COVID-19 Impact Analysis")
    df1= df1[
    ~df1["Name of the Monument "].isin(["Total", "Grand Total"]) ]


    domestic_before = df1["Domestic-2019-20"].sum()
    domestic_after = df1["Domestic-2020-21"].sum()
    foreign_before = df1["Foreign-2019-20"].sum()
    foreign_after = df1["Foreign-2020-21"].sum()


    domestic_decline =((domestic_before - domestic_after) / domestic_before) * 100
    foreign_decline = ((foreign_before - foreign_after) / foreign_before) * 100

    total_loss = (domestic_before + foreign_before) - (domestic_after + foreign_after)


    df1["Visitor Loss"] = (
    (df1["Domestic-2019-20"] + df1["Foreign-2019-20"])
    - (df1["Domestic-2020-21"] + df1["Foreign-2020-21"]))

    most_affected = df1.loc[df1["Visitor Loss"].idxmax(), "Name of the Monument "]
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
    
      st.metric(
        "📉 Domestic Decline",
        f"{domestic_decline:.1f}%")

    with col2:
      st.metric(
        "🌍 Foreign Decline",
        f"{foreign_decline:.1f}%")

    with col3:
      st.metric(
        "👥 Total Visitor Loss",
        f"{int(total_loss):,}")

    with col4:
      st.metric(
        "🏛 Most Affected Monument",
        most_affected)
   
    domestic = pd.DataFrame({
    "Period": ["2019-20", "2020-21"],
    "Visitors": [
        df1["Domestic-2019-20"].sum(),
        df1["Domestic-2020-21"].sum()
    ]})

    fig1= px.bar( domestic, x="Period", y="Visitors", color="Period", text="Visitors", color_discrete_sequence=["#2E86DE", "#E74C3C"], title="🦠 COVID-19 Impact on Domestic Visitors")
    fig1.update_layout(template="plotly_white",title_x=0.5,showlegend=False)

    #st.plotly_chart(fig, use_container_width=True)
    foreign = pd.DataFrame({
    "Period": ["2019-20", "2020-21"],
    "Visitors": [
        df1["Foreign-2019-20"].sum(),
        df1["Foreign-2020-21"].sum()
    ]})

    fig2= px.bar(foreign,x="Period",y="Visitors",color="Period",text="Visitors",color_discrete_sequence=["#16A085", "#C0392B"],title="🌍 COVID-19 Impact on Foreign Visitors")
    fig2.update_layout(template="plotly_white",title_x=0.5,showlegend=False)

    #st.plotly_chart(fig, use_container_width=True)
    col1, col2 = st.columns(2, gap="large")

    with col1:
      st.plotly_chart(fig1, use_container_width=True)
      st.divider()
    with col2:
      st.plotly_chart(fig2, use_container_width=True)
      st.divider()
    
    comparison = pd.DataFrame({
    "Period": ["2019-20", "2020-21"],
    "Domestic": [
        df1["Domestic-2019-20"].sum(),
        df1["Domestic-2020-21"].sum()
    ],
    "Foreign": [
        df1["Foreign-2019-20"].sum(),
        df1["Foreign-2020-21"].sum()
    ]})
    fig = px.bar(comparison,x="Period",y=["Domestic", "Foreign"],barmode="group",title="📉 Tourism Before and During COVID-19")
    fig.update_layout(template="plotly_white",title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)  
    
    domestic_drop = (
    (df1["Domestic-2019-20"].sum() - df1["Domestic-2020-21"].sum())
    / df1["Domestic-2019-20"].sum()) * 100

    foreign_drop = (
    (df1["Foreign-2019-20"].sum() - df1["Foreign-2020-21"].sum())
    / df1["Foreign-2019-20"].sum()) * 100

    col1, col2 = st.columns(2)
    col1.metric(
    "Domestic Visitor Decline",
    f"{domestic_drop:.1f}%")
    col2.metric(
    "Foreign Visitor Decline",
    f"{foreign_drop:.1f}%")
  
    df1["Domestic Loss"] = (
    df1["Domestic-2019-20"] - df1["Domestic-2020-21"])
    top_loss = df1.sort_values("Domestic Loss",ascending=False).head(10)
    fig = px.bar(top_loss,x="Domestic Loss",y="Name of the Monument ",orientation="h",color="Domestic Loss",color_continuous_scale="Reds",title="🏛 Top 10 Monuments Most Affected by COVID-19")
    fig.update_layout(template="plotly_white",title_x=0.5,coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)
elif opt=="Search Tourist Place":
    st.header("🔍 Search Tourist Place")

    search_by = st.selectbox(
    "Search By",
    ["State", "City", "Type"]
)

    if search_by == "State":
     option = st.selectbox("Select State", sorted(df["state"].unique()))
     result = df[df["state"] == option]

    elif search_by == "City":
     option = st.selectbox("Select City", sorted(df["city"].unique()))
     result = df[df["city"] == option]

    elif search_by == "Type":
     option = st.selectbox("Select Type", sorted(df["type"].unique()))
     result = df[df["type"] == option]

    st.success(f"Found {len(result)} Tourist Place(s)")    


    for _, row in result.iterrows():

      with st.container(border=True):

        st.subheader(f"📍 {row['name']}")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("⭐ Rating", row["google_review_rating"])
            st.metric("📝 Reviews", f"{int(row['number_of_google_review_in_lakhs']):,}")

        with col2:
            st.metric("💰 Entrance Fee", f"₹ {row['entrance_fee_in_inr']}")
            st.metric("📷 DSLR", row["dslr_allowed"])

        with col3:
            st.metric("🗺 State", row["state"])
            st.metric("🏙 City", row["city"])

        st.markdown("---")

        left, right = st.columns(2)

        with left:
            st.write("### 📋 Details")
            st.write(f"**🏛 Type:** {row['type']}")
            st.write(f"**🌳 Significance:** {row['significance']}")

        with right:
            st.write("### ℹ️ Visitor Information")
            st.write(f"**📅 Best Time:** {row['best_time_to_visit']}")
            st.write(f"**🛫 Nearby Airport:** {row['airport_with_50km_radius']}")

    st.write("")

    st.header("🏛 Search Monument")

    monument = st.selectbox(
    "Select Monument",
    sorted(df1["Name of the Monument "].unique())
)

    result = df1[df1["Name of the Monument "] == monument]

    st.dataframe(result, use_container_width=True)
    row = result.iloc[0]

    col1, col2 = st.columns(2)

    with col1:
     
      st.metric("🗺 Circle", row["Circle"])
     
      st.metric("👥 Domestic Visitors", f"{int(row['Domestic-2019-20']):,}")
     
      st.metric("🌍 Foreign Visitors", f"{int(row['Foreign-2019-20']):,}")

    with col2:
     
      st.metric("🏛 Monument", row["Name of the Monument "])
    
      st.metric("📉 Domestic Growth", f"{row['% Growth 2021-21/2019-20-Domestic']}%")
     
      st.metric("📉 Foreign Growth", f"{row['% Growth 2021-21/2019-20-Foreign']}%")
elif opt=="Insights":  
    st.header("🤖 Tourism Insights")
    df1= df1[
     ~df1["Name of the Monument "].isin(["Total", "Grand Total"])
     ]

    if st.button("✨ Generate Insights", use_container_width=True):

     st.success("Insights generated successfully!")

     st.info(f"🏛 **{df['state'].value_counts().idxmax()}** has the highest number of tourist places.")

     st.info(f"🌍 **{df['zone'].value_counts().idxmax()}** contains the largest number of tourist places.")
 
     st.info(f"⭐ Highest average rating: **{df.groupby('state')['google_review_rating'].mean().idxmax()}**")
 
     st.info(f"💰 Highest average entrance fee: **{df.groupby('state')['entrance_fee_in_inr'].mean().idxmax()}**")

     st.info(f"📷 DSLR Allowed at **{(df['dslr_allowed']=='Yes').mean()*100:.1f}%** of tourist places.")

     st.info(f"🌳 Most common significance: **{df['significance'].mode()[0]}**")

     st.info(f"🏛 Most visited monument: **{df1.loc[df1['Domestic-2019-20'].idxmax(),'Name of the Monument ']}**")

     st.info(f"🦠 Domestic tourism declined by **69.8%** during COVID-19.")

     st.info(f"🌍 Foreign tourism declined by **84.9%** during COVID-19.")

     st.info(f"📉 Most affected monument: **TAJ MAHAL**")    
     
     st.subheader("🔍 Key Findings")
     
    with st.container(border=True):
     st.write(f"🏛 **{df['state'].value_counts().idxmax()}** has the highest number of tourist places.")

    with st.container(border=True):
     st.write(f"🌍 **{df['zone'].value_counts().idxmax()} Zone** contains the largest number of tourist destinations.")

    with st.container(border=True):
     st.write(f"⭐ **{df.groupby('state')['google_review_rating'].mean().idxmax()}** has the highest average tourist rating.")

    with st.container(border=True):
     st.write(f"📷 **{(df['dslr_allowed'].eq('Yes').mean()*100):.1f}%** of tourist places allow DSLR photography.")

    with st.container(border=True):
     st.write(f"💰 **{df.groupby('state')['entrance_fee_in_inr'].mean().idxmax()}** has the highest average entrance fee.")

    with st.container(border=True):
     st.write(f"🌳 **{df['significance'].mode()[0]}** is the most common tourist significance.")

    with st.container(border=True):
     st.write(f"📅 **{df['best_time_to_visit'].mode()[0]}** is the most recommended season for tourists.")

    with st.container(border=True):
     st.write(f"🏛 **{df1.loc[df1['Domestic-2019-20'].idxmax(),'Name of the Monument ']}** recorded the highest domestic visitors in 2019–20.")

    with st.container(border=True):
     st.write(f"🌍 Foreign tourism declined by **84.9%** during the COVID-19 period.")

    with st.container(border=True):
     st.write(f"📉 Domestic tourism declined by **69.8%** during the COVID-19 period.")

    with st.container(border=True):
     st.write(f"⚠️ **TAJ MAHAL** experienced the highest visitor loss during COVID-19.")
 
    with st.container(border=True):
     st.write(f"📍 The dataset covers **28 states**, **214 cities**, and **{len(df):,} tourist places**.")
elif opt=="About":  
    st.title("ℹ️ About the Project")

    st.markdown("---")

    st.header("Indian Tourism Trend Analysis")

    st.write("""
This interactive dashboard provides insights into India's tourism sector by analyzing
tourist destinations, monument visitor statistics, and the impact of COVID-19 on tourism.
The project combines data visualization with analytical insights to help users explore
tourism trends across different states and monuments.
""")
    st.header("🎯 Project Objectives")

    st.markdown("""
- Analyze tourist destinations across India.
- Explore monument visitor statistics.
- Compare domestic and foreign tourism.
- Study the impact of COVID-19 on tourism.
- Provide interactive visualizations and insights.
- Enable quick search of tourist places and monuments.
""")
    st.header("📂 Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
     st.info("""
**Dataset 1: Tourist Places**
- State
- City
- Tourist Place
- Type
- Rating
- Reviews
- Entrance Fee
- Best Time to Visit
- DSLR Permission
""")

    with col2:
     st.info("""
**Dataset 2: Monument Visitors**
- Monument Name
- Circle
- Domestic Visitors
- Foreign Visitors
- Visitor Growth
- COVID-19 Impact
""")
    st.header("✨ Dashboard Features")

    st.markdown("""
✅ Interactive Dashboard

✅ Tourist Place Analysis

✅ Monument Analysis

✅ COVID-19 Impact Analysis

✅ Search Tourist Places

✅ Search Monuments

✅ Analytical Insights

✅ Interactive Charts

✅ KPI Cards
""")
    st.header("🛠 Technologies Used")

    tech1, tech2= st.columns(2)

    with tech1:
     st.success("""
🐍 Python

📊 Pandas

📈 NumPy
""")

    with tech2:
     st.success("""
🌐 Streamlit

📉 Plotly

📊 Matplotlib
""")
   
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📍 Tourist Places", len(df))
    col2.metric("🏛 Monuments", len(df1))
    col3.metric("🗺 States", 28)
    col4.metric("📊 Charts", "15+")

   
