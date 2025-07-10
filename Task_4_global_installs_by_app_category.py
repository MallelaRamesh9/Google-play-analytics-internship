# ## 📌 Task 4: Global Installs by App Category

from datetime import datetime, time
import plotly.express as px

# Ensure current_time is defined
current_time = datetime.now().time()

# Add fake Country and ISO_Code columns if not present
if 'Country' not in df.columns:
    df['Country'] = 'USA'
    df['ISO_Code'] = 'USA'

# Filter: Only apps with over 1 million installs
filtered_df = df[df['Installs'] > 1_000_000]

# Create choropleth map
fig4 = px.choropleth(filtered_df,
                     locations='ISO_Code',
                     locationmode='ISO-3',
                     color='Installs',
                     hover_name='Category',
                     title='Global Installs by App Category',
                     color_continuous_scale='Viridis')

# Time-based visibility
start_time = time(15, 0)
end_time = time(21, 0)

if start_time <= current_time <= end_time:
    fig4.update_layout(geo=dict(showframe=False, showcoastlines=False))
    fig4.show()
else:
    print("Task 4 map is only visible between 06:00 PM and 09:00 PM IST.")

