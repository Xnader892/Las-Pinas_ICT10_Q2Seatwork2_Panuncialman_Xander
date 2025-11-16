from pyscript import document, display

def calculate(event):
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    sci = float(document.getElementById("sci").value)
    math = float(document.getElementById("math").value)
    eng = float(document.getElementById("eng").value)
    fil = float(document.getElementById("fil").value)
    ict = float(document.getElementById("ict").value)
    pe = float(document.getElementById("pe").value)

    gwa = (sci + math + eng + fil + ict + pe) / 6

    message = f"""
Name: {fname} {lname}
Science: {sci}
Math: {math}
English: {eng}
Filipino: {fil}
ICT: {ict}
PE: {pe}

Your general weighted average is {gwa:.2f}
"""
    display(message, target="output")




