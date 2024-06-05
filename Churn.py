import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

def load_data():
    return pd.read_csv('Customer-Churn-Records.csv')

data = load_data()

# Page configurations
st.set_page_config(
    page_title="Bank Customer Churn Analysis",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

st.markdown(
    """
    <style>
    .custom-container {
        background-color: #000000;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Wrapping the entire Streamlit app with a div and applying the custom styles
st.markdown('<div class="custom-container">', unsafe_allow_html=True)

st.set_option('deprecation.showPyplotGlobalUse', False)

# Create navigation bar
def main():
    st.sidebar.image('Bank.jpg')
    st.sidebar.title("Navigation")
    
    page = st.sidebar.radio("Go to", ["Home", "EDA", "Visualization"])

    data = pd.read_csv('Customer-Churn-Records.csv')
    df = data.copy()

    if page == "Home":
        # st.image('download.jpg',width=500)
        st.markdown("<div style='color: white; font-size: 50px; text-align: center;'>Welcome to My App</div>", unsafe_allow_html=True)
        st.write("This app helps you analyze Bank Customer Churn.")
        st.markdown("""
        <div style="font-size: 16px;">
        <ul>
        <li><b>RowNumber:</b> Row index or number of the entry.</li>
        <li><b>CustomerId:</b> Unique identifier for each customer.</li>
        <li><b>Surname:</b> Last name of the customer.</li>
        <li><b>CreditScore:</b> Numerical measure of a customer's creditworthiness.</li>
        <li><b>Geography:</b> Geographic location or country of the customer.</li>
        <li><b>Gender:</b> Gender of the customer.</li>
        <li><b>Age:</b> Age of the customer.</li>
        <li><b>Tenure:</b> Number of years the customer has been with the bank.</li>
        <li><b>Balance:</b> Amount of money in the customer's account.</li>
        <li><b>NumOfProducts:</b> Number of bank products the customer has.</li>
        <li><b>HasCrCard:</b> Whether the customer has a credit card (binary: 1 for yes, 0 for no).</li>
        <li><b>IsActiveMember:</b> Whether the customer is an active member (binary: 1 for yes, 0 for no).</li>
        <li><b>EstimatedSalary:</b> Estimated annual salary of the customer.</li>
        <li><b>Exited:</b> Whether the customer has exited the bank (binary: 1 for yes, 0 for no).</li>
        <li><b>Complain:</b> Whether the customer has filed a complaint (binary: 1 for yes, 0 for no).</li>
        <li><b>Satisfaction Score:</b> Satisfaction score of the customer.</li>
        <li><b>Card Type:</b> Type of credit card held by the customer.</li>
        <li><b>Point Earned:</b> Points earned by the customer.</li>
        </ul>
        </div>
        <p style="font-size: 16px;"><b>Preferred Payment Method:</b> Cash, Credit/Debit Card, Mobile Payment App</p>
        """, unsafe_allow_html=True)

    elif page == "EDA":
        st.title("Exploratory Data Analysis")
        st.markdown("""
        <p class="desc">This section provides an overview of the dataset through various analytical components. It includes descriptive statistics, data types, and the shape of the dataset. Use the sections below to explore different aspects of the dataset.</p>
        """,unsafe_allow_html=True)
        # Add your data analysis components here
        st.header("Data Set")
        st.dataframe(df.head())
        st.markdown("#### Shape of Data")
        st.markdown("""
        <p class="desc">Here, you can see the dimensions of the dataset represented as rows and columns. This information gives you an understanding of the dataset's size and structure.</p>
        """,unsafe_allow_html=True)
        st.write(df.shape)
        st.markdown("### Data Types")
        st.markdown("""
        <p class="desc">
                        Explore the data types of each column in the dataset. Understanding the data types is crucial for data preprocessing and analysis.
                        </p>
        """,unsafe_allow_html=True)
        st.write(df.dtypes)

        st.markdown("## Descriptive Statistic of Data")
        st.markdown("""
        <p class="desc">s
                        Get insights into the central tendencies and spread of numerical features in the dataset. These descriptive statistics help in understanding the distribution and variability of the data.
                        </p>
        """,unsafe_allow_html=True)
        st.write(df.describe())

        st.markdown("")

    elif page == "Visualization":
        # st.title("Data Visualization")
        # st.markdown("""
        # <p class="desc">This section provides visualizations to better understand the data and identify patterns or trends. Use the options below to explore different visualization types.</p>
        # """,unsafe_allow_html=True)

        # Pie Chart
        categories = ['Tenure', 'Gender', 'Geography', 'Card Type', 'Complain']
        st.title("Pie Chart")
        st.write("""
        ##### Distribution of Customers by Geography, Gender, Tenure, Card Type, and Complain.
        """)

        # Selecting the category for analysis
        category = st.selectbox("Select Category", categories)

        # Count the occurrences of each unique value in the selected category
        category_counts = df[category].value_counts()

        # Information about variables
        # category_info = {
        #     'Geography': "Geography represents the location or country of the customer.",
        #     'Gender': "Gender represents the gender of the customer.",
        #     'Tenure': "Tenure represents the number of years the customer has been with the bank.",
        #     'Card Type': "Card Type represents the type of credit card held by the customer.",
        #     'Complain': "Complain represents whether the customer has filed a complaint (binary: 1 for yes, 0 for no)."
        # }

        # Display information about the selected category
        # st.write(f"**{category.capitalize()} Information:**")
        # st.write(category_info.get(category, "No information available"))

        # Plotting pie chart using Plotly
        custom_colors = custom_colors =  ['#FFC0CB', '#FF5733', '#87CEEB', '#3366FF', '#C19A6B', '#8DB600']
        fig = px.pie(values=category_counts, names=category_counts.index, title=f'Distribution of Customers by {category}',
                  color_discrete_sequence=custom_colors)
        fig.update_layout(width=800, height=530)  # Increase size of the figure
        st.plotly_chart(fig)
        
        st.title("Bar Chart")
        
           # Title with additional information
        st.write("""
        ### Understanding Customer Churn Patterns through Bar Charts

        This bar chart visualizes the count of exited customers based on different categorical variables such as age, card type, geography, and gender. By examining the distribution of exited customers across these categories, businesses can gain insights into potential factors influencing customer churn.
        """)

        # Selecting the category for analysis
        category = st.selectbox("Select Category", ['Tenure', 'Age', 'Card Type', 'Geography', 'Gender'])

        # Creating AgeGroup column
        if category == 'Age':
            df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 30, 40, 50, 60, np.inf], labels=['30', '30-40', '40-50', '50-60', '60+'])

        # Plotting bar chart with Seaborn
        plt.figure(figsize=(10, 6))

        if category == 'Age':
            sns.countplot(x='AgeGroup', hue='Exited', data=df, palette=['#FF5733', '#33FF57'])
            plt.xlabel('Age Group')
        else:
            sns.countplot(x=category, hue='Exited', data=df, palette=['#FF5733', '#33FF57'])
            plt.xlabel(category)

        plt.ylabel('Count of Exited Customers')
        plt.title(f'Count of Exited Customers by {category}')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

        # Show the plot
        st.pyplot()
        ############################
        st.title("Bar Chart")
        
        
        # Title with additional information
        st.write("""
        ### Understanding Customer Churn Patterns through Bar Charts

        This bar chart visualizes the count of exited customers based on different categorical variables such as age, card type, geography, and gender. By examining the distribution of exited customers across these categories, businesses can gain insights into potential factors influencing customer churn.
        """)

        # Filter dataframe to include only exited customers
        exited_df = df[df['Exited'] == 1]

        # Creating AgeGroup column
        exited_df['AgeGroup'] = pd.cut(exited_df['Age'], bins=[0, 30, 40, 50, 60, float('inf')], labels=['30', '30-40', '40-50', '50-60', '60+'])

        # Aggregating counts by age group
        age_group_counts = exited_df['AgeGroup'].value_counts().reset_index()
        age_group_counts.columns = ['AgeGroup', 'Count']

        # Plotting bar chart with Plotly Express
        fig = px.bar(age_group_counts, x='AgeGroup', y='Count', 
                     title='Count of Exited Customers by Age Group',
                     labels={'AgeGroup': 'Age Group', 'Count': 'Count of Exited Customers'},
                     category_orders={'AgeGroup': ['30', '30-40', '40-50', '50-60', '60+']},
                     color_discrete_sequence=px.colors.qualitative.Pastel)  # Using a qualitative color palette

        fig.update_layout(xaxis_title='Age Group', yaxis_title='Count of Exited Customers', xaxis_tickangle=-45)
        st.plotly_chart(fig)
        #######
        st.title("Churn rate By Geography")
        churn_rate_geography = df.groupby('Geography')['Exited'].mean().reset_index()
        fig = px.bar(churn_rate_geography, x='Geography', y='Exited', color='Geography', 
                     labels={'Exited': 'Churn Rate', 'Geography': 'Geography'})
        fig.update_layout(title='Churn Rate by Geography', xaxis_title='Geography', yaxis_title='Churn Rate')
        st.plotly_chart(fig)
        ######
        st.title('Churn Rate By Gender')
        churn_rate_gender = df.groupby('Gender')['Exited'].mean().reset_index()
        fig = px.bar(churn_rate_gender, x='Gender', y='Exited', color='Gender', barmode='group', 
                     labels={'Exited': 'Churn Rate', 'Gender': 'Gender'})
        fig.update_layout(title='Churn Rate by Gender', xaxis_title='Gender', yaxis_title='Churn Rate')
        st.plotly_chart(fig)
                
        # Histogram

        

        st.title("Histogram Chart")
            # Sidebar for selecting variables
        # Sidebar for selecting variables
        dependent_variable = "Exited"
        independent_variables = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary', 'Satisfaction Score', 'Point Earned']

        selected_variable = st.selectbox(
            'Select variable',
            independent_variables,
            key="selected_variable"  # Unique key for this selectbox
        )

        # Explanation of variable insights
        st.write(f"""
        # Insights 
        Histograms of various variables in the dataset offer unique insights into different aspects of customer behavior and demographics.  
        """)

        # Create histogram using Plotly
        fig = px.histogram(df, x=selected_variable, y=dependent_variable, nbins=20, title=f'Distribution of {dependent_variable} by {selected_variable}')

        # Update layout to add a gap between bars
        fig.update_layout(
            xaxis_title=selected_variable,
            yaxis_title=dependent_variable,
            bargap=0.1,  # Adjust the value as needed for the desired gap
            template='plotly_white'  # you can choose different templates
        )

        # Display the Plotly histogram
        st.plotly_chart(fig)



        st.title("Box Chart")

        expenses_columns = ['EstimatedSalary', 'Gender', 'Age', 'HasCrCard', 'EstimatedSalary', 'Balance', 'HasCrCard',
                            'Complain', 'Satisfaction Score', 'IsActiveMember', 'Exited', 'Card Type', 'Point Earned',
                            'Tenure']

        x_inp = st.selectbox("Select Category", ['Exited'])
        y_inp = st.selectbox("Select Expense", expenses_columns)

        # Filtering data based on the selected category
        selected_data = df[df['Exited'] == (1 if x_inp == 'Exited' else 0)]

        # Create box plot using Plotly Express
        fig = px.box(selected_data, x=x_inp, y=y_inp, color=x_inp, title=f'Box Plot of {y_inp.capitalize()} for {x_inp.capitalize()} Customers',
                     color_discrete_sequence=["#ADD8E6"])  # Custom color sequence

        # Update layout
        fig.update_layout(
            xaxis_title=x_inp.capitalize(),
            yaxis_title=y_inp.capitalize(),
            template='plotly_white'
        )

        # Display the Plotly box plot
        st.plotly_chart(fig)
        
        

