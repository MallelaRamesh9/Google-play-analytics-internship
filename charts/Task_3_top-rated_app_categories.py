# ## 📌 Task 3: Top-Rated App Categories

from datetime import datetime, time
import plotly.express as px

# Make sure current_time is defined
current_time = datetime.now().time()

# Group by Category and calculate average Rating
category_df = df.groupby('Category')['Rating'].mean().reset_index()
category_df = category_df.sort_values(by='Rating', ascending=False).head(10)

# Plot
fig3 = px.bar(category_df, x='Category', y='Rating', color='Rating',
              title='Top 10 App Categories by Average Rating')

# Time-based display
start_time = time(15, 0)
end_time = time(18, 0)

if start_time <= current_time <= end_time:
    fig3.show()
else:
    print("Task 3 chart is only visible between 03:00 PM and 06:00 PM IST.")


