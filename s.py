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
st.set_page_config(page_title="apna kmm ", page_icon="in", layout="wide")

with st.sidebar:
    opt=option_menu("Main Menu", ["Home","Dataset","Processing","Visualization","🦠 COVID-19 Impact","🔍 Search Tourist Place","About"],icons=["house","table","gear","bar-chart","🦠", "🔍","person"],menu_icon="cast",default_index=0)

if opt=="Home":

    st.title("Indian Tourism Trend Analysis")
    image_list=['img1.png','img2.png','img3.png','img4.png','img6.png']
    st.image(image=image_list,width=100)
    st.markdown("""
                ### Explore Tourism Trends Accross India
                This dashboard provides insights into tourism patterns using interactive visualizations and data analysis.

                #### Features:
                - 📈 Tourist arrival trends
                - 🗺️ State-wise tourism analysis
                - 🌍 Domestic vs Foreign tourists
                - 📊 Interactive charts
                - 📅 Year-wise comparisons
                 """) 
            
    st.image("im.jpg",use_container_width=True)
    st.header("About the Project")
    st.write("""
                 The Indian Tourism Trend Analysis Dashboard helps users understand
                 tourism growth, visitor statistics, and regional trends using data visualization.
                 """)

    col1, col2, col3 = st.columns(3)

    with col1:
     st.metric("States Covered", "33")

    with col2:
     st.metric("Years of Data", "2019-2021")

    with col3:
     st.metric("Tourism Categories", "Domestic & Foreign")

    st.info("👈 Use the sidebar to navigate through different analyses.")

elif opt=="Dataset":
    st.title("Dataset")
    t1,t2,t3=st.tabs(["Data","Columns","Summary"])

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
elif opt=="Processing":
    st.title("Processing")
    t1,t2=st.tabs(["Before-Processing","After-Processing"])

    with t1:
        st.title("FIRST DATASET")
        st.write(df.isna().sum())
        
        st.title("SECOND DATASET")
        st.write(df1.isna().sum())

    with t2:
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
        


    t1,t2,=st.tabs(["Tourism","Monuments",])

    with t1:
            
     state = df["state"].value_counts().reset_index()
     state.columns = ["State", "Count"]
     fig1= px.bar( state, x="State", y="Count", color="Count", title="Tourist Places by State", text_auto=True)
     #st.plotly_chart(fig1, use_container_width=True) 
            
     zone = df["zone"].value_counts().reset_index()
     zone.columns = ["Zone", "Count"]
     fig2= px.bar(zone,x="Zone",y="Count",color="Count",title="Tourist Places by Zone",text_auto=True)
     #st.plotly_chart(fig2, use_container_width=True)    
   
     types = df["type"].value_counts().reset_index()
     types.columns = ["Type", "Count"]
     fig3= px.pie(types, names="Type",values="Count",hole=0.5,title="Tourist Place Categories")
     #st.plotly_chart(fig, use_container_width=True)
      
     rating = df.groupby("state")["google_review_rating"].mean().reset_index()
     fig6= px.bar(rating,x="state",y="google_review_rating",color="google_review_rating",title="Average Rating by State")
     #st.plotly_chart(fig, use_container_width=True)
      
     sig = df["significance"].value_counts().reset_index()
     sig.columns = ["Significance", "Count"]

     fig4 = px.bar(sig,x="Significance",y="Count",color="Count",title="Tourist Place Significance")
     #st.plotly_chart(fig4, use_container_width=True) 
     
     
     best = df["best_time_to_visit"].value_counts().reset_index()
     best.columns = ["Season", "Count"]
     fig5= px.bar(best,x="Season",y="Count",color="Count",title="Best Time to Visit")
     #st.plotly_chart(fig, use_container_width=True)
     
     dslr_sig = (
     df.groupby(["significance", "dslr_allowed"])
      .size()
      .reset_index(name="Count")
)

     fig7 = px.bar(dslr_sig,x="significance",y="Count",color="dslr_allowed",barmode="group",text="Count",color_discrete_map={    "Yes": "#2E8B57",    "No": "#E74C3C"
    },
    title="📷 DSLR Permission by Significance"
)

     fig7.update_layout(template="plotly_white",title_x=0.5,xaxis_title="Significance",yaxis_title="Number of Tourist Places",height=500)

    # st.plotly_chart(fig, use_container_width=True)
     
     
     fig8= px.box(df, x="state", y="entrance_fee_in_inr", color="state", title="💰 Entrance Fee Distribution by State")
     fig8.update_layout(template="plotly_white",title_x=0.5,height=600,showlegend=False,xaxis_tickangle=-45)
    #st.plotly_chart(fig, use_container_width=True)
    
     col1, col2 = st.columns(2, gap="large")

     with col1:
      st.plotly_chart(fig1, use_container_width=True)
      st.divider()
     with col2:
      st.plotly_chart(fig2, use_container_width=True)
      st.divider()
     col3, col4 = st.columns(2, gap="large")

     with col3:
      st.plotly_chart(fig3, use_container_width=True)
      st.divider()
     with col4:
      st.plotly_chart(fig4, use_container_width=True)
      st.divider() 
     col5, col6 = st.columns(2, gap="large")  
     with col5:
      st.plotly_chart(fig5, use_container_width=True)
      st.divider()
     with col6:
      st.plotly_chart(fig6, use_container_width=True)
      st.divider()
     col7, col8 = st.columns(2, gap="large")
     with col7:
      st.plotly_chart(fig7, use_container_width=True)
      st.divider()
     with col8:
      st.plotly_chart(fig8, use_container_width=True)
      st.divider() 
      
    with t2:
     df1= df1[
     ~df1["Name of the Monument "].isin(["Total", "Grand Total"])
     ]
     top = df1.sort_values("Domestic-2019-20", ascending=False).head(10)

     fig1= px.bar( top,x="Domestic-2019-20",y="Name of the Monument ",orientation="h",color="Domestic-2019-20",color_continuous_scale="Turbo",text="Domestic-2019-20",title="🏛 Top 10 Monuments by Domestic Visitors")
     fig1.update_layout(template="plotly_white",title_x=0.5,height=600,coloraxis_showscale=False)


    # st.plotly_chart(fig1, use_container_width=True)

     top = df1.sort_values("Foreign-2019-20", ascending=False).head(10)

     fig2= px.bar(top,x="Foreign-2019-20",y="Name of the Monument ",orientation="h",color="Foreign-2019-20",color_continuous_scale="Viridis",text="Foreign-2019-20",title="🌍 Top 10 Monuments by Foreign Visitors")
     
     fig2.update_layout(template="plotly_white",title_x=0.5,height=600,coloraxis_showscale=False)
