def área(largura, comprimento):
    return largura * comprimento

largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o comprimento: '))

print(f'A área de um terreno {largura}m po {comprimento}m é: {área(largura, comprimento)}m².')
