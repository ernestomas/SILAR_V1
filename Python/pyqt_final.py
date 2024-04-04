from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import serial
import numpy as np

ser=serial.Serial('COM7',9600)

def window():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')              #'Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion'
    widget = QWidget()

    b = QPushButton()
    b.setText("How to use it")


    b.clicked.connect(showdialog)
    widget.setWindowTitle("SILAR Controller v2.0")
    widget.setWindowIcon(QIcon(r"D:\Escuela\Investigacion\SILAR\PyQt5\logo2.png)"))

    label_main = QLabel("PhotoVoltaics Researchs Laboratory")
    label_position = QLabel("Beakers Positions:")
    label_initial = QLabel("Sense:")
    label_cycles = QLabel("Number of Cycles:")
    label_sample = QLabel("Sample Length (cm):")
    label_beaker = QLabel("Beaker Height (cm):")
    label_liquid = QLabel("Liquid Height (cm):")
    label_dip_length = QLabel("Dip Length (cm):")
    label_dip_sp = QLabel("Dip Speed (mm/s):")
    label_dip_dn = QLabel("Dip Duration (sec):")
    #label_dry_dn = QLabel("Dry Duration (sec):")
    label_Pos_init = QLabel("Initial height (cm):")

    '''qp = QPalette()
    qp.setColor(QPalette.ButtonText, Qt.black)
    qp.setColor(QPalette.Window, Qt.black)
    qp.setColor(QPalette.Button, Qt.gray)
    app.setPalette(qp)'''

    pos1 = QCheckBox("1")
    pos2 = QCheckBox("2")
    pos3 = QCheckBox("3")
    pos4 = QCheckBox("4")
    pos5 = QCheckBox("5")
    pos6 = QCheckBox("6")
    pos7 = QCheckBox("7")
    pos8 = QCheckBox("8")

    def ChangedAction1():
        if pos1.checkState() == 0:
            bk1.hide()
            lq1.hide()
            dl1.hide()
            ds1.hide()
            dd1.hide()
        elif pos1.checkState() ==2:
            bk1.show()
            lq1.show()
            dl1.show()
            ds1.show()
            dd1.show()
    
    def ChangedAction2():
        if pos2.checkState() == 0:
            bk2.hide()
            lq2.hide()
            dl2.hide()
            ds2.hide()
            dd2.hide()
        elif pos2.checkState() ==2:
            bk2.show()
            lq2.show()
            dl2.show()
            ds2.show()
            dd2.show()

    def ChangedAction3():
        if pos3.checkState() == 0:
            bk3.hide()
            lq3.hide()
            dl3.hide()
            ds3.hide()
            dd3.hide()
        elif pos3.checkState() ==2:
            bk3.show()
            lq3.show()
            dl3.show()
            ds3.show()
            dd3.show()

    def ChangedAction4():
        if pos4.checkState() == 0:
            bk4.hide()
            lq4.hide()
            dl4.hide()
            ds4.hide()
            dd4.hide()
        elif pos4.checkState() ==2:
            bk4.show()
            lq4.show()
            dl4.show()
            ds4.show()
            dd4.show()

    def ChangedAction5():
        if pos5.checkState() == 0:
            bk5.hide()
            lq5.hide()
            dl5.hide()
            ds5.hide()
            dd5.hide()
        elif pos5.checkState() ==2:
            bk5.show()
            lq5.show()
            dl5.show()
            ds5.show()
            dd5.show()
    
    def ChangedAction6():
        if pos6.checkState() == 0:
            bk6.hide()
            lq6.hide()
            dl6.hide()
            ds6.hide()
            dd6.hide()
        elif pos6.checkState() ==2:
            bk6.show()
            lq6.show()
            dl6.show()
            ds6.show()
            dd6.show()

    def ChangedAction7():
        if pos7.checkState() == 0:
            bk7.hide()
            lq7.hide()
            dl7.hide()
            ds7.hide()
            dd7.hide()
        elif pos7.checkState() ==2:
            bk7.show()
            lq7.show()
            dl7.show()
            ds7.show()
            dd7.show()

    def ChangedAction8():
        if pos8.checkState() == 0:
            bk8.hide()
            lq8.hide()
            dl8.hide()
            ds8.hide()
            dd8.hide()
        elif pos8.checkState() ==2:
            bk8.show()
            lq8.show()
            dl8.show()
            ds8.show()
            dd8.show()
    
    pos1.stateChanged.connect(ChangedAction1)
    pos2.stateChanged.connect(ChangedAction2)
    pos3.stateChanged.connect(ChangedAction3)
    pos4.stateChanged.connect(ChangedAction4)
    pos5.stateChanged.connect(ChangedAction5)
    pos6.stateChanged.connect(ChangedAction6)
    pos7.stateChanged.connect(ChangedAction7)
    pos8.stateChanged.connect(ChangedAction8)
    


    def iniciar():
        pos_value=np.array([0,0,0,0,0,0,0,0])
        if pos1.isChecked():
            pos_value[0]=1
        if pos2.isChecked():
            pos_value[1]=1
        if pos3.isChecked():
            pos_value[2]=1
        if pos4.isChecked():
            pos_value[3]=1
        if pos5.isChecked():
            pos_value[4]=1
        if pos6.isChecked():
            pos_value[5]=1
        if pos7.isChecked():
            pos_value[6]=1
        if pos8.isChecked():
            pos_value[7]=1

        bk = np.array([bk1.value(),bk2.value(),bk3.value(),bk4.value(),bk5.value(),bk6.value(),bk7.value(),bk8.value()])
        lq = np.array([lq1.value(),lq2.value(),lq3.value(),lq4.value(),lq5.value(),lq6.value(),lq7.value(),lq8.value()])
        dl = np.array([dl1.value(),dl2.value(),dl3.value(),dl4.value(),dl5.value(),dl6.value(),dl7.value(),dl8.value()])
        ds = np.array([ds1.value(),ds2.value(),ds3.value(),ds4.value(),ds5.value(),ds6.value(),ds7.value(),ds8.value()])
        dd = np.array([dd1.value(),dd2.value(),dd3.value(),dd4.value(),dd5.value(),dd6.value(),dd7.value(),dd8.value()])
        #dyd = np.array([dyd1.value(),dyd2.value(),dyd3.value(),dyd4.value(),dyd5.value(),dyd6.value(),dyd7.value(),dyd8.value()])
        ds = 23.567312537886814*ds
        ds = ds.astype(int)
        altura=h_init.value()+3.9-sample.value()-lq+dl
        pos_value = cero(pos_value)
        choque = lq+8.5+sample.value()-dl
        choque = choque[pos_value].tolist()
        bk_2 = bk[pos_value].tolist()
        p=0
        for i in range(len(pos_value)):
                if choque[i]<=12.1: 
                    p=1
                    msg=QMessageBox()
                    msg.setWindowTitle("Warning")
                    msg.setText("El brazo de la grúa chocará con el fin de carril")
                    msg.setIcon(QMessageBox.Warning)
                    x=msg.exec_()
                    return

        if p==0:
            ser.write((f"{pos_value}/{(0.367774117921984+23.567312537886814*altura[pos_value]).astype(int).tolist()}/{dd[pos_value].tolist()}/{ds[pos_value].tolist()}/{init.currentText()}/{cycle.value()}/{len(pos_value)}").encode('ascii'))
            print((f"{pos_value}/{(0.367774117921984+23.567312537886814*altura[pos_value]).astype(int).tolist()}/{dd[pos_value].tolist()}/{ds[pos_value].tolist()}/{init.currentText()}/{cycle.value()}/{len(pos_value)}").encode('ascii'))


    init = QComboBox()
    init.addItems(["FORWARD","BACKWARD"])
    h_init = QDoubleSpinBox()

    cycle = QSpinBox()

    sample = QDoubleSpinBox()

    start = QPushButton("Start Process")
    start.clicked.connect(iniciar)

    bk1 = QDoubleSpinBox()
    bk1.hide()
    bk1.setValue(10.0)
    bk2 = QDoubleSpinBox()
    bk2.hide()
    bk2.setValue(10.0) 
    bk3 = QDoubleSpinBox()
    bk3.hide()
    bk3.setValue(10.0)
    bk4 = QDoubleSpinBox()
    bk4.hide()
    bk4.setValue(10.0)
    bk5 = QDoubleSpinBox()
    bk5.hide()
    bk5.setValue(10.0)
    bk6 = QDoubleSpinBox()
    bk6.hide()
    bk6.setValue(10.0)
    bk7 = QDoubleSpinBox()
    bk7.hide()
    bk7.setValue(10.0)
    bk8 = QDoubleSpinBox()
    bk8.hide()
    bk8.setValue(10.0)
    
    lq1 =  QDoubleSpinBox()
    lq1.hide()
    lq2 =  QDoubleSpinBox()
    lq2.hide()
    lq3 =  QDoubleSpinBox()
    lq3.hide()
    lq4 =  QDoubleSpinBox()
    lq4.hide()
    lq5 =  QDoubleSpinBox()
    lq5.hide()
    lq6 =  QDoubleSpinBox()
    lq6.hide()
    lq7 =  QDoubleSpinBox()
    lq7.hide()
    lq8 =  QDoubleSpinBox()
    lq8.hide()

    dl1 =  QDoubleSpinBox()
    dl1.hide()
    dl2 =  QDoubleSpinBox()
    dl2.hide()
    dl3 =  QDoubleSpinBox()
    dl3.hide()
    dl4 =  QDoubleSpinBox()
    dl4.hide()
    dl5 =  QDoubleSpinBox()
    dl5.hide()
    dl6 =  QDoubleSpinBox()
    dl6.hide()
    dl7 =  QDoubleSpinBox()
    dl7.hide()
    dl8 =  QDoubleSpinBox()
    dl8.hide()
    
    ds1 =  QDoubleSpinBox()
    ds1.hide()
    ds2 =  QDoubleSpinBox()
    ds2.hide()
    ds3 =  QDoubleSpinBox()
    ds3.hide()
    ds4 =  QDoubleSpinBox()
    ds4.hide()
    ds5 =  QDoubleSpinBox()
    ds5.hide()
    ds6 =  QDoubleSpinBox()
    ds6.hide()
    ds7 =  QDoubleSpinBox()
    ds7.hide()
    ds8 =  QDoubleSpinBox()
    ds8.hide()
    

    dd1 =  QSpinBox()
    dd1.hide()
    dd2 =  QSpinBox()
    dd2.hide()
    dd3 =  QSpinBox()
    dd3.hide()
    dd4 =  QSpinBox()
    dd4.hide()
    dd5 =  QSpinBox()
    dd5.hide()
    dd6 =  QSpinBox()
    dd6.hide()
    dd7 =  QSpinBox()
    dd7.hide()
    dd8 =  QSpinBox()
    dd8.hide()
    

    #dyd1 =  QSpinBox()
    #dyd2 =  QSpinBox()
    #dyd3 =  QSpinBox()
    #dyd4 =  QSpinBox()
    #dyd5 =  QSpinBox()
    #dyd6 =  QSpinBox()
    #dyd7 =  QSpinBox()
    #dyd8 =  QSpinBox()

    layout = QGridLayout()
    layout.addWidget(label_main,0,0)
    layout.addWidget(b,0,9)
    layout.addWidget(label_position,1,0)
    layout.addWidget(pos1,1,1)
    layout.addWidget(pos2,1,2)
    layout.addWidget(pos3,1,3)
    layout.addWidget(pos4,1,4)
    layout.addWidget(pos5,1,5)
    layout.addWidget(pos6,1,6)
    layout.addWidget(pos7,1,7)
    layout.addWidget(pos8,1,8)

    layout.addWidget(label_initial,2,0)
    layout.addWidget(init,2,1)

    layout.addWidget(label_cycles,3,0)
    layout.addWidget(cycle,3,1)
    layout.addWidget(label_Pos_init,3,3)
    layout.addWidget(h_init,3,4)

    layout.addWidget(label_sample,3,7)
    layout.addWidget(sample,3,8)

    layout.addWidget(label_beaker,5,0)
    layout.addWidget(bk1,5,1)
    layout.addWidget(bk2,5,2)
    layout.addWidget(bk3,5,3)
    layout.addWidget(bk4,5,4)
    layout.addWidget(bk5,5,5)
    layout.addWidget(bk6,5,6)
    layout.addWidget(bk7,5,7)
    layout.addWidget(bk8,5,8)

    layout.addWidget(label_liquid,6,0)
    layout.addWidget(lq1,6,1)
    layout.addWidget(lq2,6,2)
    layout.addWidget(lq3,6,3)
    layout.addWidget(lq4,6,4)
    layout.addWidget(lq5,6,5)
    layout.addWidget(lq6,6,6)
    layout.addWidget(lq7,6,7)
    layout.addWidget(lq8,6,8)

    layout.addWidget(label_dip_length,7,0)
    layout.addWidget(dl1,7,1)
    layout.addWidget(dl2,7,2)
    layout.addWidget(dl3,7,3)
    layout.addWidget(dl4,7,4)
    layout.addWidget(dl5,7,5)
    layout.addWidget(dl6,7,6)
    layout.addWidget(dl7,7,7)
    layout.addWidget(dl8,7,8)

    layout.addWidget(label_dip_sp,8,0)
    layout.addWidget(ds1,8,1)
    layout.addWidget(ds2,8,2)
    layout.addWidget(ds3,8,3)
    layout.addWidget(ds4,8,4)
    layout.addWidget(ds5,8,5)
    layout.addWidget(ds6,8,6)
    layout.addWidget(ds7,8,7)
    layout.addWidget(ds8,8,8)

    layout.addWidget(label_dip_dn,9,0)
    layout.addWidget(dd1,9,1)
    layout.addWidget(dd2,9,2)
    layout.addWidget(dd3,9,3)
    layout.addWidget(dd4,9,4)
    layout.addWidget(dd5,9,5)
    layout.addWidget(dd6,9,6)
    layout.addWidget(dd7,9,7)
    layout.addWidget(dd8,9,8)

    #layout.addWidget(label_dry_dn,10,0)
    #layout.addWidget(dyd1,10,1)
    #layout.addWidget(dyd2,10,2)
    #layout.addWidget(dyd3,10,3)
    #layout.addWidget(dyd4,10,4)
    #layout.addWidget(dyd5,10,5)
    #layout.addWidget(dyd6,10,6)
    #layout.addWidget(dyd7,10,7)
    #layout.addWidget(dyd8,10,8)



    #layout.addWidget(start,11,0)
    #layout.addWidget(QProgressBar(),12,0,10,10)
    layout.addWidget(start,10,0)
    layout.addWidget(QProgressBar(),11,0,10,10)
    layout.setColumnMinimumWidth(1,80)
    layout.setColumnMinimumWidth(2,80)
    layout.setColumnMinimumWidth(3,80)
    layout.setColumnMinimumWidth(4,80)
    layout.setColumnMinimumWidth(5,80)
    layout.setColumnMinimumWidth(6,80)
    layout.setColumnMinimumWidth(7,80)
    layout.setColumnMinimumWidth(8,80)
    layout.setColumnMinimumWidth(9,80)

    widget.setLayout(layout)
    widget.show()
    sys.exit(app.exec_())

def showdialog():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("SILAR Controller Software")
    msg.setInformativeText("This is program has been develop by Jesús Alba and Ernesto Más. Click on the Show Details button for the info about how to use the software")
    msg.setWindowTitle("Help")
    msg.setDetailedText("1. Colocar la primera solucion en la posicion inicial del sistema.")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.buttonClicked.connect(msgbtn)

    retval = msg.exec_()
    print("value")





#def iniciar():
	#ser.write((f"{sentido},{ciclos}").encode('ascii'))
	#ser.close

def msgbtn(i):
    print("button",i.text())


def cero(new):
	new_array=[]
	for i in range(len(new)):
		if new[i]!=0:
			new_array.append(i)
	return new_array



if __name__ == '__main__':
    window()


