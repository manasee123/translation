import subprocess
import sys
import sqlite3
from tkinter import *

root=Tk()
top=Frame(root)
top.grid(row=0,column=0)

con = sqlite3.connect('langcodes.db')
db =con.cursor()

def createlangdb():
    try:
        db.execute("CREATE TABLE langcode (code text, lang text)")
    except sqlite3.OperationalError:
        pass
    else:
        lang = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
        }
        for key in lang:
            con.execute('insert into langcode values (?,?)',(key,lang[key]))
        con.commit()
        
def modcheck():
    try:
     import googletrans
    except ModuleNotFoundError:
        print("googletrans module is being installed. Please wait a minute.")
        subprocess.call([sys.executable, "-m", "pip", "install", "googletrans"])
        print("Module installed")

def detect(testtext):
    from googletrans import Translator
    tr = Translator()
    detected_lang=tr.detect(testtext)
    db.execute("SELECT lang from langcode WHERE code=?",(detected_lang.lang,))
    #print("Detected language :",db.fetchall()[0][0])
    from tkinter import messagebox
    outputtext = "Detected Language: " + db.fetchall()[0][0]
    messagebox.showinfo("Information",outputtext)
    
    

def translate(testtext):
    from googletrans import Translator
    tr = Translator()
    from tkinter import simpledialog
    lang_dest = simpledialog.askstring("Input", "Enter language to be translated into: ",
                                parent=root)
    translated_text = tr.translate(testtext,dest=lang_dest)
    outputtext = "Translated Text: " + translated_text.text
    from tkinter import messagebox
    messagebox.showinfo("Information",outputtext)

createlangdb()
modcheck()
label=Label(root,text="Enter text",bg="white")
entry1=Entry(root)
label.grid(row=4,column=5)
entry1.grid(row=4,column=6)
button1=Button(root,text="Detect",command=lambda: detect(entry1.get()),bg="white")
button2=Button(root,text="Translate",command=lambda: translate(entry1.get()),bg="white")
button1.grid(row=6,column=5)
button2.grid(row=6,column=7)

