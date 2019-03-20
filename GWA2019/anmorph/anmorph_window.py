from .anmorph_ui import Ui_MainWindow
from .anmorph_model import AnmorphModel
from .QHoverLabel import QHoverLabel
# pylint:disable=no-name-in-module
from PySide2.QtWidgets import QMainWindow, QLabel
from PySide2.QtCore import QItemSelectionModel

class AnmorphWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, data_path):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.model = AnmorphModel(data_path)
        self.currentItem = None

        self.init_buttons()
        self.initialize_labels()
        self.initialize_listview()

    def initialize_labels(self):
        self.lab_target_base.hide()
        self.char_labels = []

        lab_0 = self.create_new_label()
        self.char_labels.append(lab_0)

    def initialize_listview(self):
        self.populate_word_list()
        self.lvw_words.selectionModel().selectionChanged.connect(self.on_word_changed)
        self.on_next_entry()

    def init_buttons(self):
        self.button_groups = {
            self.btn_item1_yes: 1,
            self.btn_item1_na: 1,
            self.btn_item1_no: 1,
            self.btn_item2_yes: 2,
            self.btn_item2_na: 2,
            self.btn_item2_no: 2
        }

        for btn_x in self.button_groups.keys():
            btn_x.clicked.connect(self.on_button_toggle)

        self.btn_na.clicked.connect(self.on_na_button)
        self.btn_prev_entry.clicked.connect(self.on_prev_entry)
        self.btn_next_entry.clicked.connect(self.on_next_entry)

    def on_word_changed(self):
        idx = self.lvw_words.selectedIndexes()[0]
        self.save_note()
        self.update_word_display(idx.row())

    def update_word_display(self, word_idx):
        try:
            item = self.model.item(word_idx)
        except Exception as ex:
            print(ex)
            return

        self.save_responses()        
        self.currentItem = item
        word = item.text()

        self.lab_pos.setText(item.pos)
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

        self.update_response_area()

    def create_new_label(self):
        lab_x = QHoverLabel()
        lab_x.setFont(self.lab_target_base.font())
        lab_x.setAlignment(self.lab_target_base.alignment())
        self.hbox_targets.addWidget(lab_x)
        lab_x.show()
        lab_x.label_clicked.connect(self.on_label_clicked)
        return lab_x

    def update_questions(self):
        item = self.currentItem
        if not self.currentItem: return
        if not item.unit1 or not item.unit2:
            word = item.text()
            item.unit1 = word[-1]
            item.unit2 = word[:-1]

        word = item.text()
        self.lab_question1.setText(f"""<html>
            <span style='font-weight: bolder; font-size: x-large'>
            {word}
            </span>是
            <span style='font-weight: bolder; font-size: x-large'>
            {item.unit1}
            </span>的一種？
            </html>""")
        self.lab_question2.setText(f"""<html>
            <span style='font-weight: bolder; font-size: x-large'>
            {word}
            </span>是
            <span style='font-weight: bolder; font-size: x-large'>
            {item.unit2}
            </span>的一部分？
            </html>""")

    def update_button_states(self):
        item = self.currentItem
        if not self.currentItem: return
        for btn_x, _ in self.button_groups.items():
            btn_x.setStyleSheet("")

        if item.hyper_rule == 1:
            self.btn_item1_yes.click()
        elif item.hyper_rule == 0:
            self.btn_item1_no.click()

        if item.mero_rule == 1:
            self.btn_item2_yes.click()
        elif item.mero_rule == 0:
            self.btn_item2_no.click()

        if item.na_rule == 1:
            self.btn_na.click()
        else:
            self.btn_na.setStyleSheet("")

    def update_note(self):
        item = self.currentItem
        if not self.currentItem: return
        self.line_note.setText(item.note)

    def update_response_area(self):
        self.update_note()
        self.update_questions()
        self.update_button_states()

    def save_note(self):
        item = self.currentItem
        if not self.currentItem: return
        item.note = self.line_note.text()

    def save_responses(self):
        self.model.save_data()
        n_completed = 0
        for item_i in range(self.model.rowCount()):
            idx = self.model.index(item_i, 0)            
            item = self.model.itemFromIndex(idx)
            if item.status == "complete":
                n_completed += 1
        
        self.statusBar().showMessage(f"Entry complete: {n_completed}/{self.model.rowCount()}")
    def on_prev_entry(self):
        try:
            idx = self.lvw_words.selectedIndexes()[0]
            word_idx = idx.row() - 1
            if word_idx < 0:
                word_idx = self.model.rowCount()-1
        except Exception as ex:
            word_idx = self.model.rowCount()-1
            print(ex)

        new_idx = self.model.createIndex(word_idx, 0)
        if new_idx.isValid():
            self.lvw_words.selectionModel().select(new_idx,
                QItemSelectionModel.ClearAndSelect)

    def on_next_entry(self):
        try:
            idx = self.lvw_words.selectedIndexes()[0]
            word_idx = idx.row() + 1
            if not word_idx < self.model.rowCount():
                word_idx = 0
        except Exception as ex:
            word_idx = 0
            print(ex)

        new_idx = self.model.createIndex(word_idx, 0)
        if new_idx.isValid():
            self.lvw_words.selectionModel().select(new_idx,
                QItemSelectionModel.ClearAndSelect)

    def on_button_toggle(self):
        item = self.currentItem
        if not self.currentItem: return

        src_obj = self.sender()
        src_idx = self.button_groups.get(src_obj, -1)
        for btn_x, idx in self.button_groups.items():
            if idx == src_idx:
                btn_x.setStyleSheet("")
        src_obj.setStyleSheet("background-color: yellow")

        btn_name = src_obj.objectName()
        tokens = btn_name.split("_")
        ans_map = {"yes": 1, "no": 0, "na": -1}
        if tokens[1] == "item1":
            item.hyper_rule = ans_map.get(tokens[2], -1)            
        elif tokens[1] == "item2":
            item.mero_rule = ans_map.get(tokens[2], -1)
        else:
            pass        
        self.btn_na.setStyleSheet("")
        item.na_rule = -1

    def on_na_button(self):
        item = self.currentItem
        if not self.currentItem: return
        for btn_x, _ in self.button_groups.items():
            btn_x.setStyleSheet("")
        self.btn_na.setStyleSheet("background-color: yellow")
        self.btn_item1_na.setStyleSheet("background-color: yellow")
        self.btn_item2_na.setStyleSheet("background-color: yellow")
        item.hyper_rule = -1
        item.mero_rule = -1
        item.na_rule = 1    

    def on_label_clicked(self, label_str):
        if not self.currentItem: return
        src_label = self.sender()
        src_idx = self.char_labels.index(src_label)
        if src_idx < 0:
            return

        item = self.currentItem
        word = item.text()
        item.unit1 = word[src_idx]
        item.unit2 = word[:src_idx] + word[src_idx+1:]

        self.update_questions()        

    def populate_word_list(self):
        self.lvw_words.setModel(self.model)
