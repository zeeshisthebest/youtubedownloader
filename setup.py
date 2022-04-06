from distutils.core import setup
import py2exe
options = {'includes': ['tkinter', 'pytube', 'radiobutton', 'tkinter.filedialog',
                        'tkinter.messagebox', 'pytube.exceptions',
                        'threading']}  # Here you must add list of identified modules

setup(windows=['main.py'])  # Here mention your driver python script name
