import kivy
import math
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.button import MDTextButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.list import OneLineIconListItem
from kivy.lang import Builder

kivy.require('1.9.1')

from kivymd.app import MDApp

KV = '''
<ContentNavigationDrawer>:
    ScrollView:
        MDList:
            OneLineIconListItem:
                text: "Калькулятор"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr1"

                IconLeftWidget:
                    icon: "1.png"

            OneLineIconListItem:
                text: "Расширенный Калькулятор"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr2"

                IconLeftWidget:
                    icon: "2.png"

            OneLineIconListItem:
                text: "Кредитный Калькулятор"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr3"

                IconLeftWidget:
                    icon: "3.png"

            OneLineIconListItem:
                text: "Конвертер объема памяти"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr4"

                IconLeftWidget:
                    icon: "4.png"

<Screen1>:
    name: "scr1"
    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            orientation: 'vertical'

            BoxLayout:
                ScrollView:
                    size_hint: (1, 0.5)
                    pos_hint: {"center_x": 0.5, "center_y": 0.4}

                    GridLayout:
                        cols: 1
                        size_hint_y: None
                        height: self.minimum_height

                        MDLabel:
                            id: history_label
                            text: root.history
                            halign: "left"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]


            MDTextField:
                id: input_field
                readonly: True
                multiline: True

        GridLayout:
            cols: 4
            spacing: '1dp'

            MDRaisedButton:
                text: '1'
                elevation: 3
                on_release: root.update_input_field('1')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '2'
                elevation: 3
                on_release: root.update_input_field('2')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '3'
                elevation: 3
                on_release: root.update_input_field('3')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '+'
                elevation: 3
                on_release: root.update_input_field('+')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '4'
                elevation: 3
                on_release: root.update_input_field('4')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '5'
                elevation: 3
                on_release: root.update_input_field('5')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '6'
                elevation: 3
                on_release: root.update_input_field('6')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '-'
                elevation: 3
                on_release: root.update_input_field('-')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '7'
                elevation: 3
                on_release: root.update_input_field('7')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '8'
                elevation: 3
                on_release: root.update_input_field('8')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '9'
                elevation: 3
                on_release: root.update_input_field('9')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '*'
                elevation: 3
                on_release: root.update_input_field('*')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '0'
                elevation: 3
                on_release: root.update_input_field('0')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '.'
                elevation: 3
                on_release: root.update_input_field('.')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '/'
                elevation: 3
                on_release: root.update_input_field('/')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '='
                elevation: 3
                on_release: root.calculate_result()
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: 'CE'
                elevation: 3
                on_release: root.clear_input_field()
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '<'
                elevation: 3
                on_release: root.remove_last_character()
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '('
                elevation: 3
                on_release: root.update_input_field('(')
                size_hint: (0.2, 0.2)

            MDRaisedButton:
                text: ')'
                elevation: 3
                on_release: root.update_input_field(')')
                size_hint: (0.2, 0.2)

<Screen2>:
    name: "scr2"
    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            orientation: 'vertical'

            BoxLayout:
                ScrollView:
                    size_hint: (1, 0.5)
                    pos_hint: {"center_x": 0.5, "center_y": 0.4}

                    GridLayout:
                        cols: 1
                        size_hint_y: None
                        height: self.minimum_height

                        MDLabel:
                            id: history_label
                            text: root.history
                            halign: "left"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]

            MDTextField:
                id: input_field
                readonly: True
                multiline: True

        GridLayout:
            cols: 5
            spacing: '1dp'

            MDRaisedButton:
                text: '1'
                elevation: 3
                on_release: root.update_input_field('1')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '2'
                elevation: 3
                on_release: root.update_input_field('2')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '3'
                elevation: 3
                on_release: root.update_input_field('3')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: 'CE'
                elevation: 3
                on_release: root.clear_input_field()
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '<'
                elevation: 3
                on_release: root.remove_last_character()
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '4'
                elevation: 3
                on_release: root.update_input_field('4')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '5'
                elevation: 3
                on_release: root.update_input_field('5')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '6'
                elevation: 3
                on_release: root.update_input_field('6')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '+'
                elevation: 3
                on_release: root.update_input_field('+')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '-'
                elevation: 3
                on_release: root.update_input_field('-')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '7'
                elevation: 3
                on_release: root.update_input_field('7')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '8'
                elevation: 3
                on_release: root.update_input_field('8')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '9'
                elevation: 3
                on_release: root.update_input_field('9')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '*'
                elevation: 3
                on_release: root.update_input_field('*')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '/'
                elevation: 3
                on_release: root.update_input_field('/')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '0'
                elevation: 3
                on_release: root.update_input_field('0')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '('
                elevation: 3
                on_release: root.update_input_field('(')
                size_hint: (0.2, 0.2)

            MDRaisedButton:
                text: ')'
                elevation: 3
                on_release: root.update_input_field(')')
                size_hint: (0.2, 0.2)

            MDRaisedButton:
                text: '^'
                elevation: 3
                on_release: root.update_input_field('^')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '.'
                elevation: 3
                on_release: root.update_input_field('.')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '%'
                elevation: 3
                on_release: root.update_input_field('%')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: 'sqrt'
                elevation: 3
                on_release: root.update_input_field('sqrt')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '!'
                elevation: 3
                on_release: root.update_input_field('!')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: 'log'
                elevation: 3
                on_release: root.update_input_field('log')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: 'sin'
                elevation: 3
                on_release: root.update_input_field('sin')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: 'cos'
                elevation: 3
                on_release: root.update_input_field('cos')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: 'tan'
                elevation: 3
                on_release: root.update_input_field('tan')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: 'mod'
                elevation: 3
                on_release: root.update_input_field('mod')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: 'pi'
                elevation: 3
                on_release: root.update_input_field('pi')
                size_hint: 0.2, 0.2

            MDRaisedButton:
                text: '='
                elevation: 3
                on_release: root.calculate_result()
                size_hint: 0.2, 0.2

<Screen3>:
    name: "scr3"

    BoxLayout:
        orientation: 'vertical'
        padding: dp(60)
        spacing: dp(10)
        BoxLayout:
            orientation: 'vertical'

            MDTextField:
                id: principal_input
                hint_text: "Сумма кредита"
                helper_text: "Введите сумму кредита"
                helper_text_mode: "on_focus"
                input_filter: "float"
                required: True

            MDTextField:
                id: interest_rate_input
                hint_text: "Процентная ставка"
                helper_text: "Введите процентную ставку"
                helper_text_mode: "on_focus"
                input_filter: "float"
                required: True

            MDTextField:
                id: loan_term_input
                hint_text: "Срок кредита (в годах)"
                helper_text: "Введите срок кредита"
                helper_text_mode: "on_focus"
                input_filter: "float"
                required: True

            MDRaisedButton:
                text: 'Рассчитать'
                elevation: 3
                on_release: root.calculate_credit()

            MDLabel:
                id: monthly_payment_label
                text: ""
                halign: "center"
                font_style: "Subtitle1"

            MDLabel:
                id: total_amount_label
                halign: 'center'
                text_size: self.width, None
                size_hint_y: None
                height: self.texture_size[1]

<Screen4>:
    name: "scr4"
    BoxLayout:
        orientation: 'vertical'
        padding: "10dp"
        spacing: "10dp"

        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, None
            height: "48dp"

            Label:
                text: "Convert from:"

            Spinner:
                id: from_spinner
                pos_hint: {"center_x": 0.5}
                text: "Bytes"
                values: ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Petabytes"]
                background_color: 'blue'

        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, None
            height: "48dp"

            Label:
                text: "Convert to:"

            Spinner:
                id: to_spinner
                pos_hint: {"center_x": 0.5}
                text: "Bytes"
                values: ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Petabytes"]
                background_color: 'blue'

        MDTextField:
            id: input_field
            hint_text: "Enter value"
            helper_text: "Input must be a number"
            helper_text_mode: "on_error"
            input_filter: "float"

        MDRaisedButton:
            text: "Convert"
            on_release: root.convert_units()

        MDTextField:
            id: output_field
            hint_text: "Converted value"
            readonly: True
            mode: "rectangle"
            multiline: False


Screen:
    MDTopAppBar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 1
        title: "Mеню"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen1:
            Screen2:
            Screen3:
            Screen4:

        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Screen1(Screen):
    history = StringProperty("")

    def update_input_field(self, value):
        input_field = self.ids.input_field
        input_field.text += value

    def calculate_result(self):
        try:
            input_field = self.ids.input_field
            expression = input_field.text
            result = eval(expression)
            input_field.text = str(result)
            if len(input_field.text) > 20:
                power = len(input_field.text) - 1
                text = f"{input_field.text[0]}e{power}"
                input_field.text = text
            self.history += f"\n{expression} = {input_field.text}"
        except Exception:
            input_field.text = 'Error'

    def clear_input_field(self):
        input_field = self.ids.input_field
        input_field.text = ''

    def remove_last_character(self):
        input_field = self.ids.input_field
        current_text = input_field.text
        input_field.text = current_text[:-1]


class Screen2(Screen):
    history = StringProperty("")

    def update_input_field(self, value):
        input_field = self.ids.input_field
        input_field.text += value
        if value == 'pi':
            input_field.text = input_field.text.replace('pi', str(math.pi), 1)

    def clear_input_field(self):
        input_field = self.ids.input_field
        input_field.text = ''

    def remove_last_character(self):
        input_field = self.ids.input_field
        current_text = input_field.text
        input_field.text = current_text[:-1]

    def calculate_result(self):
        try:
            input_field = self.ids.input_field
            expression = input_field.text

            while 'sqrt' in expression:
                idx = expression.index('sqrt')
                start = idx + 4
                level = 1
                while start < len(expression):
                    if expression[start] == '(':
                        level += 1
                    elif expression[start] == ')':
                        level -= 1
                    if level == 0:
                        break
                    start += 1
                number = expression[idx + 4:start]
                result = math.sqrt(float(number))
                expression = expression[:idx] + str(result) + expression[start + 1:]

            while '^' in expression:
                idx = expression.index('^')
                base_end = idx - 1
                while base_end >= 0 and expression[base_end].isdigit():
                    base_end -= 1
                base = expression[base_end + 1:idx]
                power_start = idx + 1
                level = 1
                while power_start < len(expression):
                    if expression[power_start] == '(':
                        level += 1
                    elif expression[power_start] == ')':
                        level -= 1
                    if level == 0:
                        break
                    power_start += 1
                power = expression[idx + 1:power_start]
                result = float(base) ** float(power)
                expression = expression[:base_end + 1] + str(result) + expression[power_start:]

            while '!' in expression:
                idx = expression.index('!')
                start = idx - 1
                while start >= 0 and expression[start].isdigit():
                    start -= 1
                number = expression[start + 1:idx]
                result = math.factorial(int(number))
                expression = expression[:start + 1] + str(result) + expression[idx + 1:]

            while any(op in expression for op in ['log', 'sin', 'cos', 'tan']):
                op_indices = []
                for op in ['log', 'sin', 'cos', 'tan']:
                    if op in expression:
                        op_indices.append(expression.index(op))
                min_index = min(op_indices)
                op = expression[min_index:min_index + 3]

                if op == 'log':
                    base, number = expression[min_index + 3:].split(',')
                    result = math.log(float(number), float(base))
                    expression = expression[:min_index] + str(result) + expression[
                                                                        min_index + 3 + len(base) + len(number):]

                elif op == 'sin':
                    angle = expression[min_index + 3:]
                    result = math.sin(math.radians(float(angle)))
                    expression = expression[:min_index] + str(result) + expression[min_index + 3 + len(angle):]

                elif op == 'cos':
                    angle = expression[min_index + 3:]
                    result = math.cos(math.radians(float(angle)))
                    expression = expression[:min_index] + str(result) + expression[min_index + 3 + len(angle):]

                elif op == 'tan':
                    angle = expression[min_index + 3:]
                    result = math.tan(math.radians(float(angle)))
                    expression = expression[:min_index] + str(result) + expression[min_index + 3 + len(angle):]

            result = eval(expression)
            input_field.text = str(result)
            self.history += f"\n{expression} = {input_field.text}"

        except Exception as e:
            input_field.text = "Ошибка"


class Screen3(Screen):
    def calculate_credit(self):
        principal_input = self.ids.principal_input
        interest_rate_input = self.ids.interest_rate_input
        loan_term_input = self.ids.loan_term_input
        monthly_payment_label = self.ids.monthly_payment_label
        total_amount_label = self.ids.total_amount_label

        principal = float(principal_input.text) if principal_input.text else 0
        interest_rate = float(interest_rate_input.text) if interest_rate_input.text else 0
        loan_term = float(loan_term_input.text) if loan_term_input.text else 0

        if not principal or not interest_rate or not loan_term:
            monthly_payment_label.text = "Пожалуйста, заполните все поля"
            total_amount_label.text = ""
        else:
            monthly_interest_rate = interest_rate / 100 / 12
            num_payments = int(loan_term * 12)

            monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
            total_amount = monthly_payment * num_payments

            monthly_payment_label.text = f"Ежемесячный платеж: {round(monthly_payment, 2)}"
            total_amount_label.text = f"Общая сумма с процентами: {round(total_amount, 2)}"

        monthly_payment_label.halign = 'center'
        total_amount_label.halign = 'center'
        monthly_payment_label.text_size = (self.width - dp(20), None)
        total_amount_label.text_size = (self.width - dp(20), None)
        monthly_payment_label.texture_update()
        total_amount_label.texture_update()


class Screen4(Screen):
    def convert_units(self):
        input_field = self.ids.input_field
        output_field = self.ids.output_field
        from_spinner = self.ids.from_spinner
        to_spinner = self.ids.to_spinner

        try:
            value = float(input_field.text)
            from_unit = from_spinner.text
            to_unit = to_spinner.text

            converted_value = self.convert_value(value, from_unit, to_unit)
            if converted_value is not None:
                output_field.text = "{:.6f}".format(converted_value)
            else:
                output_field.text = ""
        except ValueError:
            output_field.text = ""

        input_field.text = ""

    @staticmethod
    def convert_value(value, from_unit, to_unit):
        units = {
            "Bytes": 1,
            "Kilobytes": 1024 ** 1,
            "Megabytes": 1024 ** 2,
            "Gigabytes": 1024 ** 3,
            "Terabytes": 1024 ** 4,
            "Petabytes": 1024 ** 5
        }

        if from_unit in units and to_unit in units:
            return value * units[from_unit] / units[to_unit]
        else:
            return None


class MasterCalculater(MDApp):
    def build(self):
        Window.size = (400, 600)
        return Builder.load_string(KV)


if __name__ == '__main__':
    MasterCalculater().run()
