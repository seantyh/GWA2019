from .anmorph_ui import Ui_MainWindow
from .anmorph_model import AnmorphModel
from .QHoverLabel import QHoverLabel
# pylint:disable=no-name-in-module
from PySide2.QtWidgets import QMainWindow, QLabel

class AnmorphWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)        
        self.model = AnmorphModel()        
        
        self.init_buttons()
        self.initialize_listview()
        self.initialize_labels()
        
    def initialize_labels(self):
        self.lab_target_base.hide()
        self.char_labels = []
        
        lab_0 = self.create_new_label()        
        self.char_labels.append(lab_0)
        for lab_x in self.char_labels:
            pass

    def initialize_listview(self):
        self.populate_word_list()
        self.lvw_words.selectionModel().selectionChanged.connect(self.on_word_changed)
    
    def on_word_changed(self):        
        idx = self.lvw_words.selectedIndexes()[0]                                
        self.update_word_display(idx.row())        

    def update_word_display(self, word_idx): 
        try:
            item = self.model.item(word_idx)
        except Exception as ex:
            print(ex)
            return
        
        word = item.text()
        print(f"{word} selected")
        
        print(self.char_labels)
        for char_i, char_x in enumerate(word):            
            if char_i < len(self.char_labels):
                lab_x = self.char_labels[char_i]
            else:                
                lab_x = self.create_new_label()
                self.char_labels.append(lab_x)            
            lab_x.setText(char_x)                        

        while len(self.char_labels) > len(word):
            lab_x = self.char_labels.pop()
            self.hbox_targets.removeWidget(lab_x)
            lab_x.deleteLater()

    def create_new_label(self):
        lab_x = QHoverLabel()
        lab_x.setFont(self.lab_target_base.font())
        self.hbox_targets.addWidget(lab_x)
        lab_x.show()                
        return lab_x

    def on_hover_target_label(self):
        src_label = self.sender()
        src_label.setStyleSheet("color: blue")

    def init_buttons(self):
        self.button_groups = {
            self.btn_item1_yes: 1, 
            self.btn_item1_no: 1,
            self.btn_item2_yes: 2,
            self.btn_item2_no: 2
        }

        for btn_x in self.button_groups.keys():
            btn_x.clicked.connect(self.on_button_toggle)
        
        self.btn_na.clicked.connect(self.on_button_toggle)
        self.btn_prev_entry.clicked.connect(self.on_prev_entry)
        self.btn_next_entry.clicked.connect(self.on_next_entry)
    
    def on_prev_entry(self):
        print("previous entry")

    def on_next_entry(self):
        print("next entry")

    def on_button_toggle(self):
        src_obj = self.sender()
        src_idx = self.button_groups.get(src_obj, -1)
        for btn_x, idx in self.button_groups.items():
            if idx == src_idx:
                btn_x.setStyleSheet("")
        src_obj.setStyleSheet("background-color: yellow") 

    def populate_word_list(self):
        self.lvw_words.setModel(self.model)
