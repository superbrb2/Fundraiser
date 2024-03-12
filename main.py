from nicegui import ui
import json
import io

TOTAL_PP = 106

class participant():
    def __init__(self,name,amount) -> None:
        self.name = name
        self.total_amount: int = amount
        self.editing = False
        self.new_amount = 0
        
    def set_new_amount(self,e):
        self.new_amount = e
        self.hide_editing()

    def show_editing(self):
        if not self.editing:
            self.editing = True
            with ui.card_section():
                ui.number(label='Amount',on_change=lambda e: self.set_new_amount(e.value))
            with ui.row():
                ui.button('+', on_click=lambda: self.add_amount(self.new_amount)).classes('w-28 text-5xl')
                ui.button('-', on_click=lambda: self.sub_amount(self.new_amount)).classes('w-28 text-5xl')
            
            
    def hide_editing(self):
        self.editing = False

    def add_amount(self,amount):
        self.total_amount += amount
        save_data(self.total_amount, self.name)
        self.hide_editing()
        self.display.refresh()
        
        
    def sub_amount(self, amount):
        self.total_amount -= amount
        save_data(self.total_amount, self.name)
        self.hide_editing()
        self.display.refresh()
        
        
    @ui.refreshable
    def display(self):
        with ui.card().classes('w-80 items-stretch'):
            ui.label(self.name).classes('text-bold text-3xl')
            ui.linear_progress(self.total_amount/TOTAL_PP, show_value=False)
            with ui.card_section():
                ui.label('Amount Raised').classes('text-semibold text-xl')
                ui.label(str(self.total_amount)).classes('text-lg')
            with ui.card_section():
                ui.button('Add amount', on_click=lambda: self.show_editing())
            ui.separator()


def save_data(amount,name):
    data[name] = amount
    with io.open('data.json', 'w') as json_file:
        json.dump(data,json_file)
    
    
with open('data.json') as json_file:
    data = json.load(json_file)
    
brad = participant('Brad',data['Brad'])
emmeline = participant('Emmeline',data['Emmeline'])
tank = participant('Tank',data['Tank'])
ed = participant('Ed',data['Ed'])

with ui.row():
    brad.display()
    emmeline.display()
    tank.display()
    ed.display()
        
ui.run(on_air='')