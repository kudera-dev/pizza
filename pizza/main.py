from kivy.lang import Builder
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd import app
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDTopAppBar:
        title: 'Welcome!'
        md_bg_color: 1, 1, 1, 1  # Set the toolbar background color to white
        specific_text_color: 0, 0, 0, 1
        right_action_items: [['bell-ring', lambda x: app.on_bell_click()]]

    ScreenManager:
        id: content_manager

        MDScreen:
            name: 'home_content'
            BoxLayout:
                orientation: 'vertical'

                MDTabs:
                    background_color: 1, 1, 1, 1  # Set tab background to white
                    text_color_normal: 0, 0, 0, 1  # Set inactive tab text color to black
                    text_color_active: 0, 0, 1, 1  # Set active tab text color to blue

                    Tab:
                        title: 'Pizza'
                        ScrollView:
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: dp(10)
                                spacing: dp(20)

                                MDCard:
                                    orientation: 'horizontal'
                                    size_hint: None, None
                                    size: "280dp", "100dp"
                                    padding: dp(5)
                                    ripple_behavior: False  # Set to False to disable ripple effect
                                    md_bg_color: 1, 0.85, 0, 1  # Yellow background for the card

                                    FitImage:
                                        source: 'image/pizza.png'
                                        size_hint_x: 0.3

                                    BoxLayout:
                                        orientation: 'vertical'
                                        padding: dp(20)
                                        spacing: dp(20)

                                        MDLabel:
                                            text: 'Pizza with Mushrooms'
                                            theme_text_color: 'Primary'
                                            bold: True

                                        MDLabel:
                                            text: '14-20 minutes'
                                            theme_text_color: 'Secondary'

                                        MDLabel:
                                            text: '₱225'
                                            theme_text_color: 'Primary'
                                            bold: True

                                    MDFillRoundFlatButton:
                                        id: add_pizza_mushroom
                                        icon: 'plus'
                                        text: 'add'
                                        md_bg_color: 1, 1, 1, 1  # White background
                                        text_color: 0, 0, 0, 1
                                        icon_color: 0, 0, 0, 1  # Black icon
                                        pos_hint: {'center_y': 0.5}
                                        size_hint: None, None
                                        size: dp(40), dp(40)
                                        on_release: lambda: app.add_to_cart('Pizza with Mushrooms', 225)

                                MDCard:
                                    orientation: 'horizontal'
                                    size_hint: None, None
                                    size: "280dp", "100dp"
                                    padding: dp(5)
                                    ripple_behavior: False
                                    md_bg_color: 1, 0.85, 0, 1  # Yellow background for the card

                                    FitImage:
                                        source: 'image/pizza.png'
                                        size_hint_x: 0.3

                                    BoxLayout:
                                        orientation: 'vertical'
                                        padding: dp(10)
                                        spacing: dp(10)

                                        MDLabel:
                                            text: 'Pepperoni Cheese Pizza'
                                            theme_text_color: 'Primary'
                                            bold: True

                                        MDLabel:
                                            text: '18-25 minutes'
                                            theme_text_color: 'Secondary'

                                        MDLabel:
                                            text: '₱245'
                                            theme_text_color: 'Primary'
                                            bold: True

                                    MDFillRoundFlatIconButton:
                                        id: add_pepperoni
                                        icon: 'plus'
                                        text: 'add'
                                        md_bg_color: 1, 1, 1, 1  # White background
                                        text_color: 0, 0, 0, 1
                                        icon_color: 0, 0, 0, 1  # Black icon
                                        pos_hint: {'center_y': 0.5}
                                        size_hint: None, None
                                        size: dp(40), dp(40)
                                        on_release: lambda: app.add_to_cart('Pepperoni Cheese Pizza', 245)

                    Tab:
                        title: 'Burgers'
                        ScrollView:
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: dp(10)
                                spacing: dp(20)

                                MDCard:
                                    orientation: 'horizontal'
                                    size_hint: None, None
                                    size: "280dp", "100dp"
                                    padding: dp(5)
                                    ripple_behavior: False
                                    md_bg_color: 1, 0.85, 0, 1  # Yellow background for the card

                                    FitImage:
                                        source: 'image/burger1.png'
                                        size_hint_x: 0.5

                                    BoxLayout:
                                        orientation: 'vertical'
                                        padding: dp(10)
                                        spacing: dp(10)

                                        MDLabel:
                                            text: 'Cheeseburger'
                                            theme_text_color: 'Primary'
                                            bold: True

                                        MDLabel:
                                            text: '10-15 minutes'
                                            theme_text_color: 'Secondary'

                                        MDLabel:
                                            text: '₱150'
                                            theme_text_color: 'Primary'
                                            bold: True

                                    MDFillRoundFlatIconButton:
                                        id: add_cheeseburger
                                        icon: 'plus'
                                        text: 'add'
                                        md_bg_color: 1, 1, 1, 1  # White background
                                        text_color: 0, 0, 0, 1
                                        icon_color: 0, 0, 0, 1  # Black icon
                                        pos_hint: {'center_y': 0.5}
                                        size_hint: None, None
                                        size: dp(40), dp(40)
                                        on_release: lambda: app.add_to_cart('Cheeseburger', 150)

                                MDCard:
                                    orientation: 'horizontal'
                                    size_hint: None, None
                                    size: "280dp", "100dp"
                                    padding: dp(5)
                                    ripple_behavior: False
                                    md_bg_color: 1, 0.85, 0, 1  # Yellow background for the card

                                    FitImage:
                                        source: 'image/burger2.png'
                                        size_hint_x: 0.5

                                    BoxLayout:
                                        orientation: 'vertical'
                                        padding: dp(10)
                                        spacing: dp(10)

                                        MDLabel:
                                            text: 'Bacon Burger'
                                            theme_text_color: 'Primary'
                                            bold: True

                                        MDLabel:
                                            text: '12-18 minutes'
                                            theme_text_color: 'Secondary'

                                        MDLabel:
                                            text: '₱180'
                                            theme_text_color: 'Primary'
                                            bold: True

                                    MDFillRoundFlatIconButton:
                                        id: add_bacon_burger
                                        icon: 'plus'
                                        text: 'add'
                                        md_bg_color: 1, 1, 1, 1  # White background
                                        text_color: 0, 0, 0, 1
                                        icon_color: 0, 0, 0, 1  # Black icon
                                        pos_hint: {'center_y': 0.5}
                                        size_hint: None, None
                                        size: dp(40), dp(40)
                                        on_release: lambda: app.add_to_cart('Bacon Burger', 180)

                    Tab:
                        title: 'Fries'
                        ScrollView:
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: dp(10)
                                spacing: dp(20)

                                MDCard:
                                    orientation: 'horizontal'
                                    size_hint: None, None
                                    size: "280dp", "100dp"
                                    padding: dp(5)
                                    ripple_behavior: False
                                    md_bg_color: 1, 0.85, 0, 1  # Yellow background for the card

                                    FitImage:
                                        source: 'image/fries.png'
                                        size_hint_x: 0.3

                                    BoxLayout:
                                        orientation: 'vertical'
                                        padding: dp(10)
                                        spacing: dp(10)

                                        MDLabel:
                                            text: 'Classic Fries'
                                            theme_text_color: 'Primary'
                                            bold: True

                                        MDLabel:
                                            text: '5-10 minutes'
                                            theme_text_color: 'Secondary'

                                        MDLabel:
                                            text: '₱60'
                                            theme_text_color: 'Primary'
                                            bold: True

                                    MDFillRoundFlatIconButton:
                                        id: add_classic_fries
                                        icon: 'plus'
                                        text: 'add'
                                        md_bg_color: 1, 1, 1, 1  # White background
                                        text_color: 0, 0, 0, 1
                                        icon_color: 0, 0, 0, 1  # Black icon
                                        pos_hint: {'center_y': 0.5}
                                        size_hint: None, None
                                        size: dp(40), dp(40)
                                        on_release: lambda: app.add_to_cart('Classic Fries', 60)

                                MDCard:
                                    orientation: 'horizontal'
                                    size_hint: None, None
                                    size: "280dp", "100dp"
                                    padding: dp(5)
                                    ripple_behavior: False
                                    md_bg_color: 1, 0.85, 0, 1  # Yellow background for the card

                                    FitImage:
                                        source: 'image/cheese_fries.png'
                                        size_hint_x: 0.3

                                    BoxLayout:
                                        orientation: 'vertical'
                                        padding: dp(10)
                                        spacing: dp(10)

                                        MDLabel:
                                            text: 'Cheese Fries'
                                            theme_text_color: 'Primary'
                                            bold: True

                                        MDLabel:
                                            text: '7-12 minutes'
                                            theme_text_color: 'Secondary'

                                        MDLabel:
                                            text: '₱80'
                                            theme_text_color: 'Primary'
                                            bold: True

                                    MDFillRoundFlatIconButton:
                                        id: add_cheese_fries
                                        icon: 'plus'
                                        text: 'add'
                                        md_bg_color: 1, 1, 1, 1  # White background
                                        text_color: 0, 0, 0, 1
                                        icon_color: 0, 0, 0, 1  # Black icon
                                        pos_hint: {'center_y': 0.5}
                                        size_hint: None, None
                                        size: dp(40), dp(40)
                                        on_release: lambda: app.add_to_cart('Cheese Fries', 80)

        MDScreen:
            name: 'favorite_content'
            BoxLayout:
                orientation: 'vertical'
                MDLabel:
                    text: 'Favorite Screen'
                    halign: 'center'

        MDScreen:
            name: 'cart_content'
            BoxLayout:
                orientation: 'vertical'

                ScrollView:
                    MDBoxLayout:
                        orientation: 'vertical'
                        adaptive_height: True
                        padding: dp(10)
                        spacing: dp(20)
                        id: cart_items_container

                        # Placeholder for dynamically added cart items

                MDFillRoundFlatButton:
                    text: 'Proceed to Orders'
                    pos_hint: {'center_x': 0.5}
                    on_release: app.switch_content('my_orders_content')

        MDScreen:
            name: 'my_orders_content'
            BoxLayout:
                orientation: 'vertical'

                ScrollView:
                    MDBoxLayout:
                        orientation: 'vertical'
                        adaptive_height: True
                        padding: dp(10)
                        spacing: dp(20)



    MDBottomNavigation:
        size_hint_y: 0.5  # Take up a small part of the vertical space
        text_color_active: 1, 0, 0, 1  # Red color for active text

        MDBottomNavigationItem:
            name: 'home'
            text: 'Home'
            icon: 'home'
            on_tab_press: app.switch_content('home_content')

        MDBottomNavigationItem:
            name: 'favorite'
            text: 'Favorite'
            icon: 'heart'
            on_tab_press: app.switch_content('favorite_content')

        MDBottomNavigationItem:
            name: 'cart'
            text: 'Cart'
            icon: 'cart'
            on_tab_press: app.switch_content('cart_content')

        MDBottomNavigationItem:
            name: 'my_orders'
            text: 'My Orders'
            icon: 'clipboard-list'
            on_tab_press: app.switch_content('my_orders_content')
