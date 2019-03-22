#-*- coding: UTF-8 -*-

import sys
from PyQt4 import QtCore, QtGui, uic , Qt
import  sqlite3
import  time
import xlsxwriter
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#import  fl_rc




qtCreatorFile = "windo_home.ui"  # Enter file here.
qtCreatorFile2 = "windi_2.ui"  # Enter file here.
qtCreatorFile3 = "add_new_etidient.ui"  # Enter file here.
qtCreatorFile4 = "add_new_classe.ui"  # Enter file here.
qtCreatorFile5 = "absence.ui"  # Enter file here.
qtCreatorFile6 = "update.ui"  # Enter file here.
qtCreatorFile7 = "update_nome_classe.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile )
Ui_MainWindow2, QtBaseClass = uic.loadUiType(qtCreatorFile2)
Ui_MainWindow3, QtBaseClass = uic.loadUiType(qtCreatorFile3)
Ui_MainWindow4, QtBaseClass = uic.loadUiType(qtCreatorFile4)
Ui_MainWindow5, QtBaseClass = uic.loadUiType(qtCreatorFile5)
Ui_MainWindow6, QtBaseClass = uic.loadUiType(qtCreatorFile6)
Ui_MainWindow7, QtBaseClass = uic.loadUiType(qtCreatorFile7)





