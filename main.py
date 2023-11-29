import pickle

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QSpinBox, QTextEdit, QComboBox, \
    QCheckBox, QPushButton, QLineEdit, QLabel
from PyQt5.QtWidgets import QDoubleSpinBox, QMessageBox


import qdarkstyle


class Ui_MainWindow(object):
    def __init__(self):
        self.array_list_areascroll = None

    def setupUi(self, MainWindow):
        # region setup
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1161, 911)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1161, 871))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.button_answer = QtWidgets.QPushButton(self.tab)
        self.button_answer.setGeometry(QtCore.QRect(560, 550, 221, 61))
        self.button_answer.setObjectName("button_answer")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 765, 251, 51))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(830, 10, 301, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.button_add_const_field = QtWidgets.QPushButton(self.tab)
        self.button_add_const_field.setGeometry(QtCore.QRect(20, 10, 211, 61))
        self.button_add_const_field.setObjectName("button_add_const_field")
        self.button_delete_last_field = QtWidgets.QPushButton(self.tab)
        self.button_delete_last_field.setGeometry(QtCore.QRect(570, 10, 211, 61))
        self.button_delete_last_field.setObjectName("button_delete_last_field")
        self.button_delete_solution = QtWidgets.QPushButton(self.tab)
        self.button_delete_solution.setGeometry(QtCore.QRect(990, 40, 31, 31))
        self.button_delete_solution.setObjectName("button_delete_solution")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 740, 251, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.button_add_solution = QtWidgets.QPushButton(self.tab)
        self.button_add_solution.setGeometry(QtCore.QRect(940, 40, 31, 31))
        self.button_add_solution.setObjectName("button_add_solution")
        self.scrollArea_1 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_1.setGeometry(QtCore.QRect(20, 110, 761, 421))
        self.scrollArea_1.setWidgetResizable(True)
        self.scrollArea_1.setObjectName("scrollArea_1")
        self.scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 759, 419))
        self.scrollAreaWidgetContents_1.setObjectName("scrollAreaWidgetContents_1")
        self.scrollArea_1.setWidget(self.scrollAreaWidgetContents_1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(830, 80, 301, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 610, 761, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_2.setGeometry(QtCore.QRect(830, 110, 301, 631))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 299, 629))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(440, 760, 101, 61))
        self.spinBox.setFrame(True)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(2000)
        self.spinBox.setObjectName("spinBox")
        self.button_add_generator_field = QtWidgets.QPushButton(self.tab)
        self.button_add_generator_field.setGeometry(QtCore.QRect(300, 10, 211, 61))
        self.button_add_generator_field.setObjectName("button_add_generator_field")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 80, 761, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.button_save_and_generate = QtWidgets.QPushButton(self.tab)
        self.button_save_and_generate.setGeometry(QtCore.QRect(560, 760, 221, 61))
        self.button_save_and_generate.setObjectName("button_save_and_generate")
        self.button_to_download = QtWidgets.QPushButton(self.tab)
        self.button_to_download.setGeometry(QtCore.QRect(870, 760, 221, 61))
        self.button_to_download.setObjectName("button_to_download")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(20, 640, 761, 101))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(420, 740, 141, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.button_example_text = QtWidgets.QPushButton(self.tab)
        self.button_example_text.setGeometry(QtCore.QRect(20, 550, 211, 61))
        self.button_example_text.setObjectName("button_example_text")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_3.setGeometry(QtCore.QRect(30, 40, 1091, 741))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1089, 739))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_4.setGeometry(QtCore.QRect(30, 40, 1091, 741))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1089, 739))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_5.setGeometry(QtCore.QRect(40, 110, 551, 651))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 549, 649))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.button_delete_const = QtWidgets.QPushButton(self.tab_4)
        self.button_delete_const.setGeometry(QtCore.QRect(330, 60, 31, 31))
        self.button_delete_const.setObjectName("button_delete_const")
        self.button_add_const = QtWidgets.QPushButton(self.tab_4)
        self.button_add_const.setGeometry(QtCore.QRect(270, 60, 31, 31))
        self.button_add_const.setObjectName("button_add_const")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(40, 20, 551, 41))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(750, 50, 261, 101))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.spinBox_answer_index = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_answer_index.setGeometry(QtCore.QRect(830, 170, 101, 71))
        self.spinBox_answer_index.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_answer_index.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_answer_index.setMinimum(100)
        self.spinBox_answer_index.setMaximum(399)
        self.spinBox_answer_index.setObjectName("spinBox_answer_index")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(740, 540, 281, 71))
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1161, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menu_2)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_save_state = QtWidgets.QAction(MainWindow)
        self.action_save_state.setObjectName("action_save_state")
        self.action_load_state = QtWidgets.QAction(MainWindow)
        self.action_load_state.setObjectName("action_load_state")
        self.action_avtor = QtWidgets.QAction(MainWindow)
        self.action_avtor.setObjectName("action_avtor")
        self.action_info_gen = QtWidgets.QAction(MainWindow)
        self.action_info_gen.setObjectName("action_info_gen")
        self.action_info_solution = QtWidgets.QAction(MainWindow)
        self.action_info_solution.setObjectName("action_info_solution")
        self.action_client_instruction = QtWidgets.QAction(MainWindow)
        self.action_client_instruction.setObjectName("action_client_instruction")
        self.action_clean_state = QtWidgets.QAction(MainWindow)
        self.action_clean_state.setObjectName("action_clean_state")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action_save_state)
        self.menu.addAction(self.action_load_state)
        self.menu.addSeparator()
        self.menu.addAction(self.action_clean_state)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_info_gen)
        self.menu_3.addAction(self.action_info_solution)
        self.menu_2.addAction(self.action_client_instruction)
        self.menu_2.addAction(self.menu_3.menuAction())
        self.menu_2.addAction(self.action_avtor)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        # endregion


        #region Хранилище виджетов + данных для задач
        self.comboboxs_generator = []
        self.comboboxs_solution = []
        self.textedits_generator=[]

        self.tabels_generator = []
        self.tabels_solution = []
        self.tabels_const = []

        self.index_values_generator = 100
        self.index_values_solution = 200
        self.index_values_const = 300

        self.global_values_generation_and_solutions = [None] * 400

        self.button_answer.setEnabled(False)
        MainWindow.setFixedSize(1161, 911)
        self.spinBox_answer_index.setValue(200)
        # endregion

        #region setup2
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setWindowIcon(QtGui.QIcon("icon.ico"))
        #endregion
        # mine add

        # region Создаем вертикальный компоновщик для всех scrollArea
        self.vertical_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_1)
        self.vertical_layout.setContentsMargins(5, 5, 5, 5)
        self.vertical_layout.setSpacing(6)
        self.scrollAreaWidgetContents_1.setLayout(self.vertical_layout)

        self.vertical_layout2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.vertical_layout2.setContentsMargins(5, 5, 5, 5)
        self.vertical_layout2.setSpacing(6)
        self.scrollAreaWidgetContents_2.setLayout(self.vertical_layout2)

        self.vertical_layout3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.vertical_layout3.setContentsMargins(5, 5, 5, 5)
        self.vertical_layout3.setSpacing(6)
        self.scrollAreaWidgetContents_3.setLayout(self.vertical_layout3)

        self.vertical_layout4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.vertical_layout4.setContentsMargins(5, 5, 5, 5)
        self.vertical_layout4.setSpacing(6)
        self.scrollAreaWidgetContents_4.setLayout(self.vertical_layout4)

        self.vertical_layout5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.vertical_layout5.setContentsMargins(5, 5, 5, 5)
        self.vertical_layout5.setSpacing(6)
        self.scrollAreaWidgetContents_5.setLayout(self.vertical_layout5)

        #endregion\

        # Всякие события:
        # Кнопки взаимодействия с основной рабочей областью
        self.button_add_const_field.clicked.connect(self.add_text_edit)
        self.button_add_generator_field.clicked.connect(self.add_combobox_generator)
        self.button_delete_last_field.clicked.connect(self.delete_last_combobox_generator)

        # Кнопки взаимодействия с очередью действий решения
        self.button_add_solution.clicked.connect(self.add_combobox_queue_solution)
        self.button_delete_solution.clicked.connect(self.delete_last_combobox_queue_solution)
        # Кнопки генерации примера задачи и ответа к ней
        #self.button_example_text.clicked.connect(lambda: self.show_example_text(True))
        self.button_answer.clicked.connect(lambda: self.show_example_answer(True))

        # Кнопки взаимодействия с константами
        self.button_add_const.clicked.connect(self.add_const)
        self.button_delete_const.clicked.connect(self.delete_const)

        # Кнопка в "Загрузки"
        self.button_to_download.clicked.connect(self.open_download_folder)
        # Кнопка генерации задач
        self.button_save_and_generate.clicked.connect(self.handler_generation_tasks)

        # тест новой фичи
        # self.array_list_areascroll = [self.scrollAreaWidgetContents_1,
        #                               self.scrollAreaWidgetContents_2,
        #                               self.scrollAreaWidgetContents_3,
        #                               self.scrollAreaWidgetContents_4,
        #                               self.scrollAreaWidgetContents_5]

        self.button_example_text.clicked.connect(lambda: self.print_log(self.comboboxs_generator))
        self.button_example_text.clicked.connect(lambda: self.print_log(self.comboboxs_solution))
        self.button_example_text.clicked.connect(lambda: self.print_log(self.textedits_generator))
        self.button_example_text.clicked.connect(lambda: self.print_log(self.tabels_generator))
        self.button_example_text.clicked.connect(lambda: self.print_log(self.tabels_generator))
        self.button_example_text.clicked.connect(lambda: self.print_log(self.tabels_generator))
        self.button_example_text.clicked.connect(lambda: self.print_log(self.tabels_generator))

        self.action_save_state.triggered.connect(self.handler_save_formstate)
        self.action_load_state.triggered.connect(self.load_state)
        self.state_file = "widget_state.pickle"

        self.unique_key_id = 1000

        # Смена tab_index подгрузка констант в массив значений КОСТЫЛЬ придумать как решить !!!!
        self.tabWidget.currentChanged.connect(self.smth_const)



    # region WorkPlace Generation
    generators_dict = {
        'Сгенерировать целое число': [['Индекс'],
                                      ['Название'],
                                      ['Минимальное число', -2147483648, 2147483647],
                                      ['Максимальное число', -2147483648, 2147483647]],

        'Сгенерировать число с плав. точкой': [['Индекс'],
                                               ['Название'],
                                               ['Минимальное число', -2147483648, 2147483647],
                                               ['Максимальное число', -2147483648, 2147483647],
                                               ['Кол-во знаков после запятой (1-6)', 1, 6]],

        'Сгенерировать логическое выражение': [['Индекс'],
                                               ['Название'],
                                               ['Количество неизвестных', 2, 4],
                                               ['Количество переменных', 3, 8],
                                               ['¬', 0, 1],
                                               ['∧', 0, 1],
                                               ['∨', 0, 1],
                                               ['⊕', 0, 1],
                                               ['→', 0, 1],
                                               ['≡', 0, 1],
                                               ],
        'Сгенерировать граф': [['Индекс'],
                               ['Название'],
                               ['Количество вершин', 2, 20],
                               ['Минимальное количество ребер из вершины', 1, 20],
                               ['Максимальное количество ребер из вершины', 2, 20]]
    }

    

    def add_text_edit(self):
        text_edit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_1)
        text_edit.setText("Изменяемое константное поле")
        self.textedits_generator.append(text_edit)
        # Дополнительные настройки для виджета QTextEdit...
        self.vertical_layout.addWidget(text_edit)

    def add_combobox_generator(self):
        # Создаем комбобокс и заполняем его из словаря
        combobox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_1)
        combobox.addItems(self.generators_dict.keys())


        self.comboboxs_generator.append(combobox)
        self.vertical_layout.addWidget(combobox)

        # Создаем таблицу привязанную ко второй вкладке

        table = QTableWidget(self.tab_2)
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setVisible(False)
        combobox_key = combobox.currentText()
        values = self.generators_dict[combobox_key]

        # Устанавливаем размеры таблицы
        table.setRowCount(2)
        table.setColumnCount(len(values))
        # Заполняем ячейки таблицы

        for j in range(len(values)):
            table.setItem(0, j, QTableWidgetItem(values[j][0]))
            tmp_item = table.item(0, j)
            tmp_item.setFlags(tmp_item.flags() & ~Qt.ItemIsEditable)
            if j == 0:
                table.setItem(1, j, QTableWidgetItem(str(self.index_values_generator)))
                tmp_item = table.item(1, j)
                tmp_item.setFlags(tmp_item.flags() & ~Qt.ItemIsEditable)
                continue
            if j == 1:
                table.setItem(1, j, QTableWidgetItem(combobox_key))
                tmp_item = table.item(1, j)
                tmp_item.setFlags(tmp_item.flags() & ~Qt.ItemIsEditable)
                continue
            spinbox = QSpinBox()
            spinbox.setAlignment(QtCore.Qt.AlignCenter)
            spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            spinbox.setMinimum(values[j][1])
            spinbox.setMaximum(values[j][2])

            table.setCellWidget(1, j, spinbox)
        table.resizeColumnsToContents()
        self.vertical_layout3.addWidget(table)

        # Взаимодействие с хранилищем
        self.tabels_generator.append(table)
        self.index_values_generator += 1
        self.event_combobox_generator_changed()

    def delete_last_combobox_generator(self):
        # Получаем список всех виджетов в ScrollArea
        widgets1 = self.scrollAreaWidgetContents_1.layout().parent().children()

        # Проверяем, есть ли виджеты для удаления
        if len(widgets1) > 1:

            # Удаляем последний добавленный виджет
            widget = widgets1[-1]

            if isinstance(widget, QtWidgets.QComboBox):
                self.comboboxs_generator.pop(-1)

                # Удаление последней таблицы
                local_table = self.tabels_generator[-1]
                self.vertical_layout3.removeWidget(local_table)
                # Освобождаем память
                local_table.setParent(None)
                local_table.deleteLater()

                self.tabels_generator.pop(-1)
                self.index_values_generator -= 1

            widget.setParent(None)
            widget.deleteLater()
        self.event_combobox_generator_changed()

    def event_combobox_generator_changed(self):
        def create_handler(index_to_replace_inner):
            def handler():
                self.handle_combobox_generator_change(index_to_replace_inner)

            return handler

        for index_to_replace in range(len(self.comboboxs_generator)):
            tmp = self.comboboxs_generator[index_to_replace]
            handler = create_handler(index_to_replace)
            tmp.currentIndexChanged.connect(handler)

    def handle_combobox_generator_change(self, index_table_to_replace_inner):

        new_table = QTableWidget(self.tab_2)
        new_table.verticalHeader().setVisible(False)
        new_table.horizontalHeader().setVisible(False)
        combobox_key = self.comboboxs_generator[index_table_to_replace_inner].currentText()
        values = self.generators_dict[combobox_key]

        # Устанавливаем размеры таблицы
        new_table.setRowCount(2)
        new_table.setColumnCount(len(values))
        # Заполняем ячейки таблицы

        for j in range(len(values)):
            new_table.setItem(0, j, QTableWidgetItem(values[j][0]))
            tmp_item = new_table.item(0, j)
            tmp_item.setFlags(tmp_item.flags() & ~Qt.ItemIsEditable)
            if j == 0:
                new_table.setItem(1, j, QTableWidgetItem(str(100 + int(index_table_to_replace_inner))))
                tmp_item = new_table.item(1, j)
                tmp_item.setFlags(tmp_item.flags() & ~Qt.ItemIsEditable)
                continue
            if j == 1:
                new_table.setItem(1, j, QTableWidgetItem(combobox_key))
                tmp_item = new_table.item(1, j)
                tmp_item.setFlags(tmp_item.flags() & ~Qt.ItemIsEditable)
                continue
            spinbox = QSpinBox()
            spinbox.setAlignment(QtCore.Qt.AlignCenter)
            spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            spinbox.setMinimum(values[j][1])
            spinbox.setMaximum(values[j][2])

            new_table.setCellWidget(1, j, spinbox)

        new_table.resizeColumnsToContents()

        old_table = self.tabels_generator[index_table_to_replace_inner]
        self.vertical_layout3.replaceWidget(old_table, new_table)
        self.tabels_generator[index_table_to_replace_inner] = new_table
        old_table.setParent(None)

    def smth_generator(self, index, table_generate_index):
        try:
            # Получение списка таблиц из ScrollArea3
            table_widgets_scrollArea_3 = []
            for widget in self.scrollAreaWidgetContents_3.findChildren(QWidget):
                if isinstance(widget, QTableWidget):
                    table_widgets_scrollArea_3.append(widget)
            # Получение глобального индекса таблицы
            tmp_table = table_widgets_scrollArea_3[table_generate_index]
            tmp_value = tmp_table.item(1, 0)
            index_value_generator = int(tmp_value.text())

            # получение значений spinboxов из таблицы по индексу
            values_spinbox = []
            for row in range(table_widgets_scrollArea_3[table_generate_index].rowCount()):
                for column in range(table_widgets_scrollArea_3[table_generate_index].columnCount()):
                    cell_widget = table_widgets_scrollArea_3[table_generate_index].cellWidget(row, column)
                    if isinstance(cell_widget, QSpinBox):
                        values_spinbox.append(cell_widget.value())

            match index:
                case 0:
                    tmp_value = Combinatorics.number_generation(min_number=values_spinbox[0],
                                                                max_number=values_spinbox[1])
                    self.global_values_generation_and_solutions[index_value_generator] = tmp_value
                    return tmp_value

                case 1:
                    tmp_value = Combinatorics.float_number_generation(min_number=values_spinbox[0],
                                                                      max_number=values_spinbox[1],
                                                                      round_inner=values_spinbox[2])
                    self.global_values_generation_and_solutions[index_value_generator] = tmp_value
                    return tmp_value

                case 2:
                    tmp_value = AlgebraOfLogic.generate_right_expression(number_of_unknowns=values_spinbox[0],
                                                                         counter_of_variables=values_spinbox[1],
                                                                         flag_array=values_spinbox[2:])
                    self.global_values_generation_and_solutions[index_value_generator] = tmp_value
                    return tmp_value

                case 3:
                    tmp_value = Graph()
                    tmp_value.graph_generator(number_of_nodes=values_spinbox[0],
                                              min_number_of_edge_from_node=values_spinbox[1],
                                              max_number_of_edge_from_node=values_spinbox[2])
                    self.global_values_generation_and_solutions[index_value_generator] = tmp_value
                    return tmp_value.graph
                case _:
                    return
        except My_exceptions.Min_max_error as e:
            self.show_popup_critical("Ошибка", str(e) + "\n")

        except My_exceptions.algebra_logic_error as e:
            self.show_popup_critical("Ошибка", str(e) + "\n")

        except My_exceptions.algebra_logic_only_denial_error as e:
            self.show_popup_critical("Ошибка", str(e) + "\n")

        except Exception:
            self.show_popup_critical("Ошибка",
                                     "Неизвестная ошибка, попробуйте перепроверить введенные параметры генерации\n")

    # endregion WorkPlace Generation
    # region WorkPlace Solution Queue
    solution_dict = {
        "Сложение": [['Индекс'],
                     ['Название'],
                     ["Слагаемое 1"],
                     ["Слагаемое 2"]],

        "Вычитание": [['Индекс'],
                      ['Название'],
                      ["Уменьшаемое"],
                      ["Вычитаемое"]],

        "Умножение": [['Индекс'],
                      ['Название'],
                      ["Множитель 1"],
                      ["Множитель 2"]],

        "Деление": [['Индекс'],
                    ['Название'],
                    ["Делимое"],
                    ["Делитель"]],

        "Возведение в степень": [['Индекс'],
                                 ['Название'],
                                 ["Основание"],
                                 ["Показатель"]],

        "Факториал": [['Индекс'],
                      ['Название'],
                      ["Число"]],

        "Формула сочетаний (C)": [['Индекс'],
                                  ['Название'],
                                  ["n"],
                                  ["k"]],

        "Формула размещений (P)": [['Индекс'],
                                   ['Название'],
                                   ["n"],
                                   ["k"]],

        "Подсчет 0/1 в таблице истинности": [['Индекс'],
                                             ['Название'],
                                             ["Логическое выражение"],
                                             ["Подсчет 0 или 1 (Не индекс)", 0, 1]],

        "Макс поток": [['Индекс'],
                       ['Название'],
                       ["Граф"]],

        "Кратчайщее расстояние до вершин (Дейкстра)": [['Индекс'],
                                                       ['Название'],
                                                       ['Граф']]
    }

    def add_combobox_queue_solution(self):
        combobox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        combobox.addItems(self.solution_dict.keys())
        self.comboboxs_solution.append(combobox)
        self.vertical_layout2.addWidget(combobox)

        # Создаем таблицу привязанную к третьей вкладке

        table = QTableWidget(self.tab_3)
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setVisible(False)
        combobox_key = combobox.currentText()
        values = self.solution_dict[combobox_key]

        # Устанавливаем размеры таблицы
        table.setRowCount(2)
        table.setColumnCount(len(values))
        # Заполняем ячейки таблицы

        for j in range(len(values)):
            table.setItem(0, j, QTableWidgetItem(values[j][0]))
            tmp_item = table.item(0, j)
            tmp_item.setFlags(tmp_item.flags() & ~Qt.ItemIsEditable)
            if j == 0:
                table.setItem(1, j, QTableWidgetItem(str(self.index_values_solution)))
                tmp_item = table.item(1, j)
                tmp_item.setFlags(tmp_item.flags() & ~Qt.ItemIsEditable)
                continue
            if j == 1:
                table.setItem(1, j, QTableWidgetItem(combobox_key))
                tmp_item = table.item(1, j)
                tmp_item.setFlags(tmp_item.flags() & ~Qt.ItemIsEditable)
                continue
            spinbox = QSpinBox()
            spinbox.setAlignment(QtCore.Qt.AlignCenter)
            spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            spinbox.setMinimum(100)
            spinbox.setMaximum(399)
            table.setCellWidget(1, j, spinbox)

        table.resizeColumnsToContents()
        self.vertical_layout4.addWidget(table)

        # Взаимодействие с хранилищем
        self.tabels_solution.append(table)
        self.index_values_solution += 1
        self.event_combobox_solution_changed()

    def delete_last_combobox_queue_solution(self):
        # Получаем список всех виджетов в ScrollArea
        widgets = self.scrollAreaWidgetContents_2.layout().parent().children()

        # Проверяем, есть ли виджеты для удаления
        if len(widgets) > 1:
            widget = widgets[-1]

            if isinstance(widget, QtWidgets.QComboBox):
                self.comboboxs_solution.pop(-1)

                # Удаление последней таблицы
                local_table = self.tabels_solution[-1]
                self.vertical_layout4.removeWidget(local_table)
                # Освобождаем память
                local_table.setParent(None)
                local_table.deleteLater()

                self.tabels_solution.pop(-1)
                self.index_values_solution -= 1
            # Удаляем последний добавленный виджет
            widget.setParent(None)
            widget.deleteLater()

    def event_combobox_solution_changed(self):
        def create_handler(index):
            def handler():
                self.handle_combobox_solution_change(index)

            return handler

        for index_to_replace in range(len(self.comboboxs_solution)):
            tmp = self.comboboxs_solution[index_to_replace]
            handler = create_handler(index_to_replace)
            tmp.currentIndexChanged.connect(handler)

    def handle_combobox_solution_change(self, index_table_to_replace_inner):
        new_table = QTableWidget(self.tab_3)
        new_table.verticalHeader().setVisible(False)
        new_table.horizontalHeader().setVisible(False)
        combobox_key = self.comboboxs_solution[index_table_to_replace_inner].currentText()
        values = self.solution_dict[combobox_key]

        # Устанавливаем размеры таблицы
        new_table.setRowCount(2)
        new_table.setColumnCount(len(values))

        # Заполняем ячейки таблицы
        for j in range(len(values)):
            new_table.setItem(0, j, QTableWidgetItem(values[j][0]))
            tmp_item = new_table.item(0, j)
            tmp_item.setFlags(tmp_item.flags() & ~Qt.ItemIsEditable)
            if j == 0:
                new_table.setItem(1, j, QTableWidgetItem(str(200 + int(index_table_to_replace_inner))))
                tmp_item = new_table.item(1, j)
                tmp_item.setFlags(tmp_item.flags() & ~Qt.ItemIsEditable)
                continue
            if j == 1:
                new_table.setItem(1, j, QTableWidgetItem(combobox_key))
                tmp_item = new_table.item(1, j)
                tmp_item.setFlags(tmp_item.flags() & ~Qt.ItemIsEditable)
                continue
            spinbox = QSpinBox()
            spinbox.setAlignment(QtCore.Qt.AlignCenter)
            spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            spinbox.setMinimum(100)
            spinbox.setMaximum(399)
            if len(values[j]) == 3:
                spinbox.setMinimum(values[j][1])
                spinbox.setMaximum(values[j][2])

            new_table.setCellWidget(1, j, spinbox)
        new_table.resizeColumnsToContents()

        old_table = self.tabels_solution[index_table_to_replace_inner]
        self.vertical_layout4.replaceWidget(old_table, new_table)
        self.tabels_solution[index_table_to_replace_inner] = new_table
        old_table.setParent(None)

    def smth_solution(self, index_combobox, table_solution_index):
        try:
            # Получение списка таблиц из ScrollArea4
            table_widgets_scrollArea_4 = []
            for widget in self.scrollAreaWidgetContents_4.findChildren(QWidget):
                if isinstance(widget, QTableWidget):
                    table_widgets_scrollArea_4.append(widget)

            # Проверка наличия таблицы по индексу
            if table_solution_index >= len(table_widgets_scrollArea_4):
                raise IndexError("Индекс таблицы выходит за пределы доступных значений")

            # index_value_generator = table_widgets_scrollArea_3[table_generate_index].item(1, 0)
            # Получение глобального индекса таблицы
            tmp_table = table_widgets_scrollArea_4[table_solution_index]
            tmp_value = tmp_table.item(1, 0)
            index_value_solution_queue = int(tmp_value.text())

            # получение значений spinboxов из таблицы по индексу
            values_spinbox = []
            for row in range(table_widgets_scrollArea_4[table_solution_index].rowCount()):
                for column in range(table_widgets_scrollArea_4[table_solution_index].columnCount()):
                    cell_widget = table_widgets_scrollArea_4[table_solution_index].cellWidget(row, column)
                    if isinstance(cell_widget, QSpinBox):
                        values_spinbox.append(cell_widget.value())

            match index_combobox:
                case 0:
                    tmp_value = Operations.sum(self.global_values_generation_and_solutions[values_spinbox[0]],
                                               self.global_values_generation_and_solutions[values_spinbox[1]])
                    self.global_values_generation_and_solutions[index_value_solution_queue] = tmp_value
                    return tmp_value
                case 1:
                    tmp_value = Operations.subtraction(self.global_values_generation_and_solutions[values_spinbox[0]],
                                                       self.global_values_generation_and_solutions[values_spinbox[1]])
                    self.global_values_generation_and_solutions[index_value_solution_queue] = tmp_value
                    return tmp_value
                case 2:
                    tmp_value = Operations.multiplication(
                        self.global_values_generation_and_solutions[values_spinbox[0]],
                        self.global_values_generation_and_solutions[values_spinbox[1]])
                    self.global_values_generation_and_solutions[index_value_solution_queue] = tmp_value
                    return tmp_value

                case 3:
                    tmp_value = Operations.division(self.global_values_generation_and_solutions[values_spinbox[0]],
                                                    self.global_values_generation_and_solutions[values_spinbox[1]])
                    self.global_values_generation_and_solutions[index_value_solution_queue] = tmp_value
                    return tmp_value

                case 4:
                    tmp_value = Operations.exponentiation(
                        self.global_values_generation_and_solutions[values_spinbox[0]],
                        self.global_values_generation_and_solutions[values_spinbox[1]])
                    self.global_values_generation_and_solutions[index_value_solution_queue] = tmp_value
                    return tmp_value

                case 5:
                    tmp_value = Operations.factorial(self.global_values_generation_and_solutions[values_spinbox[0]])
                    self.global_values_generation_and_solutions[index_value_solution_queue] = tmp_value
                    return tmp_value

                case 6:
                    tmp_value = Combinatorics.C(self.global_values_generation_and_solutions[values_spinbox[1]],
                                                self.global_values_generation_and_solutions[values_spinbox[0]])
                    self.global_values_generation_and_solutions[index_value_solution_queue] = tmp_value
                    return tmp_value

                case 7:
                    tmp_value = Combinatorics.P(self.global_values_generation_and_solutions[values_spinbox[1]],
                                                self.global_values_generation_and_solutions[values_spinbox[0]])
                    self.global_values_generation_and_solutions[index_value_solution_queue] = tmp_value
                    return tmp_value

                case 8:
                    tmp_value = AlgebraOfLogic().convert_to_bool_expression(
                        self.global_values_generation_and_solutions[values_spinbox[0]],
                        bool(values_spinbox[1]))
                    self.global_values_generation_and_solutions[index_value_solution_queue] = tmp_value
                    return tmp_value

                case 9:
                    tmp_value = Graph.solution_task_max_flow(
                        self.global_values_generation_and_solutions[values_spinbox[0]])
                    self.global_values_generation_and_solutions[index_value_solution_queue] = tmp_value
                    return tmp_value
                case 10:
                    tmp_value = Graph.dijkstra(self.global_values_generation_and_solutions[values_spinbox[0]])
                    self.global_values_generation_and_solutions[index_value_solution_queue] = tmp_value
                    return tmp_value

                case _:
                    return

        except IndexError:
            self.show_popup_critical("Ошибка", "Ошибка индекса таблицы\n")

        except My_exceptions.Is_not_graph_error as e:
            self.show_popup_critical("Ошибка", str(e) + "\n")

        except My_exceptions.Is_not_AL_expression_error as e:
            self.show_popup_critical("Ошибка", str(e) + "\n")

        except My_exceptions.Factorial_error as e:
            self.show_popup_critical("Ошибка", str(e) + "\n")

        except My_exceptions.combinatoric_n_k_error as e:
            self.show_popup_critical("Ошибка", str(e) + "\n")

        except ZeroDivisionError:
            self.show_popup_critical("Ошибка", "Деление на ноль недопустимо\n")

        except OverflowError:
            self.show_popup_critical("Ошибка", "Результат одного из действий,\n привел к очень большим числам\n")

        except ValueError:
            self.show_popup_critical("Ошибка", "Вычислительная ошибка\n")

        except Exception:
            self.show_popup_critical("Ошибка", "Неизвестная ошибка, попробуйте перепроверить введенные параметры\n")

    # endregion WorkPlace Solution Queue
    # regionWorkPlace Constregion
    def add_const(self):
        tmp_dict = {
            "Название константы": [['Индекс'],
                                   ['Название'],
                                   ["Значение", -2147483648.0, 2147483647.0]]}
        # Создаем таблицу
        table = QTableWidget(self.tab_4)
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setVisible(False)
        combobox_key = "Название константы"
        values = tmp_dict[combobox_key]

        # Устанавливаем размеры таблицы
        table.setRowCount(2)
        table.setColumnCount(len(values))
        self.tabels_const.append(table)
        # Заполняем ячейки таблицы

        for j in range(len(values)):
            table.setItem(0, j, QTableWidgetItem(values[j][0]))
            tmp_item = table.item(0, j)
            tmp_item.setFlags(tmp_item.flags() & ~Qt.ItemIsEditable)
            if j == 0:
                table.setItem(1, j, QTableWidgetItem(str(self.index_values_const)))
                tmp_item = table.item(1, j)
                tmp_item.setFlags(tmp_item.flags() & ~Qt.ItemIsEditable)
                continue
            if j == 1:
                table.setItem(1, j, QTableWidgetItem(combobox_key))
                continue
            double_spinbox = QDoubleSpinBox()
            double_spinbox.setAlignment(Qt.AlignCenter)
            double_spinbox.setButtonSymbols(QDoubleSpinBox.NoButtons)

            # Тут могла быть ваша реклама
            # double_spinbox.setMinimum(float("-1.79769e+308"))
            # double_spinbox.setMaximum(float("+1.79769e+308"))

            double_spinbox.setMinimum(float(values[j][1]))
            double_spinbox.setMaximum(float(values[j][2]))
            double_spinbox.setValue(float(0))
            double_spinbox.setDecimals(2)

            table.setCellWidget(1, j, double_spinbox)
        table.resizeColumnsToContents()
        self.vertical_layout5.addWidget(table)
        self.index_values_const += 1

    def delete_const(self):
        # Получаем список всех виджетов в ScrollArea
        widgets = self.scrollAreaWidgetContents_5.layout().parent().children()

        # Проверяем, есть ли виджеты для удаления
        if len(widgets) > 1:
            # Удаляем последний добавленный виджет
            widget = widgets[-1]

            widget.setParent(None)
            widget.deleteLater()
            # Удаляем последний добавленный виджет
            self.tabels_const.pop(-1)
            self.index_values_const -= 1

    def smth_const(self):
        # Получение списка таблиц из ScrollArea4
        table_widgets_scrollArea_5 = []
        for widget in self.scrollAreaWidgetContents_5.findChildren(QWidget):
            if isinstance(widget, QTableWidget):
                table_widgets_scrollArea_5.append(widget)

        for table_index_const_locale in range(len(table_widgets_scrollArea_5)):
            # Получение глобального индекса таблицы
            tmp_table = table_widgets_scrollArea_5[table_index_const_locale]
            tmp_value = tmp_table.item(1, 0)
            index_value_const = int(tmp_value.text())

            # получение значений spinboxов из таблицы по индексу
            values_spinbox = []
            for row in range(table_widgets_scrollArea_5[table_index_const_locale].rowCount()):
                for column in range(table_widgets_scrollArea_5[table_index_const_locale].columnCount()):
                    cell_widget = table_widgets_scrollArea_5[table_index_const_locale].cellWidget(row, column)
                    if isinstance(cell_widget, QSpinBox) or isinstance(cell_widget, QDoubleSpinBox):
                        values_spinbox.append(cell_widget.value())

            self.global_values_generation_and_solutions[index_value_const] = values_spinbox[0]

    # endregion WorkPlace Constregion
    # region Workplace example task
    # Получаем текст задания
    def show_example_text(self, choice):
        result_string = "::Вопрос :: "
        widgets = self.scrollAreaWidgetContents_1.findChildren(QWidget)

        j = 0
        for widget in widgets:
            # Проверка, является ли виджет экземпляром QTextEdit
            if isinstance(widget, QTextEdit):
                result_string += widget.toPlainText()
                result_string += " "

            # Проверка, является ли виджет экземпляром QComboBox
            if isinstance(widget, QComboBox):
                result_string += str(self.smth_generator(widget.currentIndex(), j))
                result_string += " "
                j += 1

        self.button_answer.setEnabled(True)
        if choice:

            self.textEdit.setText(result_string)
        else:
            return result_string

    # Подсчет ответа
    def show_example_answer(self, choice):
        self.start_queue_solution()
        result_string = "{="
        result_string += str(self.global_values_generation_and_solutions[self.spinBox_answer_index.value()])
        result_string += "}"

        if choice:
            self.textEdit_2.setText(result_string)
            self.button_answer.setEnabled(False)
        else:
            return result_string

    # Подсчет ответа
    def start_queue_solution(self):
        widgets = self.scrollAreaWidgetContents_2.findChildren(QWidget)

        j = 0
        for widget in widgets:
            # Проверка, является ли виджет экземпляром QComboBox
            if isinstance(widget, QComboBox):
                self.smth_solution(widget.currentIndex(), j)
                j += 1

    # endregion Workplace example task
    # region Workplace save tasks
    # Кнопка в загрузки
    @staticmethod
    def open_download_folder():
        download_folder = os.path.expanduser("~\Downloads")

        if sys.platform == "win32":
            # Если мы находимся на Windows, используем команду "explorer"
            os.system(f'explorer "{download_folder}"')
        else:
            # Для других операционных систем открываем папку загрузки в файловом менеджере
            os.system(f'xdg-open "{download_folder}"')

    def handler_generation_tasks(self):
        count_task = self.spinBox.value()
        array_task = []
        for i in range(count_task):
            result_string = self.show_example_text(False)
            result_string += self.show_example_answer(False)
            result_string = result_string.replace("::Вопрос ::", "::Вопрос " + str(i + 1) + "::")
            array_task.append(result_string)
        self.create_txt_file(array_task, "Your_tasks", "")

    def create_txt_file(self, mas_line, name_file, directory_file):
        # Получаем путь к папке "Загрузки" на текущей операционной системе
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        # Создаем полный путь к папке
        folder_path = os.path.join(downloads_path, "folder_tasks", directory_file)
        # Создаем папку, если она не существует
        os.makedirs(folder_path, exist_ok=True)
        # Создаем полный путь к файлу
        file_path = os.path.join(folder_path, name_file + "0.txt")
        counter_file_in_directory = 0
        while True:
            counter_file_in_directory += 1
            if os.path.exists(file_path):
                # print("Файл существует")
                file_path = os.path.join(folder_path, name_file + " " + str(counter_file_in_directory) + ".txt")
            else:
                # print("Файл не существует")
                break

        # Записываем данные в файл
        with open(file_path, 'w', encoding="utf-8") as file:
            for line in mas_line:
                file.write(line + "\n\n")
        self.show_popup_information("Генерация задач",
                                    "Файл:" + name_file + " " + str(counter_file_in_directory - 1)
                                    + ".txt успешно сохранен, проверьте папку загрузки")

    # endregion Workplace save tasks
    # region Workplace MessageBox
    @staticmethod
    def show_popup_information(messagebox_title_inner: str, content_text_inner: str):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setText(content_text_inner)
        message_box.setWindowTitle(messagebox_title_inner)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.setDefaultButton(QMessageBox.Ok)

        message_box.exec_()

    @staticmethod
    def show_popup_warning(messagebox_title_inner: str, content_text_inner: str):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setText(content_text_inner)
        message_box.setWindowTitle(messagebox_title_inner)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.setDefaultButton(QMessageBox.Ok)

        message_box.exec_()

    @staticmethod
    def show_popup_critical(messagebox_title_inner: str, content_text_inner: str):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Critical)
        message_box.setText(content_text_inner)
        message_box.setWindowTitle(messagebox_title_inner)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.setDefaultButton(QMessageBox.Ok)

        message_box.exec_()

    # endregion Workplace MessageBox


    def print_log(self,widget_list):

        print("============================================")
        print(widget_list.__name__)
        for widget in widget_list:
            print(widget)

        print("============================================")








    # region feature/save_load_pickle

    def handler_save_formstate(self):
        """
        Функция запуска сохранения пресета (состояния формы)
        :return:
        """
        # Пример использования:
        widget_list = []
        widget_list.extend(self.comboboxs_generator) # Все комбобоксы генерации
        widget_list.extend(self.comboboxs_solution)  # Все комбобоксы порядка решения
        widget_list.extend(self.textedits_generator) # все
        widget_list.extend(self.tabels_solution)
        widget_list.extend(self.tabels_generator)
        widget_list.extend(self.tabels_const)
        widget_list.append(self.spinBox_answer_index)

        flat_widget_list = self.flatten_widget_list(widget_list)

        # Обработка таблиц и извлечение детей из них
        for i, widget in enumerate(flat_widget_list):
            if isinstance(widget, QTableWidget):
                children = self.extract_widgets(widget)
                if children is not None:
                    flat_widget_list.extend(children)


        filtered_widget_list=[widget for widget in flat_widget_list if not isinstance(widget, QTableWidget)]

        # name tables
        for widget in filtered_widget_list:
            tmp = self.dynamic_named_widgets(widget)
            widget.setObjectName(tmp)
            print(tmp)



        self.save_state(filtered_widget_list)
    def dynamic_named_widgets(self, widget_inner):
        """
        function -> get name for widget
        
        :param widget_inner:  any widget from pyqt5 
        :return:  str -> unique_name for widget
        """
        tmp_string = f"_{self.unique_key_id}"
        self.unique_key_id += 1
        return f"{str(type(widget_inner).__name__)}{tmp_string}"
    def extract_widgets(self,table):
        """
        Высокоуровневую таблицу  приводит к низкоуровневым виджетам
        
        :param table:  входная таблица размерами 2*n 
        :return:  список виджетов хранящихся во второй строке таблицы
        """
        second_row_widgets = []

        for column in range(table.columnCount()):
            item = table.cellWidget(1, column)
            if item:
                second_row_widgets.append(item)

        for widget in second_row_widgets:
            if isinstance(widget, QLabel):
                print('Label:', widget.text())
            elif isinstance(widget, QLineEdit):
                print('LineEdit:', widget.text())
            elif isinstance(widget, QComboBox):
                print('ComboBox:', widget.currentText())
            elif isinstance(widget, QPushButton):
                print('Button: Clicked!')
            elif isinstance(widget, QDoubleSpinBox):
                print('doubleSpinBox: ', widget.value())
            elif isinstance(widget, QSpinBox):
                print('SpinBox: ', widget.value())
        return second_row_widgets

    def flatten_widget_list(self,widget_list):
        """
        упрощает многомерный список до одномерного
        [[][][]] -> []
        :param widget_list:  многомерный список виджетов
        :return:  одномерный список виджетов
        """
        flat_list = []
        for widget in widget_list:
            if isinstance(widget, list):
                flat_list.extend(self.flatten_widget_list(widget))
            else:
                flat_list.append(widget)
        return flat_list

    def save_state(self, widget_list):
        """
        Сериализует и сохраняет данные в рабочей директории с расширением *.pickle
        :return: 
        """
        state = {}
        self.save_widget_state(widget_list, state)
        with open(self.state_file, 'wb') as file:
            pickle.dump(state, file)
            self.show_popup_information("успех", "успешно сохранено")

    def save_widget_state(self, widget, state):
        """
        Реализация сериализации данных
        :param widget:  виджет
        :param state:   словарь куда идет запись состояние
        :return: обновленный словарь
        """
        if isinstance(widget, QComboBox):
            state[widget.objectName()] = widget.currentIndex()

        elif isinstance(widget, QCheckBox):
            state[widget.objectName()] = widget.isChecked()

        elif isinstance(widget, QDoubleSpinBox):
            state[widget.objectName()] = widget.value()

        elif isinstance(widget, QSpinBox):
            state[widget.objectName()] = widget.value()

        elif isinstance(widget, QTextEdit):
            state[widget.objectName()] = widget.toPlainText()

    #region черновик загрузки данных
    def load_state(self):
        """

        :return:
        """
        try:
            with open(self.state_file, 'rb') as file:
                saved_state = pickle.load(file)
                self.restore_widget_state(saved_state)
                self.show_popup_information("успех", "успешно загружено")
        except FileNotFoundError:
            print(f"Файл {self.state_file} не найден.")
        except Exception as e:
            print(f"Произошла ошибка при загрузке файла {self.state_file}: {e}")

    def restore_widget_state(self, saved_state):
        for widget_name, value in saved_state.items():
            widget = self.findChild((QComboBox, QCheckBox, QDoubleSpinBox, QSpinBox, QTextEdit), widget_name)
            if widget is not None:
                self.set_widget_state(widget, value)

    def set_widget_state(self, widget, value):
        if isinstance(widget, QComboBox):
            widget.setCurrentIndex(value)
        elif isinstance(widget, QCheckBox):
            widget.setChecked(value)
        elif isinstance(widget, QDoubleSpinBox):
            widget.setValue(value)
        elif isinstance(widget, QSpinBox):
            widget.setValue(value)
        elif isinstance(widget, QTextEdit):
            widget.setPlainText(value)
        #TODO добавить другие условия для других типов виджетов

    # endregion
    # endregion



    # def load_state(self, widget_list):
    #     """
    #     Загружает  данные из рабочей директории, а именно из файла с расширением *.pickle
    #     Загрузка пресета
    #     :return:
    #     """
    #     try:
    #         with open(self.state_file, 'rb') as file:
    #             state = pickle.load(file)
    #         self.load_widget_state(widget_list, state)
    #     except FileNotFoundError:
    #         self.show_popup_critical("Безуспешный поиск","Файл состояния не найден.")
    #
    # def load_widget_state(self, widget, state):
    #     if widget.objectName() in state:
    #         if isinstance(widget, QComboBox):
    #             widget.setCurrentIndex(state[widget.objectName()])
    #         elif isinstance(widget, QCheckBox):
    #             widget.setChecked(state[widget.objectName()])
    #         elif isinstance(widget, QSpinBox):
    #             widget.setValue(state[widget.objectName()])
    #         elif isinstance(widget, QDoubleSpinBox):
    #             widget.setValue(state[widget.objectName()])
    #         elif isinstance(widget, QTextEdit):
    #             widget.setPlainText(state[widget.objectName()])
    #
    #     # Рекурсивно обходите детей виджета
    #     for child_widget in widget.findChildren(QWidget, Qt.FindDirectChildrenOnly):
    #         self.load_widget_state(child_widget, state)

    # endregion
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Universal generator 0.1v"))
        self.button_answer.setText(_translate("MainWindow", "Подсчитать ответ"))
        self.label_6.setText(_translate("MainWindow", "Добавить/удалить действие"))
        self.button_add_const_field.setText(_translate("MainWindow", "Добавить константное поле"))
        self.button_delete_last_field.setText(_translate("MainWindow", "Удалить последнее поле"))
        self.button_delete_solution.setText(_translate("MainWindow", "-"))
        self.label_4.setText(_translate("MainWindow", "Ответ"))
        self.button_add_solution.setText(_translate("MainWindow", "+"))
        self.label_2.setText(_translate("MainWindow", "Порядок решения"))
        self.label_3.setText(_translate("MainWindow", "Пример задачи"))
        self.button_add_generator_field.setText(_translate("MainWindow", "Добавить поле для генерации"))
        self.label.setText(_translate("MainWindow", "Поле для создания задачи"))
        self.button_save_and_generate.setText(_translate("MainWindow", "Сохранить и сгенерировать"))
        self.button_to_download.setText(_translate("MainWindow", "Перейти в папку Download"))
        self.label_5.setText(_translate("MainWindow", "Количество задач"))
        self.button_example_text.setText(_translate("MainWindow", "Показать текст задачи"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  _translate("MainWindow", "Основная рабочая область"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Настройка генераций"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Настройка решений"))
        self.button_delete_const.setText(_translate("MainWindow", "-"))
        self.button_add_const.setText(_translate("MainWindow", "+"))
        self.label_7.setText(_translate("MainWindow", "Добавить/удалить константу"))
        self.label_8.setText(_translate("MainWindow", "Укажите индекс в котором хранится ответ"))
        self.label_9.setText(_translate("MainWindow", "Выполнено студентами ТюмГУ МОиАИС"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4),
                                  _translate("MainWindow", "Настройка констант и ответа"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Справка"))
        self.menu_3.setTitle(_translate("MainWindow", "Методический материал"))
        self.action_save_state.setText(_translate("MainWindow", "Сохранить"))
        self.action_load_state.setText(_translate("MainWindow", "Загрузить"))
        self.action_avtor.setText(_translate("MainWindow", "Авторы"))
        self.action_info_gen.setText(_translate("MainWindow", "О генерации"))
        self.action_info_solution.setText(_translate("MainWindow", "О решениях"))
        self.action_client_instruction.setText(_translate("MainWindow", "Инструкция пользования"))
        self.action_clean_state.setText(_translate("MainWindow", "Очистить"))
        self.action_2.setText(_translate("MainWindow", "Сохранить как..."))

        # regionWorkplace ToolTips
        self.button_answer.setToolTip(
            _translate("MainWindow", "Вычисляет ответ к сгенерированной задаче и выводит его в поле \"Ответ\""))
        self.textEdit_2.setToolTip(
            _translate("MainWindow", "Здесь отображается ответ к сгенерированному примеру задачи"))
        self.button_add_const_field.setToolTip(
            _translate("MainWindow", "Добавляет поле с постоянным для каждой задачи текстом"))
        self.button_delete_last_field.setToolTip(
            _translate("MainWindow", "Удаляет последнее созданное в конструкторе поле"))
        self.button_delete_solution.setToolTip(
            _translate("MainWindow", "Удаляет последнее созданное в порядке решения действие"))
        self.button_add_solution.setToolTip(_translate("MainWindow",
                                                       "Добавляет в порядок решения настраиваемое действие (для указания переменных, используемых в решении, перейдите во вкладку \"Настройка решений\")"))
        self.scrollArea_1.setToolTip(_translate("MainWindow",
                                                "Здесь отображается модель задачи, содержащая статические поля (с неизменным при генерации задачи текстом) и динамические поля (с изменяемыми значениями)"))
        self.scrollArea_2.setToolTip(
            _translate("MainWindow", "Здесь отображается  методы решения для каждой из задач в порядке их выполнения"))
        self.spinBox.setToolTip(
            _translate("MainWindow", "Количество задач, которое необходимо сгенерировать по шаблону"))
        self.button_add_generator_field.setToolTip(_translate("MainWindow",
                                                              "Добавляет поле с изменяемым для каждой задачи значением (можно задать во вкладке \"Настройка генераций)\""))
        self.button_save_and_generate.setToolTip(
            _translate("MainWindow", "Генерирует и сохраняет задачи в формате .gift в соответствии с примером задачи"))
        self.button_to_download.setToolTip(_translate("MainWindow", "Открывает в проводнике папку Downloads"))
        self.textEdit.setToolTip(_translate("MainWindow",
                                            "Здесь отображается пример сгенерированной задачи в соответствии с созданным шаблоном, указанном в \"Поле для создания задачи\""))
        self.button_example_text.setToolTip(_translate("MainWindow",
                                                       "Выводит пример текста сгенерированной задачи в поле \"Пример задачи\", но не выполняет никаких вычислений"))
        self.scrollArea_3.setToolTip(_translate("MainWindow",
                                                "Здесь можно настроить параметры генераторов значений, созданных во вкладке \"Основная рабочая область\""))
        self.scrollArea_4.setToolTip(_translate("MainWindow",
                                                "Здесь можно задать идентификаторы переменных, используемых для вычисления значения"))
        self.scrollArea_5.setToolTip(
            _translate("MainWindow", "Здесь отображаются созданные константы, вы можете изменить их значение"))
        self.button_delete_const.setToolTip(_translate("MainWindow", "Удалить последнее поле с постоянным значением"))
        self.button_add_const.setToolTip(_translate("MainWindow", "Добавить поле с постоянным значением"))
        self.spinBox_answer_index.setToolTip(
            _translate("MainWindow", "Идентификатор переменной, значение которой будет ответом задачи"))


if __name__ == "__main__":
    import os
    import sys
    from GraphTheory import Graph
    from AlgebraOfLogic import AlgebraOfLogic
    from Combinatorics import Combinatorics
    from Operations import Operations
    from My_exceptions import My_exceptions

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
