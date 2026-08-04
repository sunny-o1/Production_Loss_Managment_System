import streamlit as st
from datetime import date
from config import *
from database import *
from analysis import *
from reports import *
import pandas as pd
import plotly.express as px
import plotly
from utils import *



col1,col2 = st.columns([1,3])
with col1:
    st.image("https://www.hindalco.com/Upload/Images/thumbnail/hindalco-logo-thumbnail.jpg")

with col2:
    st.write("")
    st.write("")
    st.header("HINDALCO INDUSTRIES LIMITED")

st.title("Production Loss Dashboard")

st.divider()




# Navigataion page

st.sidebar.title("Navigation")

page = st.sidebar.radio("",
    [
        "🏠 Home",
        "➕ Add Record",
        "📋 View Records",
        "🔎 Search Records",
        "📊 Analysis",
        "📄 Reports"
    ]
)



# Home page content

if page == "🏠 Home":
    st.subheader("🏭 Welcome to the Production Loss Dashboard")
    st.header("Dashboard Overview")
    create_table()

    col1,col2,col3 = st.columns(3)

    today=date.today()
    rows = search_by_date(str(today))
    total_pro = total_tar = total_eff =0;
    if not rows:
        pass
    else:
        for row in rows:
            total_pro += row[4]
            total_tar += row[3]

    total_eff = total_pro/total_tar * 100


    with col1:
        st.metric("Today's Production", total_pro)

    with col2:
        st.metric("Target", total_tar)

    with col3:
        st.metric("Efficiency", f"{total_eff:.2f}%")

    st.divider()

    st.subheader("Quick Information")

    

    st.success("System Running Successfully")

    st.info("Choose a page from the sidebar.")






# Add Record page content

elif page == "➕ Add Record":
    st.header("➕  Add Production Record")

    date = st.date_input("Production Date ")
    shift = st.selectbox("Shift :",SHIFTS)
    target = TARGET_PRODUCTION[shift]
    actual = st.number_input("Actual Production :",min_value=0)
    reason = st.selectbox("DownTime Reason :",DOWNTIME_REASONS)
    operator = st.text_input("Operator Name")
    if st.button("Save Record"):
        add_record(
            str(date),shift,target,actual,reason,operator
        )
        st.success("Record Saved Successfully!")








# View Record Page Content

elif page == "📋 View Records":
    st.header("📋 View Production Records")

    if st.button("View"):
        rows = view_all_records()
        get_print(rows)

    st.write("Database records will appear here.")








# Search Menu Page


elif page == "🔎 Search Records":
    st.title("🔎 Search Records")

    menu = ["None","Date","Shift","Operator"]

    src = st.selectbox("Select the Search option ",menu)

    if src == menu[0]:
        pass

    if src == menu[1]:
        st.header("Search By Date")
        date =st.date_input("Enter the Date ")
        rows = search_by_date(str(date))
        get_print(rows)
            

    if src == menu[2]:
        st.header("Search By Shift")
        shift = st.selectbox("Shift :",SHIFTS)
        rows = search_by_shift(shift)
        get_print(rows)


    if src == menu[3]:
            st.header("Search By Operator")
            opt = st.text_input("Enter the Operator Name")
            rows = search_by_operator(opt)
            get_print(rows)

    
    

    

# Analysis Record page 

elif page == "📊 Analysis":

    st.title("📊 Production Analysis")


    if st.button("Overall Analysis "):
        st.header("Overall Analysis")
        count,target,actual = overall_production_analysis()
        if(count == 0):
            st.warning("NO Record Found")
        else:
            loss = target - actual
            efficiency = actual / target * 100

            col1,col2 = st.columns(2)

            with col1:
                st.metric("Total Records", count)
                st.metric("Target Production", target)
                st.metric("Actual Production", actual)

            with col2:
                st.metric("Total Loss", loss)
                st.metric("Efficiency", f"{efficiency:.2f}%")


    
    if st.button("shift-wise Analysis "):
        st.header("Shift-Wise Analysis")

        rows = shift_wise_analysis()

        col1,col2,col3= st.columns(3)

        columns = {
            "A":col1 , "B":col2 , "C":col3
        }
        
        for shift,count,target,actual in rows:
            with columns[shift]:
                st.subheader(f"Shift {shift}")
                if count == 0:
                    st.warning("No records found.")
                    continue    

                loss = target - actual
                efficiency = actual / target * 100
                
                st.metric("Total Records", count)
                st.metric("Target Production", target)
                st.metric("Actual Production", actual)

                st.metric("Total Loss", loss)
                st.metric("Efficiency", f"{efficiency:.2f}%")




    if st.button("DownTime Analysis"):
        st.header("DownTime Analysis")

        rows = downtime_analysis()
        if not rows:
            st.warning("NO Record Found")
        else:
            for reason , count in rows:
                st.metric(reason,count)


    st.write("Charts and analysis will appear here.")







# Reports Page

elif page == "📄 Reports":

    st.title("📄 Reports")

    menu=["None","Daily Report","Weekly Report","Monthly Report"]
    src = st.selectbox("Choose Report Time ",menu)

    if src==menu[1]:
        st.header("Daily Reports")
        today = st.date_input("Enter the date")
        st.divider()

        get_kpi_cards(today,today)
        get_shift_prod_bar_graph(today,today)
        get_shift_eff_bar_graph(today,today)
        get_pie_chart(today,today)
        get_table(today,today)



    elif src==menu[2]:
        st.header("Weekly Reports")
        start = st.date_input("Enter the date")
        end = start + timedelta(days=6)
        st.divider()

        get_kpi_cards(start,end)
        get_shift_prod_bar_graph(start,end)
        get_shift_eff_bar_graph(start,end)
        get_pie_chart(start,end)
        get_production_line_graph(start,end)
        get_table(start,end)

    elif src == menu[3]:
        import calendar
        st.header("Monthly Reports")
        col1,col2 = st.columns(2)
        with col1:
            month = st.selectbox("Month ",range(1,13),format_func=lambda x: calendar.month_name[x])

        with col2:
            year = st.number_input(
                "Year",
                min_value=2020,
                max_value=2035,
                value=2026
            )

        start = date(year, month, 1)

        last_day = calendar.monthrange(year, month)[1]
        end = date(year, month, last_day)

        st.divider()

        get_kpi_cards(start,end)
        get_shift_prod_bar_graph(start,end)
        get_shift_eff_bar_graph(start,end)
        get_pie_chart(start,end)
        get_production_line_graph(start,end)
        get_table(start,end)
        

    st.write("Daily, Weekly and Monthly Reports.")