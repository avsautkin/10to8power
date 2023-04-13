from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True


MDScreen:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "10to8power"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title_color: "#4a4939"
                    icon: "logo.jpg"
                    text: "Меню"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                

                MDNavigationDrawerLabel:
                    text: "Labels"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "О нас"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Язык"
                    
                    
                MDNavigationDrawerDivider:
                 
                MDNavigationDrawerLabel:
                    text: "Обратная связь:"

                MDNavigationDrawerDivider:
                    
                DrawerClickableItem:
                    icon: "gmail"
                    text_right_color: "#4a4939"
                    text: "iasautkin@gmail.com"
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)


Example().run()