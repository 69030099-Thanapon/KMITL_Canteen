from functools import partial

import customtkinter as ctk


class CanteenApp(ctk.CTk):
    """Main window for the KMITL Canteen desktop application."""

    def __init__(self):
        super().__init__()

        self.title("KMITL Canteen")
        self.geometry("1000x650")
        self.minsize(800, 500)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=24, pady=24)

        self.app_name_label = ctk.CTkLabel(
            self.main_frame,
            text="KMITL Canteen",
            font=ctk.CTkFont(size=32, weight="bold"),
        )
        self.app_name_label.pack(pady=(48, 12))

        # ข้อมูลตัวอย่าง: โรงอาหารแต่ละแห่งมีรายชื่อร้านของตัวเอง
        self.canteens = {
            "คณะครุศาสตร์": ["ร้านข้าวแกง", "ร้านก๋วยเตี๋ยว", "ร้านน้ำผลไม้"],
            "คณะวิทยาศาสตร์": ["ร้านอาหารตามสั่ง", "ร้านข้าวมันไก่", "ร้านกาแฟ"],
            "โรงอาหารพระเทพฯ": ["ร้านข้าวหมูแดง", "ร้านส้มตำ", "ร้านเครื่องดื่ม"],
        }

        # เมนูตัวอย่างของแต่ละร้าน: ชื่อเมนูคู่กับราคา (บาท)
        self.menus = {
            "ร้านข้าวแกง": {"ข้าวราดแกงเขียวหวาน": 40, "ข้าวราดผัดผัก": 35},
            "ร้านก๋วยเตี๋ยว": {"ก๋วยเตี๋ยวหมู": 45, "ก๋วยเตี๋ยวไก่": 40},
            "ร้านน้ำผลไม้": {"น้ำส้ม": 25, "น้ำแตงโม": 30},
            "ร้านอาหารตามสั่ง": {"ข้าวกะเพราหมู": 50, "ข้าวผัดไก่": 45},
            "ร้านข้าวมันไก่": {"ข้าวมันไก่ต้ม": 45, "ข้าวมันไก่ทอด": 50},
            "ร้านกาแฟ": {"อเมริกาโน่เย็น": 40, "ลาเต้เย็น": 45},
            "ร้านข้าวหมูแดง": {"ข้าวหมูแดง": 45, "ข้าวหมูกรอบ": 55},
            "ร้านส้มตำ": {"ส้มตำไทย": 40, "ข้าวเหนียว": 10},
            "ร้านเครื่องดื่ม": {"ชาไทย": 30, "โกโก้": 35},
        }

        self.page_title_label = ctk.CTkLabel(
            self.main_frame,
            text="",
            font=ctk.CTkFont(size=18),
        )
        self.page_title_label.pack(pady=(0, 12))

        self.page_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.page_frame.pack(fill="both", expand=True, padx=24, pady=12)

        self.show_canteens()

    def clear_page(self):
        # ลบเนื้อหาหน้าเดิม ก่อนแสดงหน้าใหม่
        for widget in self.page_frame.winfo_children():
            widget.destroy()

    def show_canteens(self):
        self.clear_page()
        self.page_title_label.configure(text="เลือกโรงอาหาร")

        for canteen_name in self.canteens:
            canteen_button = ctk.CTkButton(
                self.page_frame,
                text=canteen_name,
                width=300,
                height=48,
                font=ctk.CTkFont(size=18),
                # จำชื่อโรงอาหารไว้ แล้วส่งให้ show_shops เมื่อกดปุ่ม
                command=partial(self.show_shops, canteen_name),
            )
            canteen_button.pack(pady=8)

    def show_shops(self, canteen_name):
        self.clear_page()
        self.page_title_label.configure(text=f"ร้านอาหาร — {canteen_name}")

        sample_label = ctk.CTkLabel(
            self.page_frame,
            text="ร้านตัวอย่าง — กดเลือกร้านเพื่อดูเมนู",
        )
        sample_label.pack(pady=(0, 12))

        for shop_name in self.canteens[canteen_name]:
            shop_button = ctk.CTkButton(
                self.page_frame,
                text=shop_name,
                width=300,
                height=40,
                font=ctk.CTkFont(size=18),
                command=partial(self.show_menu, canteen_name, shop_name),
            )
            shop_button.pack(pady=8)

        back_button = ctk.CTkButton(
            self.page_frame,
            text="กลับไปเลือกโรงอาหาร",
            command=self.show_canteens,
        )
        back_button.pack(pady=(24, 0))

    def show_menu(self, canteen_name, shop_name):
        self.clear_page()
        self.page_title_label.configure(text=f"{canteen_name} — {shop_name}")

        sample_label = ctk.CTkLabel(
            self.page_frame,
            text="เมนูและราคาตัวอย่าง — ยังสั่งอาหารไม่ได้",
        )
        sample_label.pack(pady=(0, 12))

        for menu_name, price in self.menus[shop_name].items():
            menu_label = ctk.CTkLabel(
                self.page_frame,
                text=f"{menu_name}  —  {price} บาท",
                font=ctk.CTkFont(size=18),
            )
            menu_label.pack(pady=8)

        back_button = ctk.CTkButton(
            self.page_frame,
            text="กลับไปเลือกร้าน",
            command=partial(self.show_shops, canteen_name),
        )
        back_button.pack(pady=(24, 0))
