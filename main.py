from nicegui import ui

TOTAL_PP = 106

class participant():
    def __init__(self,name) -> None:
        self.name = name
        self.total_amount: int = 20
        self.editing = False
        self.new_amount = 0
        
    def set_new_amount(self,e):
        self.new_amount = e
        print(e)

    def show_editing(self):
        if not self.editing:
            self.editing = True
            with ui.card_section():
                ui.number(label='Amount',on_change=lambda e: self.set_new_amount(e.value))
            with ui.row():
                ui.button('+', on_click=lambda: self.add_amount(self.new_amount),color='background-color: rgb(77 124 15);').classes('w-28 text-5xl')
                ui.button('-', on_click=lambda: self.sub_amount(self.new_amount),color='background-color: rgb(127 29 29);').classes('w-28 text-5xl')
            
            
    def hide_editing(self):
        editing = False

    def add_amount(self,amount):
        self.total_amount += amount
        self.display.refresh()
        
    def sub_amount(self, amount):
        self.total_amount -= amount
        self.display.refresh()
        
        
    @ui.refreshable
    def display(self):
        with ui.card().classes('w-80 items-stretch'):
            ui.label('Brad').classes('text-bold text-3xl')
            ui.linear_progress(self.total_amount/TOTAL_PP, show_value=False)
            with ui.card_section():
                ui.label('Amount Raised').classes('text-semibold text-xl')
                ui.label(str(self.total_amount)).classes('text-lg')
            with ui.card_section():
                ui.button('Add amount', on_click=lambda: self.show_editing())
            ui.separator()

brad = participant('Brad')
emmeline = participant('Emmeline')
tank = participant('Tank')
ed = participant('Ed')

with ui.row():
    brad.display()
    emmeline.display()
    tank.display()
    ed.display()
        
ui.run()