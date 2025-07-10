# ## 📌 Task 5: Bubble Chart - App Size vs Rating

from datetime import datetime, time
import plotly.express as px

# Ensure current_time is defined
current_time = datetime.now().time()

# Filter apps with Size < 200MB
bubble_df = df[df['Size'] < 200_000_000]

# Create bubble chart
fig5 = px.scatter(bubble_df, 
                  x='Size', 
                  y='Rating', 
                  size='Installs',
                  color='Category', 
                  hover_name='App',
                  title='App Size vs Rating (Bubble Chart)',
                  size_max=60)

# Show only between 9 PM to 11:59 PM IST
start_time = time(21, 0)
end_time = time(23, 59)

if start_time <= current_time <= end_time:
    fig5.show()
else:
    print("Task 5 chart is only visible between 09:00 PM and 11:59 PM IST.")