# Assuming you have loaded your DataFrame 'df'


        st.title("Stacked Bar Chart")

        # Title with additional information
        st.write("""
        ### Understanding Customer Churn Patterns through Stacked Bar Charts

        This stacked bar chart visualizes the count of exited customers based on different categorical variables such as age, card type, geography, and gender. By examining the distribution of exited customers across these categories, businesses can gain insights into potential factors influencing customer churn.
        """)

        # Selecting the category for analysis
        category = st.selectbox("Select Category", ['Tenure', 'Age', 'Card Type', 'Geography', 'Gender'], key="select_category")

        # Creating AgeGroup column
        if category == 'Age':
            df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 30, 40, 50, 60, np.inf], labels=['30', '30-40', '40-50', '50-60', '60+'])

        # Grouping data by category and churn status
        grouped_df = df.groupby([category, 'Exited']).size().reset_index(name='Count')

        # Define custom colors
        custom_colors = ['#1f77b4', '#ff7f0e']  # Blue and orange colors

        # Assigning custom colors to Exited categories
        grouped_df['Color'] = grouped_df['Exited'].map({0: custom_colors[0], 1: custom_colors[1]})

        # Plotting stacked bar chart with Plotly Express
        fig = px.bar(grouped_df, x=category, y='Count', color='Color', barmode='stack', 
                    labels={category: category, 'Count': 'Count of Customers', 'Exited': 'Exited'}, 
                    title=f'Count of Exited Customers by {category}')

        # Rotate x-axis labels for better readability
        fig.update_layout(xaxis_tickangle=-45)

        # Show the plot
        st.plotly_chart(fig)
        
        
        
        # Violene Plot
        fig_v, ax = plt.subplots()
        st.title("Violine Chart")
        expenses_columns = ['EstimatedSalary','Gender','Age','HasCrCard','EstimatedSalary','Balance','HasCrCard','Complain','Satisfaction Score','IsActiveMember','Exited', 'Card Type', 'Point Earned', '	Tenure']
        catigories = ['Exited']

        x_inp = st.selectbox("Select Cat",catigories)
        st.write("V/s")
        y_inp = st.selectbox("Select Expence",expenses_columns)

        st.markdown(f"""
        <h3>Distribution of {y_inp.capitalize().replace("_"," ")} by {x_inp.capitalize().replace("_"," ")}</h3>

        <p class="desc"> This violin plot displays the distribution of {y_inp.capitalize().replace("_"," ")} across different categories of {x_inp.capitalize().replace("_"," ")}. It provides insights into the spread and density of {y_inp.capitalize().replace("_"," ")} within each category, allowing for comparison between groups. Use the dropdown menus to select the category for the x-axis and the expense for the y-axis.</p>

        """,unsafe_allow_html=True)

        sns.violinplot(x=x_inp,y=y_inp, data=df)
        plt.xlabel('Category')
        plt.xticks(rotation=45) 
        plt.title('Violine Plot of Bank_Custmer')
        plt.legend([x_inp.capitalize().replace("_"," ")],title="Legend", loc="upper right", fontsize="small", fancybox=True, bbox_to_anchor=(1.9, 1))
        st.pyplot(fig_v)

if __name__ == "__main__":
    main()

# Closing the div tag
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<footer class='footer'>©  Mohsin_Fayyaz </footer>",unsafe_allow_html=True)
