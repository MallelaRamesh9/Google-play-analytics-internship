# ## 📌 Task 2: Free vs Paid Apps - Installs Comparison

from datetime import datetime, time
import plotly.express as px

# Make sure current_time is defined
current_time = datetime.now().time()

# Group by Type and sum Installs
type_df = df.groupby('Type')['Installs'].sum().reset_index()

# Plot
fig2 = px.bar(type_df, x='Type', y='Installs', color='Type',
              title='Free vs Paid Apps - Total Installs')

# Time-based filter
start_time = time(6, 0)
end_time = time(15, 0)

if start_time <= current_time <= end_time:
    fig2.show()
else:
    print("Task 2 chart is only visible between 12:00 PM and 3:00 PM IST.")


