# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.set_page_config(
        page_title="Labor Count",
    )

    st.write("# Predict Labor Count")
    
    df=pd.read_csv("predicted_values_df.csv")

    laborForm = st.form('laborForm')

    store_name = laborForm.selectbox('Select store:', df['Store Name'].unique())
        
    day_name = laborForm.selectbox('Enter the day', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    dept = laborForm.selectbox('Enter department', ['Employee', 'Supervisor', 'Manager'])
    
    age_group = laborForm.selectbox('Enter the combination of gender and age group', ['Female (23-50)', 'Female (50-65)', 'Male (23-50)', 'Male (50-65)'])
    
    shift_time = laborForm.selectbox('Enter the shift', ['Morning Shift (10 AM - 12 PM)', 'Afternoon Shift (12 PM - 3 PM)', 'Evening Shift (3 PM - 6 PM)'])
    
    submit = laborForm.form_submit_button(f'Predict')
    
    if submit:
        #Department
        if dept=="Employee":
            dept=0
        elif dept=="Manager":
            dept=1
        elif dept=="Supervisor":
            dept=2
        
        #customer_time
        if shift_time=="Afternoon Shift (12 PM - 3 PM)":
            shift_time=0
        elif shift_time=="Evening Shift (3 PM - 6 PM)":
            shift_time=1
        elif shift_time=="Morning Shift (10 AM - 12 PM)":
            shift_time=2
        
        #Age_Group
        if age_group=="Female (23-50)":
            age_group=0
        elif age_group=="Female (50-65)":
            age_group=1
        elif age_group=="Male (23-50)":
            age_group=2
        elif age_group=="Male (50-65)":
            age_group=3
        
        #Day_Name
        if day_name=="Friday":
            day_name=0
        elif day_name=="Monday":
            day_name=1
        elif day_name=="Saturday":
            day_name=2
        elif day_name=="Sunday":
            day_name=3
        elif day_name=="Thursday":
            day_name=4
        elif day_name=="Tuesday":
            day_name=5
        elif day_name=="Wednesday":
            day_name=6
    
        filtered_table=df.loc[(df['Store Name']==store_name) & (df['Day_Name']==day_name)& (df['Department']==dept)& (df['Age_Group']==age_group)& (df['customer_time']==shift_time)]
    
        # actual=[]
        # predicted=[]
        # for ind,col in filtered_table.iterrows():
        #     actual.append(filtered_table['Count of employees across each condition'])
        #     predicted.append(filtered_table['Predicted Values'])
        
        # sns.barplot(x=['Actual', 'Predicted'], y=[actual, predicted])
        actual = filtered_table['Count of employees across each condition'].tolist()
        predicted = filtered_table['Predicted Values'].tolist()

        data = {'Category': ['Actual'] * len(actual) + ['Predicted'] * len(predicted),
        'Value': actual + predicted}

        df_plot = pd.DataFrame(data)

        
        plt.figure(figsize=(10, 6))
        sns.barplot(data=df_plot, x='Category', y='Value')
        plt.legend()
        st.write(filtered_table[['Count of employees across each condition', 'Predicted Values']].rename({'Count of employees across each condition': 'Actual Value'}), index=False)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    


if __name__ == "__main__":
    run()
