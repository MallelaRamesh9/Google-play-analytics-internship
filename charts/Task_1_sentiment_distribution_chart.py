# ## 📌 Task 1: Sentiment Distribution Chart

from datetime import datetime, time
import numpy as np
import plotly.express as px

# Create sentiment
df['Sentiment'] = np.where(df['Rating'] >= 4.0, 'Positive',
                   np.where(df['Rating'] >= 2.5, 'Neutral', 'Negative'))

df['RatingGroup'] = pd.cut(df['Rating'], bins=[0, 2, 4, 5], labels=['1-2', '3-4', '4-5'])

sentiment_df = df.groupby(['RatingGroup', 'Sentiment']).size().reset_index(name='Count')

fig1 = px.bar(sentiment_df, x='RatingGroup', y='Count', color='Sentiment',
             title='Sentiment Distribution by Rating Group', barmode='stack')

# Add current time check
current_time = datetime.now().time()
start_time = time(8, 0)
end_time = time(12, 0)

if start_time <= current_time <= end_time:
    fig1.show()
else:
    print("Visualization is only visible between 08:00 AM and 12:00 PM IST.")

