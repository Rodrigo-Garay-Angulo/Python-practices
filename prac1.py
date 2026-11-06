def format_title(title, category="general"):
    sku_code = (title.lstrip().replace(' ', '-').lower() + f"@{category.lower()}")
    title = title.strip().title()

    return (title, sku_code)

print(format_title(" STAr WarS ", category="Space"))
    