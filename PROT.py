# Problem 8 - Translating RNA into Protein
protfile = open("rosalind_prot.txt","r")
string = protfile.read().rstrip()
lcodon = [string[i:i+3] for i in range(0, len(string), 3)]
translated = []

for i in range(len(lcodon)):
    
    if lcodon[i].startswith('AA'):
        if lcodon[i].endswith('U') or lcodon[i].endswith('C'):
            translated.append('N')
        else:
            translated.append('K')
            
    elif lcodon[i].startswith('AC'):
        translated.append('T')  
        
    elif lcodon[i].startswith('AG'):
        if lcodon[i].endswith('U') or lcodon[i].endswith('C'):
            translated.append('S')
        else:
            translated.append('R')
            
    elif lcodon[i].startswith('AU'):
        if lcodon[i].endswith('G'):
            translated.append('M')
        else:
            translated.append('I') 
            
    elif lcodon[i].startswith('CA'):
        if lcodon[i].endswith('U') or lcodon[i].endswith('C'):
            translated.append('H')
        else:
            translated.append('Q')
            
    elif lcodon[i].startswith('CC'):
        translated.append('P')  
        
    elif lcodon[i].startswith('CG'):
        translated.append('R') 
        
    elif lcodon[i].startswith('CU'):
        translated.append('L')  
        
    elif lcodon[i].startswith('GA'):
        if lcodon[i].endswith('U') or lcodon[i].endswith('C'):
            translated.append('D')
        else:
            translated.append('E')
        
    elif lcodon[i].startswith('GC'):
        translated.append('A')  
        
    elif lcodon[i].startswith('GG'):
        translated.append('G')
        
    elif lcodon[i].startswith('GU'):
        translated.append('V') 
        
    elif lcodon[i].startswith('UC'):
        translated.append('S')
        
    elif lcodon[i].startswith('UU'):
        if lcodon[i].endswith('U') or lcodon[i].endswith('C'):
            translated.append('F')
        else:
            translated.append('L')
            
    elif lcodon[i].startswith('UA'):
        if lcodon[i].endswith('U') or lcodon[i].endswith('C'):
            translated.append('Y')
        else:
            break
    
    elif lcodon[i].startswith('UG'):
        if lcodon[i].endswith('U') or lcodon[i].endswith('C'):
                translated.append('C')
        elif lcodon[i].endswith('G'):
                translated.append('W')
        else:
            break
            
''.join(translated)
