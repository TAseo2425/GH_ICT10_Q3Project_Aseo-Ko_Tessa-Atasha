from pyscript import display, document


def team(t):
    document.getElementById('output').innerHTML = ' '
    
    medcert = document.querySelector('input[name="body"]:checked').value
    registration = document.querySelector('input[name="reg"]:checked').value
    section = document.getElementById('section').value

#medical certificate and registration not checked/signed
    if medcert == 'not' and registration == 'not':
        display(f'Obtain a cleared medical certificate and complete the online registration.', target='output')
#registration only one checked
    elif medcert == 'not' and registration == 'signed':
        display(f'Obtain a cleared medical certificate to continue.', target='output')
#medical certificate only one checked
    elif medcert == 'cleared' and registration == 'not':
        display(f'Please complete the online Intramurals registration to continue.', target='output')
#everything signed, emerald section
    elif registration == 'signed' and medcert == 'cleared' and section == 'emerald':
        display(f'Congratulations. You are now in Green Hornets!', target='output')
#everything signed, ruby section
    elif registration == 'signed' and medcert == 'cleared' and section == 'ruby':
        display(f'Congratulations. You are now in Red Bulldogs!', target='output')
#everything signed, sapphire section
    elif registration == 'signed' and medcert == 'cleared' and section == 'sapphire':
        display(f'Congratulations. You are now in Blue Bears!', target='output')
#everything signed, topaz section
    elif registration == 'signed' and medcert == 'cleared' and section == 'topaz':
        display(f'Congratulations. You are now in Yellow Tigers!', target='output')
    else:
        display(f'Please fill all fields.', target='output')




