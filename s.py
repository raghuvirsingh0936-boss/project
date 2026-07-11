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
    opt=option_menu("Main Menu", ["Home","Dataset","Processing","Visualization","About"],icons=["house","table","gear","bar-chart","person"],menu_icon="cast",default_index=0)

if opt=="Home":

    st.title("Indian Tourism Trend Analysis")
    image_list=['img1.png','img2.png','img3.png','img4.png',img6.png']
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
        


    t1,t2,t3=st.tabs(["Streamlit","Plotly","Seaborn"])

    with t1:
        state = df["state"].value_counts().reset_index()
        state.columns = ["State", "Count"]

        st.subheader("Tourist Places by State")
        st.bar_chart(state, x="State", y="Count")
        
        type_df = df["type"].value_counts().reset_index()
        type_df.columns = ["Type", "Count"]

        st.subheader("Tourist Places by Type")
        st.bar_chart(type_df, x="Type", y="Count")

        
        zone = df["zone"].value_counts().reset_index()
        zone.columns = ["Zone", "Count"]
        st.subheader("Distribution of Tourist Places by Zone")
        st.bar_chart(zone, x="Zone", y="Count")
        
        
        state = df["state"].value_counts().reset_index()
        state.columns = ["State", "Count"]
        st.subheader("Number of Tourist Places by State")
        st.bar_chart(state, x="State", y="Count")


        df1= df1[
        ~df1["Name of the Monument "].isin(["Total", "Grand Total"])
     ]
        circle = df1.groupby("Circle")["Domestic-2019-20"].sum().reset_index()

        st.subheader("Domestic Visitors by Circle")

        st.area_chart( circle, x="Circle", y="Domestic-2019-20")

        st.subheader("Domestic vs Foreign Tourist Visitors")
        st.scatter_chart(df1,x="Domestic-2019-20",y="Foreign-2019-20")
    with t2:
     df1= df1[
     ~df1["Name of the Monument "].isin(["Total", "Grand Total"])
     ]
     fig = px.scatter(
    df,
    x="google_review_rating",
    y="number_of_google_review_in_lakhs",
    color="zone",
    hover_name="name",
    title="Google Rating vs Number of Reviews"
     )
     st.plotly_chart(fig, use_container_width=True)
     
     top = df.sort_values("google_review_rating", ascending=False).head(10)

     fig = px.bar(
    top,
    x="name",
    y="google_review_rating",
    color="google_review_rating",
    title="Top 10 Highest Rated Tourist Places"
)

     st.plotly_chart(fig, use_container_width=True)
     
     top = df1.sort_values("Domestic-2019-20", ascending=False).head(10)

     fig = px.bar( top,x="Name of the Monument ",y="Domestic-2019-20",color="Domestic-2019-20",title="Top 10 Monuments by Domestic Visitors")

     st.plotly_chart(fig, use_container_width=True)
     
     
     
     circle = df1.groupby("Circle")["Domestic-2019-20"].sum().reset_index()
     fig = px.pie(circle,names="Circle",values="Domestic-2019-20",title="Share of Domestic Visitors")

     st.plotly_chart(fig)
     
     
     top = df1.sort_values("Domestic-2019-20", ascending=False).head(10)

     fig = px.bar(
    top,
    x="Name of the Monument ",
    y=["Domestic-2019-20","Domestic-2020-21"],
    barmode="group",
    title="COVID Impact on Tourism"
      )

     st.plotly_chart(fig)

     fig = px.scatter(
     df1,
    x="Domestic-2019-20",
    y="Foreign-2019-20",
    color="Circle",
    hover_name="Name of the Monument ",
    title="Domestic vs Foreign Visitors"
)
    with t3:
        
     zone = df["zone"].value_counts().reset_index()
     zone.columns = ["Zone", "Count"]

     plt.figure(figsize=(8,5))
     sns.barplot(data=zone, x="Zone", y="Count")

     plt.title("Zone-wise Distribution of Tourist Places")

     st.pyplot(plt)  
        
     plt.figure(figsize=(8,5))

     sns.boxplot(
    data=df,
    x="zone",
    y="google_review_rating"
)

     plt.title("Google Rating Distribution by Zone")

     st.pyplot(plt)  
        
        
        
     plt.figure(figsize=(12,6))

     sns.countplot(
    data=df1,
    x="Circle"
)

     plt.xticks(rotation=90)
     plt.title("Number of Monuments in Each Circle")
     st.pyplot(plt)     
    
     top = df1.sort_values("Domestic-2019-20", ascending=False).head(10)

     plt.figure(figsize=(12,6))

     sns.lineplot(
    data=top,
    x="Name of the Monument ",
    y="Domestic-2019-20",
    markers="o"
)

     plt.xticks(rotation=90)
     plt.title("Top Monuments by Visitors")
     st.pyplot(plt)
