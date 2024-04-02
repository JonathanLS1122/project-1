import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class VectorCalculatorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.vector_a_input = TextInput(multiline=False, hint_text='Enter Vector A (comma separated)')
        self.vector_b_input = TextInput(multiline=False, hint_text='Enter Vector B (comma separated)')
        self.calculate_button = Button(text='Calculate')
        self.calculate_button.bind(on_press=self.on_calculate)

        self.result_label = Label(size_hint_y=None, height=100, text='Result will be shown here')

        self.layout.add_widget(self.vector_a_input)
        self.layout.add_widget(self.vector_b_input)
        self.layout.add_widget(self.calculate_button)
        self.layout.add_widget(self.result_label)

        return self.layout

    def on_calculate(self, instance):
        vector_a_str = self.vector_a_input.text.split(',')
        vector_b_str = self.vector_b_input.text.split(',')

        try:
            vector_a = np.array([float(i) for i in vector_a_str])
            vector_b = np.array([float(i) for i in vector_b_str])

            dot_product = np.dot(vector_a, vector_b)
            angle = np.arccos(dot_product / (np.linalg.norm(vector_a) * np.linalg.norm(vector_b)))
            mod_a = np.linalg.norm(vector_a)
            mod_b = np.linalg.norm(vector_b)

            self.result_label.text = (
                f"Dot Product: {dot_product}\n"
                f"Angle (radians): {angle}\n"
                f"Modulus of Vector A: {mod_a}\n"
                f"Modulus of Vector B: {mod_b}"
            )
        except ValueError:
            self.result_label.text = 'Invalid input! Make sure to input numbers only and separate them with commas.'

if __name__ == '__main__':
    VectorCalculatorApp().run()