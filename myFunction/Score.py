def getScore_nilai (nilai):
    if nilai >= 60 and nilai <= 100:
        ket ='lulus'
    else:
        ket ='gagal'
    return ket

def getScore_grade (nilai):
    if nilai >= 90 and nilai <= 100:
        grade = 'Grade A'
    elif nilai >= 70 and nilai <= 89:
        grade = 'Grade B'
    elif nilai >= 60 and nilai <= 69:
        grade = 'Grade C'
    elif nilai >= 30 and nilai <= 59:
        grade = 'Grade D'
    else:
        grade = 'Grade E'
    return grade