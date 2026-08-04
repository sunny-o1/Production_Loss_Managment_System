
import streamlit as st
import plotly.express as px
import pandas as pd
from reports import *



def get_print(rows):
    if not rows:
        st.warning("No Record Found")

    else:
        df = pd.DataFrame(
            rows,
            columns=[
                "ID",
                "Date",
                "Shift",
                "Target",
                "Actual",
                "Reason",
                "Operator"
            ]
        )
        st.dataframe(df, use_container_width=True) 




def get_table(start,end):
    record = table(str(start),str(end))
    if not record:
        st.warning("No Record Found")

    else:
        df2 = pd.DataFrame(record,columns=(
            "Record Id",
            "Date",
            "Shift",
            "Target",
            "Actual",
            "Loss",
            "Efficieny"
        ))

        st.dataframe(df2,use_container_width=True)

    st.divider()






def get_kpi_cards(start,end):
    kpi = kpi_cards(str(start),str(end))
    if not kpi:
        st.warning("No Record Found")

    else:
        pro,tar,loss,eff = kpi
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Production", pro)

        with col2:
            st.metric("Total Target", tar)

        with col3:
            st.metric("Total Loss", loss)

        with col4:
            st.metric("Efficiency", f"{eff}%")

    st.divider()





#bar graph

def get_shift_prod_bar_graph(star,end):
    shift_production = shift_prod(str(star),str(end))
    if not shift_production:
        st.warning("No Record Found")

    else:
        df = pd.DataFrame(shift_production,columns=["Shift","Production"])
        fig = px.bar(
                df,
                x="Shift",
                y="Production",
                title="Shift-wise Production",
                color="Shift",
                text_auto=True
        )

        fig.update_layout(
            xaxis_title="Shift",
            yaxis_title="Production"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()




#bar graph

def get_shift_eff_bar_graph(start,end):
    shift_efficiency = shift_eff(str(start),str(end))
    if not shift_efficiency:
        st.warning("No Record Found")

    else:
        df = pd.DataFrame(shift_efficiency,columns=["Shift","Efficiency"])
        fig = px.bar(
                df,
                x="Shift",
                y="Efficiency",
                title="Shift-Efficieny Graph",
                color="Shift",
                text_auto=True
        )

        fig.update_layout(
            xaxis_title="Shift",
            yaxis_title="Efficiency"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()




def get_pie_chart(start,end):
    shift_production = shift_prod(str(start),str(end))
    if not shift_production:
        st.warning("No Record Found")

    else:
        df = pd.DataFrame(shift_production,columns=["Shift","Production"])
        fig2 = px.pie(
            df,
            names="Shift",
            values="Production",
            title="Production Contribution",
            hole=0.4,
            color="Shift"
        )

        st.plotly_chart(fig2,use_container_width=True)
    st.divider()



#line graph
def get_production_line_graph(start,end):
    data = prod_line(str(start),str(end))
    if not data:
        st.warning("No Record Found")

    else:
        df = pd.DataFrame(data,columns=["Date","Production"])
        fig = px.line(
            df,
            x="Date",
            y="Production",
            title="Day_Wise Production"
        )
        fig.update_traces(
            mode="lines+markers"
        )

        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Loss"
        )
        st.plotly_chart(fig,use_container_width=True)

    st.divider()





