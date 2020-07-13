from PyQt5.Qt import *
import sys
app=QApplication(sys.argv)

w=QWidget()
w.resize(800,800)
w.move(200,200)

labe=QLabel(w)
labe.setText("hello")

w.show()
sys.exit(app.exec_())