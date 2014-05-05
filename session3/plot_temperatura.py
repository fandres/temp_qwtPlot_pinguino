# -*- coding: utf-8 -*-
"""
Created on Fri May  2 11:35:48 2014

@author: fAnDrEs (fabian.salamanca@openmailbox.org)

"""

import os,sys    
# Importar modulo Qt
from PyQt4 import QtCore,QtGui
# Importar el código del modulo compilado UI
from plot_temperaturaUi import Ui_MainWindow
# Importamos modulo pinguino 
import Pinguino
import usb
# 
#from PyQt4.Qwt5.Qwt import QwtPlotGrid
from numpy import arange, sin
from PyQt4 import * 


#------------------------------------------------------------------------------
# Principal
#------------------------------------------------------------------------------
# Crear una clase para nuestra ventana principal
class Principal(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        # Esto es siempre igual.
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        # 
        self.pinguino = Pinguino.Pinguino()
        # Conectamos la senal de click del boton (boton_conectar) con el metodo inicio
        self.connect(self.ui.ui_botonIniciar, QtCore.SIGNAL("clicked()"), self.inicio)
        
    #--------------------------------------------------------------------------
    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        if self.pinguino.pinguinoOpen == None:
            # Cierra la conexcion con el pinguino Correctamente
            self.pinguino.pinguinoClose()
        exit(1)
        
    #--------------------------------------------------------------------------
    @QtCore.pyqtSlot()
    def on_action_Average_triggered(self):
        pass
    
    def inicio(self):
        if self.pinguino.pinguinoOpen() == None:
            print >> sys.stderr, "Unable to open Pinguino device!"
            self.pinguino.pinguinoClose() # Cerrar aplicacion de manera correcta.
        else: 
            # Activamos en la GUI el elemento QWT [qwtPlot],el contenedor groupbox
            # y desactivamos el boton conectar.
            self.ui.ui_qwtPlot.setEnabled(True) 
            self.ui.ui_groupBox.setEnabled(True)
            self.ui.ui_botonIniciar.setEnabled(False)         
            
            self.temperatura()
                    
            # Timer
            ##self.timer = QtCore.QTimer()
            ##self.timer.timeout.connect(self.temperatura)
            ##self.timer.start(500) #se ejecutará la self.temperatura() cada 500 mili segundos 
   
    def average(self):
       pass
   
    def updateBoard(self):
        self.INTERVAL = 100 # intervalo (tiempo) de lectura 
        deg = unichr(176).encode("utf-8")
        self.myString = ''

        # Obtiene los datos de la targeta Pinguino 
        try :
            for i in self.pinguino.pinguinoRead(5, self.INTERVAL):
                if i > 47 and i < 58:    # ANSI 0,1,2,...,9
                    #print "valor actual",i # Debug
                    self.myString += chr(i)
                    #print "actual caracter",chr(i) # Debug
                    #print "total ",self.myString # Debug
                
        except usb.USBError as err:
            pass
        
        #print  "myString completo:",self.myString  #debug
        #print float(self.myString)
        #print type(self.myString) #debug
        #print int(self.myString) #debug
        if len(self.myString) > 0:
            return self.myString
    
    
    def temperatura(self):
        # Obtener promedio ususario
        #promedio = self.average()
        #print self.updateBoard()
        self.tiempo = 60;
        
        if self.updateBoard():
            self.ui.ui_qwtPlot.setTitle("Temperatura en Grados Celcius")
            
            x = arange(1, 17, 0.01)
            #print x #Debug
            
            #test
            Gph = Qwt5.QwtPlotCurve("sin(x)") # se crea  y se nombra la curva
            #self.ui.ui_qwtPlot.insertLegend(Qwt5.QwtLegend(), Qwt5.QwtPlot.BottomLegend) # ojo  Timer Habilita leyendas.             
            
            #Gph.setPen()
            Gph.attach(self.ui.ui_qwtPlot) # se enlaza la curva al plano 
            y = map(sin, x)
            Gph.setData(x, y)
            self.ui.ui_qwtPlot.replot() # redibujar
            self.startTimer(50)
            
    def timerEvent(self, tiempo):
        a = 1        
        print a
        a+= 1
    

#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------
def main():
    # Nuevamente, esto es estándar, será igual en cada
    # aplicación que escribas
    app = QtGui.QApplication(sys.argv)
    # Se crea una instancia de la clase
    ventana=Principal()
    # Se muestra el elemento en pantalla
    ventana.show()
    # Se ejecuta y expera a que termine la aplicación
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()