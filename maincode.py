import tkinter as tk
from tkinter import font

class FertilizerAdvisor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🌱 Farm Fertilizer Advisor")
        self.configure(bg='#f0f9f0')
        self.geometry("500x550")
        self.resizable(False, False)
        self.center_window()

        # Color scheme
        self.colors = {
            'primary': '#2e7d32',
            'secondary': '#4caf50',
            'background': '#f0f9f0',
            'card_bg': '#ffffff',
            'text_primary': '#1b5e20',
            'text_secondary': '#388e3c',
            'accent_green': '#4caf50',
            'accent_yellow': '#ff9800',
            'accent_red': '#f44336',
            'hover_green': '#45a049',
            'hover_yellow': '#e68900',
            'hover_red': '#d32f2f'
        }

        # Custom fonts
        self.title_font = font.Font(family="Segoe UI", size=22, weight="bold")
        self.header_font = font.Font(family="Segoe UI", size=16, weight="bold")
        self.text_font = font.Font(family="Segoe UI", size=11)
        self.subtext_font = font.Font(family="Segoe UI", size=10)
        self.button_font = font.Font(family="Segoe UI", size=12, weight="bold")

        self.create_widgets()

    def center_window(self):
        """Center the window on the screen"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'500x550+{x}+{y}')

    def create_widgets(self):
        # Main container with shadow effect
        main_container = tk.Frame(self, bg=self.colors['background'])
        main_container.pack(fill='both', expand=True, padx=20, pady=20)

        # Header section
        header_frame = tk.Frame(main_container, bg=self.colors['background'])
        header_frame.pack(fill='x', pady=(0, 20))

        # Title with icon
        title_frame = tk.Frame(header_frame, bg=self.colors['background'])
        title_frame.pack(fill='x')
        
        tk.Label(title_frame, text="🌱", font=("Segoe UI", 28), 
                bg=self.colors['background'], fg=self.colors['primary']).pack(side='left')
        
        title_text = tk.Label(title_frame, text="Fertilizer Advisor", 
                             font=self.title_font, fg=self.colors['text_primary'], 
                             bg=self.colors['background'])
        title_text.pack(side='left', padx=(10, 0))

        # Subtitle
        subtitle = tk.Label(header_frame, 
                           text="Select the primary nutrient your soil needs most",
                           font=self.text_font, fg=self.colors['text_secondary'], 
                           bg=self.colors['background'])
        subtitle.pack(pady=(5, 0))

        # Card container
        card = tk.Frame(main_container, bg=self.colors['card_bg'], bd=0, 
                       relief='raised', highlightbackground='#e0e0e0', 
                       highlightthickness=1)
        card.pack(fill='both', expand=True, padx=5, pady=5)

        # Buttons frame
        btn_frame = tk.Frame(card, bg=self.colors['card_bg'])
        btn_frame.pack(pady=30)

        # Nutrient buttons
        self.buttons = {}
        self.create_modern_button(btn_frame, "N", "Nitrogen", 
                                 self.colors['accent_green'], self.colors['hover_green'])
        self.create_modern_button(btn_frame, "P", "Phosphorus", 
                                 self.colors['accent_yellow'], self.colors['hover_yellow'])
        self.create_modern_button(btn_frame, "K", "Potassium", 
                                 self.colors['accent_red'], self.colors['hover_red'])

        # Advice section
        self.advice_container = tk.Frame(card, bg=self.colors['card_bg'])
        self.advice_container.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Initial state message
        self.initial_message = tk.Label(self.advice_container,
                text="💡 Click on any nutrient button above to get personalized fertilizer recommendations tailored to your soil's needs.",
                font=self.subtext_font, fg='#1565c0', bg='#e3f2fd', 
                wraplength=400, justify='center', padx=20, pady=15,
                bd=1, relief='solid')
        self.initial_message.pack(fill='x')

        # Advice content (initially hidden)
        self.advice_content = tk.Frame(self.advice_container, bg=self.colors['card_bg'])
        
        # Icon and title
        self.advice_header = tk.Frame(self.advice_content, bg=self.colors['card_bg'])
        self.advice_header.pack(fill='x', pady=(0, 10))
        
        self.advice_icon = tk.Label(self.advice_header, font=("Segoe UI", 20),
                                   bg=self.colors['card_bg'])
        self.advice_icon.pack(side='left')
        
        self.advice_title = tk.Label(self.advice_header, font=self.header_font,
                                    bg=self.colors['card_bg'], justify='left')
        self.advice_title.pack(side='left', padx=(10, 0))

        # Advice text
        self.advice_text = tk.Label(self.advice_content, font=self.text_font,
                                  bg=self.colors['card_bg'], wraplength=420, 
                                  justify='left', anchor='w')
        self.advice_text.pack(fill='x', pady=(0, 10))

        # Recommendation box
        self.recommendation_frame = tk.Frame(self.advice_content, bg='#fff3e0',
                                           bd=1, relief='solid')
        self.recommendation_frame.pack(fill='x', pady=5)
        
        self.ratio_text = tk.Label(self.recommendation_frame, font=self.subtext_font,
                                 bg='#fff3e0', wraplength=400, justify='left',
                                 padx=15, pady=10)
        self.ratio_text.pack(fill='x')

        # Reset button
        reset_frame = tk.Frame(card, bg=self.colors['card_bg'])
        reset_frame.pack(fill='x', padx=20, pady=10)
        
        self.reset_btn = tk.Button(reset_frame, text="🔄 Start Over", 
                                  font=self.text_font, command=self.reset_advisor,
                                  bg='#757575', fg='white', activebackground='#616161',
                                  activeforeground='white', bd=0, padx=20, pady=8,
                                  cursor='hand2')
        self.reset_btn.pack(side='right')

    def create_modern_button(self, parent, nut_symbol, nut_name, color, hover_color):
        btn_frame = tk.Frame(parent, bg=self.colors['card_bg'])
        btn_frame.pack(side='left', padx=12)
        
        btn = tk.Button(btn_frame, 
                       text=f" {nut_symbol}\n{nut_name}",
                       font=self.button_font, 
                       fg='white',
                       bg=color,
                       activebackground=hover_color,
                       width=12,
                       height=3,
                       bd=0,
                       relief='flat',
                       cursor='hand2',
                       command=lambda: self.give_fertilizer_advice(nut_symbol))
        btn.pack()
        
        # Add hover effects
        def on_enter(e):
            btn['bg'] = hover_color
        def on_leave(e):
            if nut_symbol not in self.selected_nutrient:
                btn['bg'] = color
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        self.buttons[nut_symbol] = btn
        self.selected_nutrient = None

    def give_fertilizer_advice(self, nutrient):
        self.selected_nutrient = nutrient
        
        advice_data = {
            "N": {
                "icon": "🌿",
                "title": "Nitrogen (N) Recommendation",
                "text": "Nitrogen is essential for vegetative growth, promoting lush green leaves and strong stems. Crucial for leafy vegetables like lettuce, spinach, and grasses. Deficiency shows as yellowing leaves and stunted growth.",
                "ratio": "💡 Recommendation: Use high-N fertilizers like Urea (46-0-0) or Ammonium Nitrate (34-0-0). Apply during active growth phases for best results.",
                "color": self.colors['accent_green']
            },
            "P": {
                "icon": "🌻", 
                "title": "Phosphorus (P) Recommendation",
                "text": "Phosphorus promotes robust root development, abundant flowering, and fruit production. Essential during planting, early growth stages, and fruit setting. Deficiency causes purple tinting and poor fruiting.",
                "ratio": "💡 Recommendation: Use high-P fertilizers like Triple Superphosphate (0-46-0) or DAP (18-46-0). Ideal for root crops and flowering plants.",
                "color": self.colors['accent_yellow']
            },
            "K": {
                "icon": "🍎",
                "title": "Potassium (K) Recommendation",
                "text": "Potassium acts as the plant's health booster, enhancing disease resistance, drought tolerance, and improving fruit quality and ripening. Deficiency appears as brown leaf edges and weak stems.",
                "ratio": "💡 Recommendation: Use high-K fertilizers like Muriate of Potash (0-0-60) or Potassium Sulfate (0-0-50). Perfect for fruiting vegetables and stress periods.",
                "color": self.colors['accent_red']
            }
        }
        
        data = advice_data[nutrient]
        
        # Update advice content
        self.advice_icon.config(text=data["icon"], fg=data["color"])
        self.advice_title.config(text=data["title"], fg=data["color"])
        self.advice_text.config(text=data["text"])
        self.ratio_text.config(text=data["ratio"])
        
        # Show advice and hide initial message
        self.initial_message.pack_forget()
        self.advice_content.pack(fill='both', expand=True)
        
        # Update button states with modern selection indicator
        for btn_key, btn in self.buttons.items():
            if btn_key == nutrient:
                # Selected state - add border
                btn.config(relief='solid', bd=2, highlightbackground=data["color"],
                          highlightcolor=data["color"], highlightthickness=2)
            else:
                # Deselected state
                btn.config(relief='flat', bd=0, highlightthickness=0)

    def reset_advisor(self):
        """Reset the advisor to initial state"""
        self.selected_nutrient = None
        self.advice_content.pack_forget()
        self.initial_message.pack(fill='x')
        
        # Reset all buttons to default state
        for btn_key, btn in self.buttons.items():
            colors = {
                "N": (self.colors['accent_green'], self.colors['hover_green']),
                "P": (self.colors['accent_yellow'], self.colors['hover_yellow']),
                "K": (self.colors['accent_red'], self.colors['hover_red'])
            }
            btn.config(relief='flat', bd=0, highlightthickness=0,
                      bg=colors[btn_key][0])


if __name__ == "__main__":
    app = FertilizerAdvisor()
    app.mainloop()
