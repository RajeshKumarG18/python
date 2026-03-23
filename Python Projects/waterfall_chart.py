import plotly.graph_objects as go

fig = go.Figure(go.Waterfall(
    name = "Profit Breakdown",
    orientation = "v",
    measure = ["relative", "relative", "relative", "relative", "total"],
    x = ["Revenue", "Cost of Goods", "Operating Expenses", "Marketing", "Net Profit"],
    y = [1000, -200, -150, -100, 0],
))
fig.update_layout(title = "Company Profit Analysis")
fig.show()