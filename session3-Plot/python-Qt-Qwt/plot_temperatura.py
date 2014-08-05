#! /usr/bin/python
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
from PyQt4.Qwt5.Qwt import QwtLegend, QwtPlot, QwtPlotGrid, QwtPlotCurve
from PyQt4.Qt import Qt, QPen
#from PyQt4.Qwt5.anynumpy import arange, zeros, concatenate # Requerido para manejo con numpy



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
        #Centramos el frame
        self.centrar()
        
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
            self.ui.ui_botonIniciar.setEnabled(False)   
            self.ui.action_Average.setEnabled(True)
            self.tiempo_maximo = 60
            self.time = 0
            self.grafico()
            # Creamos y abrimos los ficheros
            self.fichero = open('Datos.txt','w')
            self.fichero2 = open('DatosAvg.txt','w')
            self.startTimer(50)


#-------------------------------------------------------------------------------
    def centrar(self):
            screen = QtGui.QDesktopWidget().screenGeometry() # obtiene resolucion del usuario
            size =  self.geometry() 
            self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
            
#-------------------------------------------------------------------------------

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
                    #print "total ",s# Timer
            ##self.timer = QtCore.QTimer()
            ##self.timer.timeout.connect(self.temperatura)
            ##self.timer.start(500) #se ejecutará la self.temperatura() cada 500 mili segundos elf.myString # Debug
                
        except usb.USBError as err:
            pass
        
        #print  "myString completo:",self.myString  #debug
        #print float(self.myString)
        #print type(self.myString) #debug
        #print int(self.myString) #debug
        
        # Retorna valor de temperatura
        if len(self.myString) > 0:
            #print "Retorno updateBoard: ",self.myString # Debug
            self.termperatura = (5*int(self.myString)*100)/1023 # Conversión a Grados celcius.
            return True
    
    
    
    def grafico(self):
        # Obtener promedio ususario
        #promedio = self.average()
        #print self.updateBoard()
        # FORMATEO
        self.ui.ui_qwtPlot.setTitle("Temperatura en Grados Celcius") # Titulo Grafico
        self.ui.ui_qwtPlot.setCanvasBackground(Qt.white) #  Color de fondo del frame Qwtpot
        self.ui.ui_qwtPlot.insertLegend(QwtLegend(),QwtPlot.BottomLegend) # Habilita las leyendas(centradas) con el «nombre» de cada curva 
        self.grafica = QwtPlotCurve("Canal 1") # Asignando nombre a la curva creada(grafica)
        self.grafica.setPen(QPen(Qt.red, 2)) # (color,taman^o )
        # OBTENER VALORES
# Con numpy
#        self.equis = arange(0, self.tiempo_maximo, 1) 
#        self.valores = zeros(len(self.equis)) # Arreglo a ser llenado con los valores obtenidos
        self.equis = range(0,self.tiempo_maximo,1)
        self.valores = []
        self.promedio = 0
        self.promedioMints = 0.0
        self.promedios = []
        self.minutos = 0
        self.grafica.attach(self.ui.ui_qwtPlot)# se enlaza la curva al plano 
        # GRILLA
        grilla = QwtPlotGrid()
        grilla.setPen(QPen(Qt.gray))
        grilla.enableX(1)
        grilla.enableXMin(1)
        grilla.enableY(1)
        grilla.enableYMin(1)
        grilla.attach(self.ui.ui_qwtPlot)
        # OTROS
        #self.grafica.setPen(Qt.red) # Color
        #self.ui.ui_qwtPlot.setAxisTitle(QwtPlot.yLeft,"Temperatura")
        
            
    def timerEvent(self, tiempo):
        if self.updateBoard():
            self.time+= 1
            #print "tiempo: ",self.time # Debug
# Con numpy
#        if self.tiempo_maximo > self.time :
#            self.valores[self.time] = self.termperatura
#        else:
#            self.valores =  concatenate((self.valores[1:],[self.termperatura]),1)
        if self.tiempo_maximo > self.time : # Si los datos no superan los 60 datos.
            self.valores.append(self.termperatura)
        else : #si se superan los 60 datos se elimina el dato del indice 0 y se agrega el nuevo dato.
            self.valores = self.valores[1:]
            self.valores.append(self.termperatura)
            # CALCULO PROMEDIO ultimos 60 datos
            self.promedio = reduce(lambda x,y: y+x,self.valores)
            self.promedio = self.promedio/60
            self.ui.ui_lcd1Min.display(self.promedio) #mostramos el promedio en el LCD 1Min
            if self.time % 60 == 0 :
                self.promedios.append(self.promedio)
                #print"Promedios",self.promedios # Debug
                self.minutos += 1
                self.fichero.write(str(self.promedio)+"\n")
                #print "minutos",self.minutos # Debug
                if self.minutos == 2 : # 2 cambiar por average
                    self.minutos = 0
                    self.promedioMints = reduce(lambda x,y: y+x, self.promedios)
                    self.promedioMints = self.promedioMints*1.0/len(self.promedios)
                    self.promedios = []
                    self.ui.ui_lcdAvg.display(self.promedioMints)
                    self.fichero2.write(str(self.promedio)+"\n")
        #print self.valores # Debug
        self.grafica.setData(self.equis,self.valores)
        self.ui.ui_qwtPlot.replot() # redibujar

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
    #Cerramos los fichero
    ventana.fichero.close()
    ventana.fichero2.close()

if __name__ == "__main__":
    main()