#st.plotly_chart(fig, use_container_width=True)

     col11, col22 = st.columns(2, gap="large")

     with col11:
      st.plotly_chart(fig1, use_container_width=True)
      st.divider()
     with col22:
      st.plotly_chart(fig2, use_container_width=True)
      st.divider()

     fig3= px.scatter(df1,x="Domestic-2019-20", y="Foreign-2019-20", color="Circle", hover_name="Name of the Monument ", size="Domestic-2019-20", title="📈 Domestic vs Foreign Visitors")
     #st.plotly_chart(fig, use_container_width=True)

     circle = df1["Circle"].value_counts().reset_index()
     circle.columns = ["Circle", "Count"]
     fig4= px.pie(circle,names="Circle",values="Count",hole=0.55,title="🗺 Monuments by Circle")

     #st.plotly_chart(fig, use_container_width=True)

     col12, col23 = st.columns(2, gap="large")

     with col12:
      st.plotly_chart(fig3, use_container_width=True)
      st.divider()
     with col23:
      st.plotly_chart(fig4, use_container_width=True)
      st.divider()
      
     top = df1.sort_values("% Growth 2021-21/2019-20-Domestic", ascending=False)
     fig5= px.bar(top,x="Name of the Monument ",y="% Growth 2021-21/2019-20-Domestic",color="% Growth 2021-21/2019-20-Domestic",color_continuous_scale="Plasma",title="📈 Domestic Visitor Growth")
     fig5.update_layout(xaxis_tickangle=-45)
     #st.plotly_chart(fig, use_container_width=True)
     
     fig6= px.bar(df1, x="Name of the Monument ", y="% Growth 2021-21/2019-20-Foreign", color="% Growth 2021-21/2019-20-Foreign", color_continuous_scale="Inferno", title="🌍 Foreign Visitor Growth")
     fig6.update_layout(xaxis_tickangle=-45)
     #st.plotly_chart(fig, use_container_width=True)
     col22, col33 = st.columns(2, gap="large")

     with col22:
      st.plotly_chart(fig5, use_container_width=True)
      st.divider()
     with col33:
      st.plotly_chart(fig6, use_container_width=True)
      st.divider()
    
     fig7= px.bar(df1.head(10),x="Name of the Monument ",y=["Domestic-2019-20", "Foreign-2019-20"],barmode="group",title="👥 Domestic vs Foreign Visitors")
     fig7.update_layout( xaxis_tickangle=-45,template="plotly_white")
     #st.plotly_chart(fig, use_container_width=True)

     corr = df1[
    [
        "Domestic-2019-20",
        "Foreign-2019-20",
        "Domestic-2020-21",
        "Foreign-2020-21"
    ]
    ].corr()
     fig8, ax = plt.subplots(figsize=(8,6))
     sns.heatmap(corr, annot=True, cmap="YlGnBu", ax=ax)

     
     col5, col6 = st.columns(2, gap="large")

     with col5:
      st.plotly_chart(fig7, use_container_width=True)
      st.divider()
     with col6:
      st.pyplot(fig8)
      st.divider()
elif opt=="🦠 COVID-19 Impact":
    st.title("🦠 COVID-19 Impact Analysis")
    df1= df1[
    ~df1["Name of the Monument "].isin(["Total", "Grand Total"])
     ]


# Total visitors
    domestic_before = df1["Domestic-2019-20"].sum()
    domestic_after = df1["Domestic-2020-21"].sum()
    foreign_before = df1["Foreign-2019-20"].sum()
    foreign_after = df1["Foreign-2020-21"].sum()
# Percentage decline
    domestic_decline = ((domestic_before - domestic_after) / domestic_before) * 100
    foreign_decline = ((foreign_before - foreign_after) / foreign_before) * 100
# Total visitor loss
    total_loss = (domestic_before + foreign_before) - (domestic_after + foreign_after)

# Most affected monument
    df1["Visitor Loss"] = (
    (df1["Domestic-2019-20"] + df1["Foreign-2019-20"])
    - (df1["Domestic-2020-21"] + df1["Foreign-2020-21"]))

    most_affected = df1.loc[df1["Visitor Loss"].idxmax(), "Name of the Monument "]

# KPI Cards
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
elif opt=="🔍 Search Tourist Place":
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
