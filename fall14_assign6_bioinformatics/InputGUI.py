'''
Get necessary user input from the user.

There is NO need to modify this file.

Created on Sep 16, 2013

@author: rcd
'''
import os
import tkFileDialog
import Tkinter
import Bioinformatics2 as StudentWork

expected = ''

def getFileAsString (dataFile):
    results = dataFile.read().strip()
    dataFile.close()
    return results

def getFile ():
    global expected
    dataFile = tkFileDialog.askopenfile(initialdir=os.getcwd())
    expected = getFileAsString(open(dataFile.name.replace('dna', 'protein')))
    return dataFile

def showText (output):
    text.config(state=Tkinter.NORMAL)
    text.delete(1.0, Tkinter.END)
    text.insert(Tkinter.END, output)
    text.config(state=Tkinter.DISABLED)

def showInput ():
    showText(getFileAsString(getFile()))

def checkOutput (data, actual, expected):
    results = []
    message = ''
    toCheck = zip(data.split('\n'), actual.split('\n'), expected.split('\n'))
    for (d, a, e) in toCheck:
        if a == e:
            message = 'You Rock!'
        elif len(a) == 0 and len(e) > 0:
            message = 'There is a valid region --- keep looking'
        elif len(a) < len(e):
            message = 'Too short --- not longest?'
        elif len(a) > len(e):
            message = 'Too long --- not first region?'
        elif 'X' in a:
            message = ''.join([ (' ', x)[x == 'X'] for x in a ]) + ' --- Invalid codon(s)'
        else:
            message = ''.join([ (' ', a[k])[a[k] != e[k]] for k in range(len(a)) ]) + ' --- Differences'
        results.append('\n'.join(['Input:\t' + d, 'Result:\t' + a, 'Expected:\t'+ e, message]))
    return results

def translate ():
    data = text.get(1.0, Tkinter.END)
    actual = StudentWork.translateDNAtoProtein(data)
    report = checkOutput(data, actual, expected)
    showText('\n\n'.join(report))


# initialize the window
root = Tkinter.Tk()
frame = Tkinter.Frame(root)
frame.grid()
# establishing text box
text = Tkinter.Text(frame, bd=4, width=80, height=20)
text.grid(row=0, columnspan=4)
# file prompt button
btn1 = Tkinter.Button(frame, text="Choose File", command=showInput)
btn1.grid(row=1, column=1)
btn2 = Tkinter.Button(frame, text="Translate and Check", command=translate)
btn2.grid(row=1, column=2)

root.mainloop()
