def get_minium(formula="55-50+40"):
    result = 0
    sections = formula.split('-')
    result += sum(map(int, sections[0].split('+')))
    for section in sections[1:]:
        result -= sum(map(int, section.split('+')))
    
    return result

form = input()
print(get_minium(form))