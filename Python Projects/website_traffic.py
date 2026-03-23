blog_visits = [1200, 1350, 1600, 1800, 2100, 2500, 2300, 2700, 2600, 3000, 3300, 3600]

shop_visits = [800, 900, 1100, 1300, 1500, 1700, 1650, 1900, 1850, 2100, 2400, 2600]

websites = {
    "Blog": {
        "visits": blog_visits,
        "type": "Content",
        "owner": "Marketing Team"
    },
    "Shop": {
        "visits": shop_visits,
        "type": "E-commerce",
        "owner": "Sales Team"
    }
}

total_blog_visits = sum(
    websites["Blog"]["visits"]
)

total_shop_visits = sum(
    websites["Shop"]["visits"]
)

print(f"""Total Blog visits:
      {total_blog_visits:,}""")

print(f"""Total Shop visits:
      {total_shop_visits:,}""")

best_month = max(
    range(12),
    key=lambda m: websites["Blog"]["visits"][m]
)

print(f"""Best month for Blog traffic:
      Month {best_month + 1}""")