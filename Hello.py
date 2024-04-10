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

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Labor Count",
    )

    st.write("# Predict Labor Count")

    laborForm = st.form('laborForm')

    day_name = laborForm.selectbox('Enter the day', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    dept = laborForm.selectbox('Enter department', ['Employee', 'Supervisor', 'Manager'])
    
    age_group = laborForm.selectbox('Enter the combination of gender and age group', ['Female (23-50)', 'Female (50-65)', 'Male (23-50)', 'Male (50-65)'])
    
    shift_time = laborForm.selectbox('Enter the shift', ['Morning Shift (10 AM - 12 PM)', 'Afternoon Shift (12 PM - 3 PM)', 'Evening Shift (3 PM - 6 PM)'])

    submit = laborForm.form_submit_button(f'Predict')
    
if __name__ == "__main__":
    run()