'''


class Tab(BoxLayout, MDTabsBase):
    """Class implementing content for a tab."""


def create_cart_item_widget(item_name, item_price, item_quantity):
    cart_item_card = MDCard(
        orientation='horizontal',
        size_hint_y=None,
        height=dp(100),
        padding=dp(5),
        ripple_behavior=True,
        md_bg_color=(1, 0.85, 0, 1)
    )

    item_label = MDLabel(text=item_name, theme_text_color='Primary', bold=True)
    quantity_box = BoxLayout(orientation='horizontal')
    decrement_button = MDFillRoundFlatIconButton(icon='minus', text='', md_bg_color=(1, 1, 1, 1),
                                                 text_color=(0, 0, 0, 1), icon_color=(0, 0, 0, 1),
                                                 pos_hint={'center_y': 0.3}, size_hint=(None, None),
                                                 size=(dp(40), dp(40)))
    quantity_label = MDLabel(text=str(item_quantity), theme_text_color='Primary', bold=True)
    increment_button = MDFillRoundFlatIconButton(icon='plus', text='', md_bg_color=(1, 1, 1, 1),
                                                 text_color=(0, 0, 0, 1), icon_color=(0, 0, 0, 1),
                                                 pos_hint={'center_y': 0.3}, size_hint=(None, None),
                                                 size=(dp(40), dp(40)))
    quantity_box.add_widget(decrement_button)
    quantity_box.add_widget(quantity_label)
    quantity_box.add_widget(increment_button)

    price_label = MDLabel(text=f'₱{item_price * item_quantity}', theme_text_color='Primary', bold=True)

    cart_item_card.add_widget(item_label)
    cart_item_card.add_widget(quantity_box)
    cart_item_card.add_widget(price_label)

    decrement_button.bind(on_release=lambda x: app.decrement_item(item_name))
    increment_button.bind(on_release=lambda x: app.increment_item(item_name))

    return cart_item_card


class MainApp(MDApp):
    cart_items = []

    def build(self):
        Window.size = (300, 500)
        self.screen = Builder.load_string(KV)
        Clock.schedule_once(self.setup_app, 0)
        return self.screen

    def setup_app(self, dt):
        self.cart_content = self.screen.ids.cart_items_container

    def on_bell_click(self):
        print("Bell icon clicked!")

    def add_to_cart(self, item_name, item_price):
        for item in self.cart_items:
            if item['name'] == item_name:
                item['quantity'] += 1
                self.update_cart_screen()
                return

        self.cart_items.append({'name': item_name, 'price': item_price, 'quantity': 1})
        self.update_cart_screen()

    def increment_item(self, item_name):
        for item in self.cart_items:
            if item['name'] == item_name:
                item['quantity'] += 1
                self.update_cart_screen()
                return

    def decrement_item(self, item_name):
        for item in self.cart_items:
            if item['name'] == item_name:
                if item['quantity'] > 1:
                    item['quantity'] -= 1
                else:
                    self.cart_items.remove(item)
                self.update_cart_screen()
                return

    def update_cart_screen(self):
        self.cart_content.clear_widgets()
        for item in self.cart_items:
            cart_item_widget = create_cart_item_widget(item['name'], item['price'], item['quantity'])
            self.cart_content.add_widget(cart_item_widget)

    def switch_content(self, screen_name):
        self.screen.ids.content_manager.current = screen_name


if __name__ == '__main__':
    MainApp().run()