class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.betton()
        #self.combobox_classe()
        self.time()




    def data_base(self):
        pass



    def betton(self):
         self.pushButton_3.clicked.connect(self.etidient)
         self.pushButton.clicked.connect(self.foneetrn_add_new_etidient)
         self.pushButton_8.clicked.connect(self.add_new_classe)
         self.pushButton_2.clicked.connect(self.vieus_absense)
         self.pushButton_4.clicked.connect(self.update)




    def etidient(self):
        self.window2 = fonetr_etidient()
        self.window2.show()




    def foneetrn_add_new_etidient(self):
        self.window3 = add_etidient()
        self.window3.show()

    def add_new_classe(self):
        self.window4 = add_new_classe()
        self.window4.show()
    def update(self):
        self.window5 = update()
        self.window5.show()

    def combobox_classe(self):
        file = ("C:\Users\hemidi benameur\Desktop\project_\data.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT classe FROM etidient " )

        s = self.cur.fetchall()
        """
        for  i  in  s  :
            if i[0] != None :
                self.comboBox.addItem(i[0])
        """
        ls = []
        ms = []
        for i in s:
            ls.append(i[0])
        for H in ls:
            if H not in ms:
                ms.append(H)

        for i in ms:
            if i != None:
                #self.comboBox.addItem(i)
                pass



    def number_absence_etidient(self):

        classe_  = self.comboBox.currentText()
        ####################################################################
        file = ("presence.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()


        self.cur.execute("""SELECT name_prenome , presence  FROM presence WHERE classe ='%s' """ % str(classe_))

        liste_data_presence = self.cur.fetchall()
        #####################################################################

        file2 = ("data.db")
        self.conn2 = sqlite3.connect(file2)
        self.cur2 = self.conn2.cursor()
        self.cur2.execute("SELECT * FROM  etidient WHERE classe = '%s' " % str(classe_)  )
        lise_data_etidient = self.cur2.fetchall()

        #####################################################################"

        nome_etidien = []
        for  i in  lise_data_etidient :
            nome_etidien.append(i[1] + ' ' + i[2])


        P = 0
        A = 0
        liste_final_present = {}
        liste_final_absence = {}

        for  i  in  nome_etidien :
            coumpt = 0
            while  coumpt < len(liste_data_presence) :
                if i in  liste_data_presence[coumpt] :
                    if  liste_data_presence[coumpt][1] == 'P'  :
                        P +=1
                    elif liste_data_presence[coumpt][1] == 'A' :
                        A +=1
                coumpt += 1
            liste_final_present[i] =  P
            liste_final_absence[i] =  A
            A = 0
            P =  0


        #print liste_final_absence
        #print liste_final_present
        #print liste_data_presence
        ##############################################################################
        ##############################################################################

    def vieus_absense(self):

        self.window5 = vieus_absence()
        self.window5.show()




    def time(self):
        time_new = time.strftime("%Y-%m-%d %H:%M", time.gmtime())
        self.lineEdit.setText(str(time_new))







#  هذا الكلاس تاع الفوناتر لي تعرض عدد الغيابات  و الحضور

class vieus_absence(QtGui.QMainWindow, Ui_MainWindow5):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.combobox_classe()
        self.button()



    def button(self):
        self.pushButton_2.clicked.connect(self.number_absence_etidient)
        self.pushButton.clicked.connect(self.amprim)


    #   الدالة التي تطبع ملف  الاكسل
    def amprim(self):

        try:
            classe =self.comboBox.currentText()
            file = ("presence.db")

            self.conn = sqlite3.connect(file)
            self.cur = self.conn.cursor()

            self.cur.execute("SELECT * FROM presence WHERE classe = '%s' " %classe)
            car = self.cur.fetchall()

            sav = Qt.QFileDialog.getSaveFileName(self, caption='save', directory= classe, filter="xlsx")
            wb = xlsxwriter.Workbook(str(sav) + '.' + 'xlsx')
            shet1 = wb.add_worksheet()

            """
            count  = 0
            LM  = [car[0]]
            for  i in car  :
                if i[2] == LM[count][2] and i[0] != LM[count][0]:
                    LM.append(i)
                if i[2] != LM[count][2] and i[0] == LM[count][0]:
                    LM.append(i)
                if i[2] != LM[count][2] and i[0] != LM[count][0]:
                    LM.append(i)
    
            car_ = LM
            ###############################"""
            bold = wb.add_format({'bold': True})


            #########################################



            data_presence = []
            nome_etidient = []
            # print car
            for i in car :
                if i[2] not in data_presence:
                    data_presence.append(i[2])
                if  i[0] not  in  nome_etidient :
                    nome_etidient.append(i[0])

            cul = 1
            for  i  in  data_presence :
                shet1.write(0, cul, str(i) , bold)
                cul += 1


            cul2 = 1
            for L in  nome_etidient :
                shet1.write(cul2 , 0 , L , bold)
                cul2 += 1


            for  i in data_presence :
                for  n in nome_etidient :
                    for m in  car :
                        if m[0] == n  and m[2] == i :
                            shet1.write(nome_etidient.index(n) + 1, data_presence.index(i)+1, str(m[3]) , bold)





            """
            cul =  1
    
            for i  in  car_  :
                shet1.write(0, cul, str(i[2]) )
                shet1.write(cul , 0 , i[0])
                if i[2] == car[n][2] :
                    shet1.write()
    
                shet1.write(cul , cul , i[3])
                cul += 1
    
            """











            wb.close()

        except :
            Qt.QMessageBox.critical(self , u'خطأ' , u'الرجاء تغيير اسم الملف')



    def combobox_classe(self):
        file = ("data.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT classe FROM etidient " )
        s = self.cur.fetchall()

        ls = []
        ms = []
        for i in  s  :
            ls.append(i[0])
        for H in ls :
            if H not in ms :
                ms.append(H)


        for  i  in  ms  :
            if i != None :
                self.comboBox.addItem(i)



    #    هذي  الدالة ترجع اسماء الطلبة في قائمة من 36 عنصر العدد الباقي من مجموع عدد الطلبة تعمره اصفار
    '''
    def liste_total(self):
        liste = self.get_nom_etidient()
        list__ =  [0] * 36
        i = 0
        while len(liste) > i :
            list__[i] = liste[i]
            i  = i+1
        return  list__
    '''



    def number_absence_etidient(self):

        classe_  = self.comboBox.currentText()
        ####################################################################
        file = ("presence.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()


        self.cur.execute("""SELECT name_prenome , presence  FROM presence WHERE classe ='%s' """ % str(classe_))

        liste_data_presence = self.cur.fetchall()
        #####################################################################

        file2 = ("data.db")
        self.conn2 = sqlite3.connect(file2)
        self.cur2 = self.conn2.cursor()
        self.cur2.execute("SELECT * FROM  etidient WHERE classe = '%s' " % str(classe_)  )
        lise_data_etidient = self.cur2.fetchall()

        #####################################################################"

        nome_etidien = []
        for  i in  lise_data_etidient :
            if  None not in i :
                nome_etidien.append(i[1] + ' ' + i[2])


        P = 0
        A = 0
        liste_final_present = {}
        liste_final_absence = {}

        for  i  in  nome_etidien :
            coumpt = 0
            while  coumpt < len(liste_data_presence) :
                if i in  liste_data_presence[coumpt] :
                    if  liste_data_presence[coumpt][1] == 'P'  :
                        P +=1
                    elif liste_data_presence[coumpt][1] == 'A' :
                        A +=1
                coumpt += 1
            liste_final_present[i] =  P
            liste_final_absence[i] =  A
            A = 0
            P =  0
        #######################################################################
        ################################    اضافة اسماء الطلبة في قائمة من 36 عنصر الباقي من مجموع الطلبة يساوي 0 #######################################
        #######################################################################
        liste = liste_final_present.keys()
        list__ = [0] * 36
        i = 0
        while len(liste) > i:
            list__[i] = liste[i]
            i = i + 1
         #################################################################"####
        ########################################################################

        L = [self.lineEdit_1.text() , self.lineEdit_2.text() , self.lineEdit_3.text() ,self.lineEdit_4.text() , self.lineEdit_5.text() ,self.lineEdit_6.text() , self.lineEdit_7.text(),
             self.lineEdit_8.text() , self.lineEdit_9.text() ,self.lineEdit_10.text() , self.lineEdit_11.text(), self.lineEdit_12.text() ,
             self.lineEdit_13.text() , self.lineEdit_14.text() , self.lineEdit_15.text() , self.lineEdit_16.text() , self.lineEdit_17.text() ,
             self.lineEdit_18.text(), self.lineEdit_19.text() , self.lineEdit_21.text() , self.lineEdit_22.text() , self.lineEdit_23.text(),
             self.lineEdit_24.text() , self.lineEdit_25.text() , self.lineEdit_26.text() , self.lineEdit_27.text() , self.lineEdit_28.text(),
             self.lineEdit_29.text() , self.lineEdit_30.text() , self.lineEdit_31.text() , self.lineEdit_32.text() , self.lineEdit_33.text(),
             self.lineEdit_34.text() , self.lineEdit_35.text() , self.lineEdit_36.text()]

        #############################################################
        #  # هذا الكود لتفريغ الاماكن التي يوجد بها كتابة سابقة
        #######################################################"#############

        v  = ''

        if list__[0] == 0 :
            self.lineEdit_1.setText(v)
            self.lcdNumber_1.display(0)
            self.lcdNumber_1_1.display(0)

        if list__[1] == 0 :
            self.lineEdit_2.setText(v)
            self.lcdNumber_2.display(0)
            self.lcdNumber_2_2.display(0)
        if list__[2] == 0 :
            self.lineEdit_3.setText(v)
            self.lcdNumber_3.display(0)
            self.lcdNumber_3_3.display(0)
        if list__[3] == 0 :
            self.lineEdit_4.setText(v)
            self.lcdNumber_4.display(0)
            self.lcdNumber_4_4.display(0)
        if list__[4] == 0 :
            self.lineEdit_5.setText(v)
            self.lcdNumber_5.display(0)
            self.lcdNumber_5_5.display(0)

        if list__[5] == 0:
            self.lineEdit_6.setText(v)
            self.lcdNumber_6.display(0)
            self.lcdNumber_6_6.display(0)
        if list__[6] == 0:
            self.lineEdit_7.setText(v)
            self.lcdNumber_7.display(0)
            self.lcdNumber_7_7.display(0)

        if list__[7] == 0:
            self.lineEdit_8.setText(v)
            self.lcdNumber_8.display(0)
            self.lcdNumber_8_8.display(0)

        if list__[8] == 0 :
            self.lineEdit_9.setText(v)
            self.lcdNumber_9.display(0)
            self.lcdNumber_9_9.display(0)
        if list__[9] == 0 :
            self.lineEdit_10.setText(v)
            self.lcdNumber_10.display(0)
            self.lcdNumber_10_10.display(0)

        if list__[10] == 0 :
            self.lineEdit_11.setText(v)
            self.lcdNumber_11.display(0)
            self.lcdNumber_11_11.display(0)

        if list__[11] == 0 :
            self.lineEdit_12.setText('')
            self.lcdNumber_12.display(0)
            self.lcdNumber_12_12.display(0)

        if list__[12] == 0 :
            self.lineEdit_13.setText('')
            self.lcdNumber_13.display(0)
            self.lcdNumber_13_13.display(0)
        if list__[13] == 0 :
            self.lineEdit_14.setText('')
            self.lcdNumber_14.display(0)
            self.lcdNumber_14_14.display(0)

        if list__[14] == 0 :
            self.lineEdit_15.setText('')
            self.lcdNumber_15.display(0)
            self.lcdNumber_15_15.display(0)

        if list__[15] == 0 :
            self.lineEdit_16.setText('')
            self.lcdNumber_16.display(0)
            self.lcdNumber_16_16.display(0)

        if list__[16] == 0 :
            self.lineEdit_17.setText('')
            self.lcdNumber_17.display(0)
            self.lcdNumber_17_17.display(0)

        if list__[17] == 0 :
            self.lineEdit_18.setText('')
            self.lcdNumber_18.display(0)
            self.lcdNumber_18_18.display(0)

        if list__[18] == 0 :
            self.lineEdit_19.setText('')
            self.lcdNumber_19.display(0)
            self.lcdNumber_19_19.display(0)
        if list__[19] == 0 :
            self.lineEdit_20.setText('')
            self.lcdNumber_20.display(0)
            self.lcdNumber_20_20.display(0)

        if list__[20] == 0 :
            self.lineEdit_21.setText('')
            self.lcdNumber_21.display(0)
            self.lcdNumber_21_21.display(0)

        if list__[21] == 0 :
            self.lineEdit_22.setText('')
            self.lcdNumber_22.display(0)
            self.lcdNumber_22_22.display(0)

        if list__[22] == 0 :
            self.lineEdit_23.setText('')
            self.lcdNumber_23.display(0)
            self.lcdNumber_23_23.display(0)

        if list__[23] == 0 :
            self.lineEdit_24.setText('')
            self.lcdNumber_24.display(0)
            self.lcdNumber_24_24.display(0)

        if list__[24] == 0 :
            self.lineEdit_25.setText('')
            self.lcdNumber_25.display(0)
            self.lcdNumber_25_25.display(0)


        if list__[25] == 0 :
            self.lineEdit_26.setText('')
            self.lcdNumber_26.display(0)
            self.lcdNumber_26_26.display(0)

        if list__[26] == 0 :
            self.lineEdit_27.setText('')
            self.lcdNumber_27.display(0)
            self.lcdNumber_27_27.display(0)
        if list__[27] == 0 :
            self.lineEdit_28.setText('')
            self.lcdNumber_28.display(0)
            self.lcdNumber_28_28.display(0)

        if list__[28] == 0 :
            self.lineEdit_29.setText('')
            self.lcdNumber_29.display(0)
            self.lcdNumber_29_29.display(0)

        if list__[29] == 0 :
            self.lineEdit_30.setText('')
            self.lcdNumber_30.display(0)
            self.lcdNumber_30_30.display(0)

        if list__[30] == 0 :
            self.lineEdit_31.setText('')
            self.lcdNumber_31.display(0)
            self.lcdNumber_31_31.display(0)

        if list__[31] == 0 :
            self.lineEdit_32.setText('')
            self.lcdNumber_32.display(0)
            self.lcdNumber_32_32.display(0)
        if list__[32] == 0 :
            self.lineEdit_33.setText('')
            self.lcdNumber_33.display(0)
            self.lcdNumber_33_33.display(0)

        if list__[33] == 0 :
            self.lineEdit_34.setText('')
            self.lcdNumber_34.display(0)
            self.lcdNumber_34_34.display(0)
        if list__[34] == 0 :
            self.lineEdit_35.setText('')
            self.lcdNumber_35.display(0)
            self.lcdNumber_35_35.display(0)
        if list__[35] == 0 :
            self.lineEdit_36.setText('')
            self.lcdNumber_36.display(0)
            self.lcdNumber_36_36.display(0)

        ##################################################################################
        #         تسجيل الفيابات و اسم كل طالب

        ####################################################################################
        if list__[0] != 0 and list__[0] != '' :
            self.lineEdit_1.setText(liste_final_present.keys()[0])
            self.lcdNumber_1.display(liste_final_absence.values()[0])
            self.lcdNumber_1_1.display(liste_final_present.values()[0])

        if list__[1] != 0 and list__[1] != '' :
            self.lineEdit_2.setText(liste_final_present.keys()[1])
            self.lcdNumber_2.display(liste_final_absence.values()[1])
            self.lcdNumber_2_2.display(liste_final_present.values()[1])
        if list__[2] != 0 and list__[2] != '' :
            self.lineEdit_3.setText(liste_final_present.keys()[2])
            self.lcdNumber_3.display(liste_final_absence.values()[2])
            self.lcdNumber_3_3.display(liste_final_present.values()[2])
        if list__[3] != 0 and list__[3] != '' :
            self.lineEdit_4.setText(liste_final_present.keys()[3])
            self.lcdNumber_4.display(liste_final_absence.values()[3])
            self.lcdNumber_4_4.display(liste_final_present.values()[3])
        if list__[4] != 0 and list__[4] != '' :
            self.lineEdit_5.setText(liste_final_present.keys()[4])
            self.lcdNumber_5.display(liste_final_absence.values()[4])
            self.lcdNumber_5_5.display(liste_final_present.values()[4])

        if list__[5] != 0 and list__[5] != '' :
            self.lineEdit_6.setText(liste_final_present.keys()[5])
            self.lcdNumber_6.display(liste_final_absence.values()[5])
            self.lcdNumber_6_6.display(liste_final_present.values()[5])
        if list__[6] != 0 and list__[6] != '' :
            self.lineEdit_7.setText(liste_final_present.keys()[6])
            self.lcdNumber_7.display(liste_final_absence.values()[6])
            self.lcdNumber_7_7.display(liste_final_present.values()[6])

        if list__[7] != 0 and list__[7] != '' :
            self.lineEdit_8.setText(liste_final_present.keys()[7])
            self.lcdNumber_8.display(liste_final_absence.values()[7])
            self.lcdNumber_8_8.display(liste_final_present.values()[7])

        if list__[8] != 0 and list__[8] != '' :
            self.lineEdit_9.setText(liste_final_present.keys()[8])
            self.lcdNumber_9.display(liste_final_absence.values()[8])
            self.lcdNumber_9_9.display(liste_final_present.values()[8])
        if list__[9] != 0 and list__[9] != '' :
            self.lineEdit_10.setText(liste_final_present.keys()[9])
            self.lcdNumber_10.display(liste_final_absence.values()[9])
            self.lcdNumber_10_10.display(liste_final_present.values()[9])

        if list__[10] != 0 and list__[10] != '' :
            self.lineEdit_11.setText(liste_final_present.keys()[10])
            self.lcdNumber_11.display(liste_final_absence.values()[10])
            self.lcdNumber_11_11.display(liste_final_present.values()[10])

        if list__[11] != 0 and list__[11] != '' :
            self.lineEdit_12.setText(liste_final_present.keys()[11])
            self.lcdNumber_12.display(liste_final_absence.values()[11])
            self.lcdNumber_12_12.display(liste_final_present.values()[11])

        if list__[12] != 0 and list__[12] != '' :
            self.lineEdit_13.setText(liste_final_present.keys()[12])
            self.lcdNumber_13.display(liste_final_absence.values()[12])
            self.lcdNumber_13_13.display(liste_final_present.values()[12])
        if list__[13] != 0 and list__[13] != '' :
            self.lineEdit_14.setText(liste_final_present.keys()[13])
            self.lcdNumber_14.display(liste_final_absence.values()[13])
            self.lcdNumber_14_14.display(liste_final_present.values()[13])

        if list__[14] != 0 and list__[14] != '' :
            self.lineEdit_15.setText(liste_final_present.keys()[14])
            self.lcdNumber_15.display(liste_final_absence.values()[14])
            self.lcdNumber_15_15.display(liste_final_present.values()[14])

        if list__[15] != 0 and list__[15] != '' :
            self.lineEdit_16.setText(liste_final_present.keys()[15])
            self.lcdNumber_16.display(liste_final_absence.values()[15])
            self.lcdNumber_16_16.display(liste_final_present.values()[15])

        if list__[16] != 0 and list__[16] != '' :
            self.lineEdit_17.setText(liste_final_present.keys()[16])
            self.lcdNumber_17.display(liste_final_absence.values()[16])
            self.lcdNumber_17_17.display(liste_final_present.values()[16])

        if list__[17] != 0 and list__[17] != '' :
            self.lineEdit_18.setText(liste_final_present.keys()[17])
            self.lcdNumber_18.display(liste_final_absence.values()[17])
            self.lcdNumber_18_18.display(liste_final_present.values()[17])

        if list__[18] != 0 and list__[18] != '' :
            self.lineEdit_19.setText(liste_final_present.keys()[18])
            self.lcdNumber_19.display(liste_final_absence.values()[18])
            self.lcdNumber_19_19.display(liste_final_present.values()[18])
        if list__[19] != 0 and list__[19] != '' :
            self.lineEdit_20.setText(liste_final_present.keys()[19])
            self.lcdNumber_20.display(liste_final_absence.values()[19])
            self.lcdNumber_20_20.display(liste_final_present.values()[19])

        if list__[20] != 0 and list__[20] != '' :
            self.lineEdit_21.setText(liste_final_present.keys()[20])
            self.lcdNumber_21.display(liste_final_absence.values()[20])
            self.lcdNumber_21_21.display(liste_final_present.values()[20])

        if list__[21] != 0 and list__[21] != '' :
            self.lineEdit_22.setText(liste_final_present.keys()[21])
            self.lcdNumber_22.display(liste_final_absence.values()[21])
            self.lcdNumber_22_22.display(liste_final_present.values()[21])

        if list__[22] != 0 and list__[22] != '' :
            self.lineEdit_23.setText(liste_final_present.keys()[22])
            self.lcdNumber_23.display(liste_final_absence.values()[22])
            self.lcdNumber_23_23.display(liste_final_present.values()[22])

        if list__[23] != 0 and list__[23] != '' :
            self.lineEdit_24.setText(liste_final_present.keys()[23])
            self.lcdNumber_24.display(liste_final_absence.values()[23])
            self.lcdNumber_24_24.display(liste_final_present.values()[23])

        ###########################################################################"
        if list__[24] != 0 and list__[24] != '':
            self.lineEdit_25.setText(liste_final_present.keys()[24])
            self.lcdNumber_25.display(liste_final_absence.values()[24])
            self.lcdNumber_25_25.display(liste_final_present.values()[24])

        ##############################################################################


        if list__[25] != 0 and list__[25] != '' :
            self.lineEdit_26.setText(liste_final_present.keys()[25])
            self.lcdNumber_26.display(liste_final_absence.values()[25])
            self.lcdNumber_26_26.display(liste_final_present.values()[25])

        if list__[26] != 0 and list__[26] != '' :
            self.lineEdit_27.setText(liste_final_present.keys()[26])
            self.lcdNumber_27.display(liste_final_absence.values()[26])
            self.lcdNumber_27_27.display(liste_final_present.values()[26])
        if list__[27] != 0 and list__[27] != '' :
            self.lineEdit_28.setText(liste_final_present.keys()[27])
            self.lcdNumber_28.display(liste_final_absence.values()[27])
            self.lcdNumber_28_28.display(liste_final_present.values()[27])

        if list__[28] != 0 and list__[28] != '' :
            self.lineEdit_29.setText(liste_final_present.keys()[28])
            self.lcdNumber_29.display(liste_final_absence.values()[28])
            self.lcdNumber_29_29.display(liste_final_present.values()[28])

        if list__[29] != 0 and list__[29] != '' :
            self.lineEdit_30.setText(liste_final_present.keys()[29])
            self.lcdNumber_30.display(liste_final_absence.values()[29])
            self.lcdNumber_30_30.display(liste_final_present.values()[29])

        if list__[30] != 0 and list__[30] != '' :
            self.lineEdit_31.setText(liste_final_present.keys()[30])
            self.lcdNumber_31.display(liste_final_absence.values()[30])
            self.lcdNumber_31_31.display(liste_final_present.values()[30])

        if list__[31] != 0 and list__[31] != '' :
            self.lineEdit_32.setText(liste_final_present.keys()[31])
            self.lcdNumber_32.display(liste_final_absence.values()[31])
            self.lcdNumber_32_32.display(liste_final_present.values()[31])
        if list__[32] != 0 and list__[32] != '' :
            self.lineEdit_33.setText(liste_final_present.keys()[32])
            self.lcdNumber_33.display(liste_final_absence.values()[32])
            self.lcdNumber_33_33.display(liste_final_present.values()[32])

        if list__[33] != 0 and list__[33] != '' :
            self.lineEdit_34.setText(liste_final_present.keys()[33])
            self.lcdNumber_34.display(liste_final_absence.values()[33])
            self.lcdNumber_34_34.display(liste_final_present.values()[33])
        if list__[34] != 0 and list__[34] != '' :
            self.lineEdit_35.setText(liste_final_present.keys()[34])
            self.lcdNumber_35.display(liste_final_absence.values()[34])
            self.lcdNumber_35_35.display(liste_final_present.values()[34])
        if list__[35] != 0 and list__[35] != '' :
            self.lineEdit_36.setText(liste_final_present.keys()[35])
            self.lcdNumber_36.display(liste_final_absence.values()[35])
            self.lcdNumber_36_36.display(liste_final_present.values()[35])
































# هذا الكلاس تاع الطلبة يمركي الابسنس
class fonetr_etidient(QtGui.QMainWindow, Ui_MainWindow2):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.combobox_classe()
        self.bottun()


    def bottun(self):
        self.pushButton_3.clicked.connect(self.pass_nome_etidient)
        self.pushButton.clicked.connect(self.presence)
        #self.pushButton.clicked.connect(self.pass_nome_etidient)



    # تشغيل كومبو بوكس
    def combobox_classe(self):
        file = ("C:\Users\hemidi benameur\Desktop\project_\data.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT classe FROM etidient " )
        s = self.cur.fetchall()

        '''
        for  i  in  s  :
            if i[0] != None :
                self.comboBox.addItem(i[0])
                
        '''
        ls = []
        ms = []
        for i in s:
            ls.append(i[0])
        for H in ls:
            if H not in ms:
                ms.append(H)

        for i in ms:
            if i != None:
                self.comboBox.addItem(i)

    # هذي  الدالة ترجع كامل اسماء الي في القسم في قائمة

    def get_nom_etidient(self):
        classe_combo = self.comboBox.currentText()
        file = ("data.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()


        self.cur.execute("SELECT * FROM etidient")
        car = self.cur.fetchall()

        list_class = []

        #print(car)

        #strr = u' '.join(classe).encode('utf-8')



        for i  in  car :
            if  classe_combo in  i and None not in i   :
                list_class.append(i[1]+' '+i[2])
        return   list_class


    #  هذي الدالة تدمج بين قائمة مكونة من 36 صفر و القائمة التي  تحتوي اسماء الطلبة للاستخدام فيما بعد
    def liste_total(self):
        liste = self.get_nom_etidient()
        list__ =  [0] * 36
        i = 0
        while len(liste) > i :
            list__[i] = liste[i]
            i  = i+1
        return  list__


    # هذي الدالة لطباعة الاسم و اللقب في اللاين اديت
    def pass_nome_etidient(self):
        liste = self.liste_total()

        #    تفريغ الاشارات او المعلمات

        self.checkBox1.setChecked(False)
        self.checkBox2.setChecked(False)
        self.checkBox3.setChecked(False)
        self.checkBox4.setChecked(False)
        self.checkBox5.setChecked(False)
        self.checkBox6.setChecked(False)
        self.checkBox7.setChecked(False)
        self.checkBox8.setChecked(False)
        self.checkBox9.setChecked(False)
        self.checkBox10.setChecked(False)
        self.checkBox11.setChecked(False)
        self.checkBox12.setChecked(False)
        self.checkBox13.setChecked(False)
        self.checkBox14.setChecked(False)
        self.checkBox15.setChecked(False)
        self.checkBox16.setChecked(False)
        self.checkBox17.setChecked(False)
        self.checkBox18.setChecked(False)
        self.checkBox19.setChecked(False)
        self.checkBox20.setChecked(False)
        self.checkBox21.setChecked(False)
        self.checkBox22.setChecked(False)
        self.checkBox23.setChecked(False)
        self.checkBox24.setChecked(False)
        self.checkBox25.setChecked(False)
        self.checkBox26.setChecked(False)
        self.checkBox27.setChecked(False)
        self.checkBox28.setChecked(False)
        self.checkBox29.setChecked(False)
        self.checkBox30.setChecked(False)
        self.checkBox31.setChecked(False)
        self.checkBox32.setChecked(False)
        self.checkBox33.setChecked(False)
        self.checkBox34.setChecked(False)
        self.checkBox35.setChecked(False)
        self.checkBox36.setChecked(False)
        self.checkBox37.setChecked(False)
        self.checkBox38.setChecked(False)
        self.checkBox39.setChecked(False)
        self.checkBox40.setChecked(False)
        self.checkBox41.setChecked(False)
        self.checkBox42.setChecked(False)
        self.checkBox43.setChecked(False)
        self.checkBox44.setChecked(False)
        self.checkBox45.setChecked(False)
        self.checkBox46.setChecked(False)
        self.checkBox47.setChecked(False)
        self.checkBox48.setChecked(False)
        self.checkBox49.setChecked(False)
        self.checkBox50.setChecked(False)
        self.checkBox51.setChecked(False)
        self.checkBox52.setChecked(False)
        self.checkBox53.setChecked(False)
        self.checkBox54.setChecked(False)
        self.checkBox55.setChecked(False)
        self.checkBox56.setChecked(False)
        self.checkBox57.setChecked(False)
        self.checkBox58.setChecked(False)
        self.checkBox59.setChecked(False)
        self.checkBox60.setChecked(False)
        self.checkBox61.setChecked(False)
        self.checkBox62.setChecked(False)
        self.checkBox63.setChecked(False)
        self.checkBox64.setChecked(False)
        self.checkBox65.setChecked(False)
        self.checkBox66.setChecked(False)
        self.checkBox67.setChecked(False)
        self.checkBox68.setChecked(False)
        self.checkBox69.setChecked(False)
        self.checkBox70.setChecked(False)
        self.checkBox71.setChecked(False)
        self.checkBox72.setChecked(False)


        ##############################  تفريغ المساحات    ########################

        if liste[0] == 0 :
            self.lineEdit_1.setText('')
        if liste[1] == 0  :
            self.lineEdit_2.setText('')
        if liste[2] == 0   :
            self.lineEdit_3.setText('')
        if liste[3] == 0:
            self.lineEdit_4.setText('')
        if liste[4] == 0  :
            self.lineEdit_5.setText('')
        if liste[5] == 0  :
            self.lineEdit_6.setText('')
        if liste[6] == 0:
            self.lineEdit_7.setText('')
        if liste[7] == 0 :
            self.lineEdit_8.setText('')
        if liste[8] == 0  :
            self.lineEdit_9.setText('')
        if liste[9] == 0 :
            self.lineEdit_10.setText('')
        if liste[10] == 0 :
            self.lineEdit_11.setText('')
        if liste[11] == 0 :
            self.lineEdit_12.setText('')
        if liste[12] == 0 :
            self.lineEdit_13.setText('')
        if liste[13] == 0 :
            self.lineEdit_14.setText('')
        if liste[14] == 0 :
            self.lineEdit_15.setText('')
        if liste[15] == 0  :
            self.lineEdit_16.setText('')
        if liste[16] == 0  :
            self.lineEdit_17.setText('')
        if liste[17] == 0  :
            self.lineEdit_18.setText('')
        if liste[18] == 0  :
            self.lineEdit_19.setText('')
        if liste[19] == 0:
            self.lineEdit_20.setText('')
        if liste[20] == 0   :
            self.lineEdit_21.setText('')
        if liste[21] == 0  :
            self.lineEdit_22.setText('')
        if liste[22] == 0  :
            self.lineEdit_23.setText('')
        if liste[23] == 0  :
            self.lineEdit_24.setText('')
        if liste[24] == 0  :
            self.lineEdit_25.setText('')
        if liste[25] == 0 :
            self.lineEdit_26.setText('')
        if liste[26] == 0:
            self.lineEdit_27.setText('')
        if liste[27] == 0  :
            self.lineEdit_28.setText('')
        if liste[28] == 0  :
            self.lineEdit_29.setText('')
        if liste[29] == 0 :
            self.lineEdit_30.setText('')
        if liste[30] == 0 :
            self.lineEdit_31.setText('')
        if liste[31] == 0  :
            self.lineEdit_32.setText('')
        if liste[32] == 0  :
            self.lineEdit_33.setText('')
        if liste[33] == 0  :
            self.lineEdit_34.setText('')
        if liste[34] == 0  :
            self.lineEdit_35.setText('')
        if liste[35] == 0  :
            self.lineEdit_36.setText('')



        ###########
        ############################  الكتابة على  المساحات  #############################################
        if liste[0] != 0 and liste[0] != None :
            self.lineEdit_1.setText(liste[0])
        if liste[1] != 0 and liste[1] != None :
            self.lineEdit_2.setText(liste[1])
        if liste[2] != 0  and liste[2] != None :
            self.lineEdit_3.setText(liste[2])
        if liste[3] != 0 and liste[3] != None :
            self.lineEdit_4.setText(liste[3])
        if liste[4] != 0 and liste[4] != None :
            self.lineEdit_5.setText(liste[4])
        if liste[5] != 0 and liste[5] != None :
            self.lineEdit_6.setText(liste[5])
        if liste[6] != 0 and liste[6] != None :
            self.lineEdit_7.setText(liste[6])
        if liste[7] != 0 and liste[7] != None :
            self.lineEdit_8.setText(liste[7])
        if liste[8] != 0 and liste[8] != None :
            self.lineEdit_9.setText(liste[8])
        if liste[9] != 0 and liste[9] != None :
            self.lineEdit_10.setText(liste[9])
        if liste[10] != 0 and liste[10] != None :
            self.lineEdit_11.setText(liste[10])
        if liste[11] != 0 and liste[11] != None :
            self.lineEdit_12.setText(liste[11])
        if liste[12] != 0 and liste[12] != None :
            self.lineEdit_13.setText(liste[12])
        if liste[13] != 0 and liste[13] != None :
            self.lineEdit_14.setText(liste[13])
        if liste[14] != 0 and liste[14] != None :
            self.lineEdit_15.setText(liste[14])
        if liste[15] != 0 and liste[15] != None :
            self.lineEdit_16.setText(liste[15])
        if liste[16] != 0 and liste[16] != None :
            self.lineEdit_17.setText(liste[16])
        if liste[17] != 0 and liste[17] != None :
            self.lineEdit_18.setText(liste[17])
        if liste[18] != 0 and liste[18] != None :
            self.lineEdit_19.setText(liste[18])
        if liste[19] != 0 and liste[19] != None :
            self.lineEdit_20.setText(liste[19])
        if liste[20] != 0 and liste[20] != None  :
            self.lineEdit_21.setText(liste[20])
        if liste[21] != 0 and liste[21] != None :
            self.lineEdit_22.setText(liste[21])
        if liste[22] != 0 and liste[22] != None :
            self.lineEdit_23.setText(liste[22])
        if liste[23] != 0 and liste[23] != None :
            self.lineEdit_24.setText(liste[23])
        if liste[24] != 0 and liste[24] != None :
            self.lineEdit_25.setText(liste[24])
        if liste[25] != 0 and liste[25] != None :
            self.lineEdit_26.setText(liste[25])
        if liste[26] != 0 and liste[26] != None :
            self.lineEdit_27.setText(liste[26])
        if liste[27] != 0 and liste[27] != None :
            self.lineEdit_28.setText(liste[27])
        if liste[28] != 0 and liste[28] != None :
            self.lineEdit_29.setText(liste[28])
        if liste[29] != 0 and liste[29] != None :
            self.lineEdit_30.setText(liste[29])
        if liste[30] != 0 and liste[30] != None :
            self.lineEdit_31.setText(liste[30])
        if liste[31] != 0 and liste[31] != None :
            self.lineEdit_32.setText(liste[31])
        if liste[32] != 0 and liste[32] != None :
            self.lineEdit_33.setText(liste[32])
        if liste[33] != 0 and liste[33] != None :
            self.lineEdit_34.setText(liste[33])
        if liste[34] != 0 and liste[34] != None :
            self.lineEdit_35.setText(liste[34])
        if liste[35] != 0 and liste[35] != None :
            self.lineEdit_36.setText(liste[35])






    def presence(self):


        time_new = time.strftime("%Y-%m-%d %H:%M", time.gmtime())
        classe = self.comboBox.currentText()


        filee = ("presence.db")
        self.conn = sqlite3.connect(filee)
        self.cur = self.conn.cursor()

        try:
            ppp  = {}

            flag5 = 0
            if self.lineEdit_1.text() != ''  :
                name_prenome =  self.lineEdit_1.text()
                if self.checkBox1.isChecked() !=  self.checkBox2.isChecked() :
                    if self.checkBox1.isChecked() == True and self.checkBox2.isChecked() == False :
                        presence =  'P'
                    else  :
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_2.text() != ''  :
                name_prenome =  self.lineEdit_2.text()
                if self.checkBox3.isChecked() !=  self.checkBox4.isChecked() :
                    if self.checkBox3.isChecked() == True and self.checkBox4.isChecked() == False :
                        presence =  'P'
                    else  :
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_3.text() != ''  :
                name_prenome =  self.lineEdit_3.text()
                if self.checkBox5.isChecked() !=  self.checkBox6.isChecked() :
                    if self.checkBox5.isChecked() == True and self.checkBox6.isChecked() == False :
                        presence =  'P'
                    else  :
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence

            if self.lineEdit_4.text() != ''  :
                name_prenome =  self.lineEdit_4.text()
                if self.checkBox7.isChecked() !=  self.checkBox8.isChecked() :
                    if self.checkBox7.isChecked() == True and self.checkBox8.isChecked() == False :
                        presence =  'P'
                    else  :
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_5.text() != ''  :
                name_prenome =  self.lineEdit_5.text()
                if self.checkBox9.isChecked() !=  self.checkBox10.isChecked() :
                    if self.checkBox9.isChecked() == True and self.checkBox10.isChecked() == False :
                        presence =  'P'
                    else  :
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_6.text() != ''  :
                name_prenome =  self.lineEdit_6.text()
                if self.checkBox11.isChecked() !=  self.checkBox12.isChecked() :
                    if self.checkBox11.isChecked() == True and self.checkBox12.isChecked() == False :
                        presence =  'P'
                    else  :
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_7.text() != ''  :
                name_prenome =  self.lineEdit_7.text()
                if self.checkBox13.isChecked() !=  self.checkBox14.isChecked() :
                    if self.checkBox13.isChecked() == True and self.checkBox14.isChecked() == False :
                        presence =  'P'
                    else  :
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_8.text() != ''  :
                name_prenome =  self.lineEdit_8.text()
                if self.checkBox15.isChecked() !=  self.checkBox16.isChecked() :
                    if self.checkBox15.isChecked() == True and self.checkBox16.isChecked() == False :
                        presence =  'P'
                    else  :
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_9.text() != ''  :
                name_prenome =  self.lineEdit_9.text()
                if self.checkBox17.isChecked() !=  self.checkBox18.isChecked() :
                    if self.checkBox17.isChecked() == True and self.checkBox18.isChecked() == False :
                        presence =  'P'
                    else  :
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_10.text() != ''  :
                name_prenome =  self.lineEdit_10.text()
                if self.checkBox19.isChecked() !=  self.checkBox20.isChecked() :
                    if self.checkBox19.isChecked() == True and self.checkBox20.isChecked() == False :
                        presence =  'P'
                    else  :
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_11.text() != ''  :
                name_prenome =  self.lineEdit_11.text()
                if self.checkBox21.isChecked() !=  self.checkBox22.isChecked() :
                    if self.checkBox21.isChecked() == True and self.checkBox22.isChecked() == False :
                        presence =  'P'
                    else  :
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_12.text() != ''  :
                name_prenome =  self.lineEdit_12.text()
                if self.checkBox23.isChecked() !=  self.checkBox24.isChecked() :
                    if self.checkBox23.isChecked() == True and self.checkBox24.isChecked() == False :
                        presence =  'P'
                    else  :
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_13.text() != ''  :
                name_prenome =  self.lineEdit_13.text()
                if self.checkBox25.isChecked() !=  self.checkBox26.isChecked() :
                    if self.checkBox25.isChecked() == True and self.checkBox26.isChecked() == False :
                        presence =  'P'
                    else  :
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_14.text() != ''  :
                name_prenome =  self.lineEdit_14.text()
                if self.checkBox27.isChecked() !=  self.checkBox28.isChecked() :
                    if self.checkBox27.isChecked() == True and self.checkBox28.isChecked() == False :
                        presence =  'P'
                    else  :
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_15.text() != '':
                name_prenome = self.lineEdit_15.text()
                if self.checkBox29.isChecked() != self.checkBox30.isChecked():
                    if self.checkBox29.isChecked() == True and self.checkBox30.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_16.text() != '':
                name_prenome = self.lineEdit_16.text()
                if self.checkBox31.isChecked() != self.checkBox32.isChecked():
                    if self.checkBox31.isChecked() == True and self.checkBox32.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_17.text() != '':
                name_prenome = self.lineEdit_17.text()
                if self.checkBox33.isChecked() != self.checkBox34.isChecked():
                    if self.checkBox33.isChecked() == True and self.checkBox34.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence



            if self.lineEdit_18.text() != '':
                name_prenome = self.lineEdit_18.text()
                if self.checkBox35.isChecked() != self.checkBox36.isChecked():
                    if self.checkBox35.isChecked() == True and self.checkBox36.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_19.text() != '':
                name_prenome = self.lineEdit_19.text()
                if self.checkBox37.isChecked() != self.checkBox38.isChecked():
                    if self.checkBox37.isChecked() == True and self.checkBox38.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_20.text() != '':
                name_prenome = self.lineEdit_20.text()
                if self.checkBox39.isChecked() != self.checkBox40.isChecked():
                    if self.checkBox39.isChecked() == True and self.checkBox40.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_21.text() != '':
                name_prenome = self.lineEdit_21.text()
                if self.checkBox41.isChecked() != self.checkBox42.isChecked():
                    if self.checkBox41.isChecked() == True and self.checkBox42.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_22.text() != '':
                name_prenome = self.lineEdit_22.text()
                if self.checkBox43.isChecked() != self.checkBox44.isChecked():
                    if self.checkBox43.isChecked() == True and self.checkBox44.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence

            if self.lineEdit_23.text() != '':
                name_prenome = self.lineEdit_23.text()
                if self.checkBox45.isChecked() != self.checkBox46.isChecked():
                    if self.checkBox45.isChecked() == True and self.checkBox46.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence



            if self.lineEdit_24.text() != '':
                name_prenome = self.lineEdit_24.text()
                if self.checkBox47.isChecked() != self.checkBox48.isChecked():
                    if self.checkBox47.isChecked() == True and self.checkBox48.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_25.text() != '':
                name_prenome = self.lineEdit_25.text()
                if self.checkBox49.isChecked() != self.checkBox50.isChecked():
                    if self.checkBox49.isChecked() == True and self.checkBox50.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_26.text() != '':
                name_prenome = self.lineEdit_26.text()
                if self.checkBox51.isChecked() != self.checkBox52.isChecked():
                    if self.checkBox51.isChecked() == True and self.checkBox52.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_27.text() != '':
                name_prenome = self.lineEdit_27.text()
                if self.checkBox53.isChecked() != self.checkBox54.isChecked():
                    if self.checkBox53.isChecked() == True and self.checkBox54.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_28.text() != '':
                name_prenome = self.lineEdit_28.text()
                if self.checkBox55.isChecked() != self.checkBox56.isChecked():
                    if self.checkBox55.isChecked() == True and self.checkBox56.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_29.text() != '':
                name_prenome = self.lineEdit_29.text()
                if self.checkBox57.isChecked() != self.checkBox58.isChecked():
                    if self.checkBox57.isChecked() == True and self.checkBox58.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_30.text() != '':
                name_prenome = self.lineEdit_30.text()
                if self.checkBox59.isChecked() != self.checkBox60.isChecked():
                    if self.checkBox59.isChecked() == True and self.checkBox60.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence



            if self.lineEdit_31.text() != '':
                name_prenome = self.lineEdit_31.text()
                if self.checkBox61.isChecked() != self.checkBox62.isChecked():
                    if self.checkBox61.isChecked() == True and self.checkBox62.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_32.text() != '':
                name_prenome = self.lineEdit_32.text()
                if self.checkBox63.isChecked() != self.checkBox64.isChecked():
                    if self.checkBox63.isChecked() == True and self.checkBox64.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence



            if self.lineEdit_33.text() != '':
                name_prenome = self.lineEdit_33.text()
                if self.checkBox65.isChecked() != self.checkBox66.isChecked():
                    if self.checkBox65.isChecked() == True and self.checkBox66.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_34.text() != '':
                name_prenome = self.lineEdit_34.text()
                if self.checkBox67.isChecked() != self.checkBox68.isChecked():
                    if self.checkBox67.isChecked() == True and self.checkBox68.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence



            if self.lineEdit_35.text() != '':
                name_prenome = self.lineEdit_35.text()
                if self.checkBox69.isChecked() != self.checkBox70.isChecked():
                    if self.checkBox69.isChecked() == True and self.checkBox70.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence


            if self.lineEdit_36.text() != '':
                name_prenome = self.lineEdit_36.text()
                if self.checkBox71.isChecked() != self.checkBox72.isChecked():
                    if self.checkBox71.isChecked() == True and self.checkBox72.isChecked() == False:
                        presence = 'P'
                    else:
                        presence = 'A'
                    flag5 += 1
                    ppp[name_prenome] = presence




            #   قائمة الطلبة

            N  = self.get_nom_etidient()

            #  اذا كان كل شيئ على  ما يرام احفظ في قاعدة المعلومات  و الا هناك خطأ

            if flag5 == len(N) :
                ppp_ = ppp.items()
                for i in  ppp_ :
                    #print i[0] , i[1]
                    filee = ("presence.db")
                    self.conn = sqlite3.connect(filee)
                    self.cur = self.conn.cursor()
                    self.cur.execute(
                        "INSERT INTO presence(name_prenome,classe,data , presence ) VALUES('%s','%s','%s','%s')  " % (
                            str(i[0]), classe, str(time_new), str(i[1])))

                    self.conn.commit()
                Qt.QMessageBox.information(self, u'تم حفظ'  , u'تم حفظ جميع البيانات')

            else :
                Qt.QMessageBox.critical(self,u'خطأ' , u'الرجاء التاكد من الاختيارات ')

        except Exception, e:
            print str(e)
            Qt.QMessageBox.critical(self, 'erurr', str(e))











# هذا الكلاس تاع فوناتر تاع اضافة طالب جديد


class add_etidient(QtGui.QMainWindow, Ui_MainWindow3):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.betton()
        self.data_add()





    def betton(self):
        self.pushButton.clicked.connect(self.add_new_etidient)


    def data_add(self):
        file = ("C:\Users\hemidi benameur\Desktop\project_\data.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT classe FROM etidient ")
        s = self.cur.fetchall()

        '''
        for i in s:
            if i[0] != None :
                self.comboBox.addItem(i[0])
                
        '''
        ls = []
        ms = []
        for i in s:
            ls.append(i[0])
        for H in ls:
            if H not in ms:
                ms.append(H)

        for i in ms:
            if i != None:
                self.comboBox.addItem(i)


    def add_new_etidient(self):
        #connect avec data base

        try :

            file = ("C:\Users\hemidi benameur\Desktop\project_\data.db")
            self.conn  =  sqlite3.connect(file)
            self.cur = self.conn.cursor()




            #get le information que fonetre
            nome_ = self.lineEdit.text()
            prenome_ =  self.lineEdit_2.text()
            age_ = self.lineEdit_3.text()
            classe = self.comboBox.currentText()
            numbre_ = self.lineEdit_5.text()


            # اولا نقوم بحذف  الفراغات الزائدة في كل نص بستعمال الدالة في الكلاس تاع اضافة قسم جديد

            delet_text  =  add_new_classe()
            nome = delet_text.delet_text(nome_)
            prenome = delet_text.delet_text(prenome_)
            age = delet_text.delet_text(age_)
            numbre = delet_text.delet_text(numbre_)


            # التاكد ان الطالب غير موجود في قاعدة البانات

            self.cur.execute("SELECT * FROM etidient  WHERE classe = '%s' " % classe)
            car =  self.cur.fetchall()
            #  لتاكد من عدم وجود اسم التلميد في القائمة اصلا

            flag2 = 0
            for i in car  :
                if age == i[0] and  nome == i[1] and prenome == i[2]  :
                    Qt.QMessageBox.critical(self , u'موجود بالفعل ' , u'تم اظافة هذا الطالب في هذا القسم سابقا')
                    flag2 = 1
                    break

            #  التاكد من عدم وجود فراغ
            flag3 = 0
            if age == '' or nome == '' or prenome == ''  :
                flag3 = 1
                Qt.QMessageBox.critical(self, u'خطأ ', u'لم يتم ادخال كافة المعلومات')

            #    التاكد ان عدد الطلاب في القسم اقل من 36 طالب
            flag4 = 0
            self.cur.execute("SELECT nome , prenom FROM etidient WHERE classe = '%s' " % classe )
            car2 = self.cur.fetchall()
            if  len(car2) > 36 :
                flag4 = 1
                Qt.QMessageBox.critical(self, u'خطأ ', u'عدد الطلاب هو 36 و هو الحد الاقصى')



            if flag2 + flag3 + flag4 == 0  :



                    #Qt.QMessageBox.critical(self, u'خطأ ', u'لم يتم ادخال كافة المعلومات')




                    #ajeuté les information sur data base

                    #cur.execute("CREATE TABLE etidient (age TEXT , nome TEXT , prenom TEXT , numbre INTEGER , classe TEXT)")
                self.cur.execute('''INSERT INTO etidient(age , nome , prenom , numbre , classe ) VALUES('%s' , '%s' , '%s' , '%s' , '%s' )''' %(age , nome , prenome , numbre , classe))

                self.conn.commit()


                    #self.cur.execute("SELECT * FROM etidient ")
                    #Is  = self.cur.fetchall()
                    #for i  in Is  :
                    #    print i



                Qt.QMessageBox.information(self , u'تم الحفظ'  , u'تم حفظ معلومات الطالب'  )
        except IndexError :
            Qt.QMessageBox.critical(self,u'خطأ' ,u'هناك خطأ ما ')


#  اضافة قسم جديد
class add_new_classe(QtGui.QMainWindow, Ui_MainWindow4):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.betton()


    def betton(self):
        self.pushButton.clicked.connect(self.classe)


    # هذه الدالة تحذف الفراغات الموجودة في اخر  النص و اوله

    def delet_text(self , text):
        f = text
        i = 0
        while len(f)> 0 :
            if f[-1] == ' ':
                f = f[:-1]
            else :
                break

        while len(f) > 0 :
            if f[0] == ' ' :
                f = f[1:]
            else :
                break
        return  f



    def classe(self):
        file = ("C:\Users\hemidi benameur\Desktop\project_\data.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()

        classes_ = self.lineEdit.text()


        # هذه الدالة تحذف الفراغات في اخر  النص

        classes =  self.delet_text(classes_)

        self.cur.execute("SELECT classe FROM etidient")
        car  =  self.cur.fetchall()

        # 5 عدد الاقسام لا يتجاوز
        classes_ = []
        max_classe = 10
        for  i in car  :
            if  i not in classes_ :
                classes_.append(i)

        if len(classes_) > max_classe :
            Qt.QMessageBox.critical(self,u'خطأ', u'وصلت للحد الاقصى من عدد الاقسام ')

        else :




            # سحب جميع الاقسام و اذا كان القسم موجود في قاعدة البانات اضف واحد للفلاق

            flag  =  0
            for i in car  :
                if classes == i[0] :
                    flag  =  1
                    break
            #  اذا كان الكلاس فارغ اظهر خطأ تنبيه
            if  classes == '' or classes == None    :
                Qt.QMessageBox.critical(self, u'خطأ', u'لم تقم باضافة اي شيئ ')


            # اذا كان الفلاق يساوي واحد معناه القسم موجود بالفغل
            elif flag == 1 :

                Qt.QMessageBox.critical(self, u'خطأ', u'هذا القسم موجود بالفعل ')

            #     احفظ القسم في قاعدة البانات و اظهر رسالة تاكيد الحفظ

            else :


                self.cur.execute('''INSERT INTO etidient(classe) VALUES('%s')''' % (classes))

                self.conn.commit()

                Qt.QMessageBox.information(self, u'تنبيه', u'تم اضافة القسم بنجاح ')




            #   هذي الحكاية بش كي ندخل قسم جديد يتحدث مباشرة في نافذة الكومبوبكس
            get_class_myapp = MyApp()
            get_class_myapp.combobox_classe()





############################################### update #################################################
############################################### update #################################################
############################################### update #################################################
############################################### update #################################################
########################################################################################################
#  كلاس تعديل الاقسام و الطلاب
class update(QtGui.QMainWindow, Ui_MainWindow6):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.combobox_classe()
        self.button()
        self.return_nome_classe()



    def button(self):

        self.pushButton.clicked.connect(self.delet_class)
        self.pushButton_2.clicked.connect(self.update_nome_clase)



    def combobox_classe(self):
        file = ("data.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT classe FROM etidient " )

        s = self.cur.fetchall()
        """
        for  i  in  s  :
            if i[0] != None :
                self.comboBox.addItem(i[0])
        """
        ls = []
        ms = []
        for i in s:
            ls.append(i[0])
        for H in ls:
            if H not in ms:
                ms.append(H)

        for i in ms:
            if i != None:
                self.comboBox.addItem(i)


    def return_nome_classe(self):
        classe = self.comboBox.currentText()
        return  classe


    def delet_class(self):

        ##############################################
        file = ("presence.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()
        #################################################
        file2 = ("data.db")
        self.conn2 = sqlite3.connect(file2)
        self.cur2 = self.conn2.cursor()
        ################################################
        classe =  self.comboBox.currentText()



        a = 'Voulez-vous vraiment supprimer la section: ' + classe
        self.resulta = Qt.QMessageBox.question(self,'Confirmer' , a , 'Yes' , 'Non' )
        print self.resulta


        if self.resulta ==  False  :
            self.cur.execute("DELETE FROM presence WHERE classe = '%s' " % classe)
            self.conn.commit()
            self.cur2.execute("DELETE FROM etidient WHERE classe = '%s' " % classe)
            self.conn2.commit()
            Qt.QMessageBox.information(self,'Suppression terminée' , 'La section a ete supprimée')



        #self.cur.execute("DELETE FROM presence WHERE class = '%s' " % classe )




    def update_nome_clase(self):

        self.window5 = update_nome_classe()
        self.window5.show()








    # ceet  fonction  pour  reuturn nome de classe qui il ya comoBox pour utilise autre class mithode





    #    هذا الكلاس تابع لكلاس التعديلات

class update_nome_classe(QtGui.QMainWindow, Ui_MainWindow7):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.button()
        #self.update_()
        self.update_()

    def button(self):
        self.pushButton.clicked.connect(self.confirm_update)


    def update_(self):

        N =  update()
        classe = N.return_nome_classe()
        self.lineEdit.setText(classe)


    def confirm_update(self):
        file = ("presence.db")
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()
        #################################################
        file2 = ("data.db")
        self.conn2 = sqlite3.connect(file2)
        self.cur2 = self.conn2.cursor()
        ################################################
        N = update()
        classe = N.return_nome_classe()
        ####################################
        new_nome = self.lineEdit.text()

        if  new_nome != classe  and new_nome != ''   :
            delet_text = add_new_classe()
            nome = delet_text.delet_text(new_nome)
            self.cur.execute("UPDATE presence SET classe = '%s' WHERE classe = '%s' ;" % (nome , classe) )
            self.conn.commit()
            print 'non'
            print classe
            print nome










if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())