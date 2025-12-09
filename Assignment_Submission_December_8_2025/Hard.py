# interactive_plotly.py
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Sample sales data
regions = ["North", "South", "East", "West"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales_data = {
    "North": [150, 200, 250, 300, 280, 350],
    "South": [180, 220, 260, 310, 290, 360],
    "East": [130, 170, 210, 250, 230, 300],
    "West": [160, 210, 240, 290, 270, 330]
}

# --- 1. Bar Chart for total sales by region ---
total_sales = [sum(sales_data[region]) for region in regions]

bar_chart = go.Figure(
    data=[go.Bar(x=regions, y=total_sales, marker_color='skyblue')],
    layout_title_text="Total Sales by Region"
)
bar_chart.update_layout(
    xaxis_title="Region",
    yaxis_title="Total Sales",
    template="plotly_dark"
)

# --- 2. Line Chart for monthly sales per region ---
line_chart = go.Figure()
for region in regions:
    line_chart.add_trace(
        go.Scatter(x=months, y=sales_data[region], mode='lines+markers', name=region)
    )
line_chart.update_layout(
    title="Monthly Sales by Region",
    xaxis_title="Month",
    yaxis_title="Sales",
    template="plotly_dark"
)

# --- 3. Scatter Plot comparing North vs South sales ---
scatter_chart = go.Figure()
scatter_chart.add_trace(
    go.Scatter(
        x=sales_data["North"],
        y=sales_data["South"],
        mode='markers+text',
        text=months,
        textposition='top center',
        marker=dict(size=12, color='orange', symbol='circle'),
        name="North vs South"
    )
)
scatter_chart.update_layout(
    title="North vs South Monthly Sales",
    xaxis_title="North Sales",
    yaxis_title="South Sales",
    template="plotly_dark"
)

# --- Display all plots ---
bar_chart.show()
line_chart.show()
scatter_chart.show()
