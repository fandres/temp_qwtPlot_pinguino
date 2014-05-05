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

#-------------------------------------------------------------------------------
# Principal
#-------------------------------------------------------------------------------
# Crear una clase para nuestra ventana principal
# Crear una clase para nuestra ventana principal
class Principal(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        # Esto es siempre igual.
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
    

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