def add_item(cart, canteen_name, shop_name, menu_name, price, options=None, note=""):
    if options is None:
        options = []
    options = sorted(options)
    note = note.strip()
    # ตรวจว่ามีอาหารรายการนี้จากร้านและโรงอาหารเดียวกันหรือยัง
    for item in cart:
        if (item["canteen"] == canteen_name
                and item["shop"] == shop_name
                and item["menu"] == menu_name
                and item["price"] == price
                and item["options"] == options
                and item["note"] == note):
            item["quantity"] += 1
            return

    # ถ้ายังไม่มี ให้เพิ่มรายการใหม่ จำนวน 1 ชิ้น
    cart.append({
        "canteen": canteen_name,
        "shop": shop_name,
        "menu": menu_name,
        "price": price,
        "quantity": 1,
        "options": options,
        "note": note,
    })


def increase_quantity(item):
    item["quantity"] += 1


def get_shops(cart):
    # ใช้ทั้งโรงอาหารและชื่อร้าน เผื่อมีร้านชื่อเดียวกันคนละโรงอาหาร
    shops = []
    for item in cart:
        shop = (item["canteen"], item["shop"])
        if shop not in shops:
            shops.append(shop)
    return shops


def get_shop_items(cart, canteen_name, shop_name):
    shop_items = []
    for item in cart:
        if item["canteen"] == canteen_name and item["shop"] == shop_name:
            shop_items.append(item)
    return shop_items


def decrease_quantity(item):
    # จำนวนต่ำสุดคือ 1 ถ้าต้องการเอาออกให้ใช้ remove_item
    if item["quantity"] > 1:
        item["quantity"] -= 1


def remove_item(cart, item):
    cart.remove(item)


def get_total_quantity(cart):
    total_quantity = 0
    for item in cart:
        total_quantity += item["quantity"]
    return total_quantity


def get_item_total(item):
    # ราคารวมของอาหารหนึ่งรายการ
    return item["price"] * item["quantity"]


def get_total_price(cart):
    total_price = 0
    for item in cart:
        total_price += get_item_total(item)
    return total_price
