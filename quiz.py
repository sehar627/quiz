from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button

class QuizApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # === Question 1 ===
        self.layout.add_widget(Label(text="1. What is the capital of France?"))
        self.q1_a = CheckBox()
        row1 = BoxLayout(padding=[400, 0, 400, 0])
        row1.add_widget(self.q1_a)
        row1.add_widget(Label(text="A. Berlin"))
        self.layout.add_widget(row1)

        self.q1_b = CheckBox()
        row2 = BoxLayout(padding=[400, 0, 400, 0])
        row2.add_widget(self.q1_b)
        row2.add_widget(Label(text="B. London"))
        self.layout.add_widget(row2)

        self.q1_c = CheckBox()
        row3 = BoxLayout(padding=[400, 0, 400, 0])
        row3.add_widget(self.q1_c)
        row3.add_widget(Label(text="C. Paris"))
        self.layout.add_widget(row3)

        self.q1_d = CheckBox()
        row4 = BoxLayout(padding=[400, 0, 400, 0])
        row4.add_widget(self.q1_d)
        row4.add_widget(Label(text="D. Rome"))
        self.layout.add_widget(row4)

        # === Question 2 ===
        self.layout.add_widget(Label(text="2. 2 + 2 = ?"))
        self.q2_a = CheckBox()
        row5 = BoxLayout(padding=[400, 0, 400, 0])
        row5.add_widget(self.q2_a)
        row5.add_widget(Label(text="A. 3"))
        self.layout.add_widget(row5)

        self.q2_b = CheckBox()
        row6 = BoxLayout(padding=[400, 0, 400, 0])
        row6.add_widget(self.q2_b)
        row6.add_widget(Label(text="B. 4"))
        self.layout.add_widget(row6)

        self.q2_c = CheckBox()
        row7 = BoxLayout(padding=[400, 0, 400, 0])
        row7.add_widget(self.q2_c)
        row7.add_widget(Label(text="C. 5"))
        self.layout.add_widget(row7)

        self.q2_d = CheckBox()
        row8 = BoxLayout(padding=[400, 0, 400, 0])
        row8.add_widget(self.q2_d)
        row8.add_widget(Label(text="D. 6"))
        self.layout.add_widget(row8)

        # === Question 3 ===
        self.layout.add_widget(Label(text="3. Python is a ...?"))
        self.q3_a = CheckBox()
        row9 = BoxLayout(padding=[400, 0, 400, 0])
        row9.add_widget(self.q3_a)
        row9.add_widget(Label(text="A. Snake"))
        self.layout.add_widget(row9)

        self.q3_b = CheckBox()
        row10 = BoxLayout(padding=[400, 0, 400, 0])
        row10.add_widget(self.q3_b)
        row10.add_widget(Label(text="B. Car"))
        self.layout.add_widget(row10)

        self.q3_c = CheckBox()
        row11 = BoxLayout(padding=[400, 0, 400, 0])
        row11.add_widget(self.q3_c)
        row11.add_widget(Label(text="C. Programming"))
        self.layout.add_widget(row11)

        self.q3_d = CheckBox()
        row12 = BoxLayout(padding=[400, 0, 400, 0])
        row12.add_widget(self.q3_d)
        row12.add_widget(Label(text="D. Fruit"))
        self.layout.add_widget(row12)

        # === Submit Button ===
        submit_btn = Button(text="Submit", size_hint_y=None, height=50)
        submit_btn.bind(on_press=self.check_answers)
        self.layout.add_widget(submit_btn)

        # === Result ===
        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)

        return self.layout

    def check_answers(self, instance):
        score = 0

        if self.q1_c.active and not (self.q1_a.active or self.q1_b.active or self.q1_d.active):
            score += 1

        if self.q2_b.active and not (self.q2_a.active or self.q2_c.active or self.q2_d.active):
            score += 1

        if self.q3_c.active and not (self.q3_a.active or self.q3_b.active or self.q3_d.active):
            score += 1

        self.result_label.text = f"Your Score: {score}/3"

if __name__ == '__main__':
    QuizApp().run()
