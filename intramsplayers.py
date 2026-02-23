from pyscript import display, document

def intramsplayers(t):
    document.getElementById('output').innerHTML = ' '

    players = ['1. ASEO, TESSA YSABELLE M.',
'2. BATAC, ANAKIN MIGUEL Q.',
'3. CALANGLANG, NERIZA A.',
'4. DE GUZMAN, VITO ANTONIO O.',
'5. DEE, AARON JAMES G.',
'6. DOLOR, HARVEY WAYNE B.',
'7. GALVEZ, SELENA M.',
'8. GARCES, ADRIANNA M.',
'9. GROSPE, JILLIAN C.',
'10. HIZON, EDUARDO ALONSO M.' ,
'11. INTALAN, MARGO ZERA F.',
'12. KO, ATASHA SOLEIL R.',
'13. LAGMAN, ALIJAH RAIN',
'14. LAW, MARCUS CHRISTIAN P.',
'15. MACABAGO, SITTIE AINAH M.',
'16. MARTINEZ, EUAN JUSTIN L.',
'17. MEDINA, KELSEY CLAIRE L.',
'18. MENDOZA, MICHAELA YSABELLE C.',
'19. MERGAL, MANUEL JACINTO G.',
'20. NGO, SETH GARETT G.',
'21. PADOJINOG, SOFIA LAURENCE F.',
'22. RIVERA, BENIGNO IGNACIO J.',
'23. SHRESTHA, ISHAN JUSTICE Q.',
'24. UY, JENNIFER LORRAINE S.',
'25. YAO, FRANCESCA JEAN K.']

#displays players:
    for players in players:
        display(f'{players}', target='output')
    



