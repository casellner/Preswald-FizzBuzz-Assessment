from preswald import text, plotly, connect, get_df, table, query, slider
import pandas as pd
import plotly.express as px

# Load the CSV
connect() # load in all sources, which by default is the sample_csv
df = get_df('sample_csv')

# Query the data
sql = "SELECT * FROM sample_csv WHERE \"Number of Tourists (thousands)\" > 70"
filtered_df = query(sql, "sample_csv")

# Build an interactive UI
text("# Ice Cream Data Analysis App")
table(filtered_df)

# Add user controls
threshold = slider("Threshold", min_val=0, max_val=100, default=60)
table(df[df["Temperature (F)"] > threshold])

# Create a visualization
fig = px.scatter(df)
plotly(fig)
