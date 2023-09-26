#import das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

planilha = pd.read_csv('CADASTRO_IES_2020.CSV', encoding='ISO-8859-1', sep=';', low_memory=False)
print(planilha)

#excluindo e analisando as quantidade de valores nulos após do dropna
planilha.dropna(inplace=True)
valores_nulos = planilha.isnull().sum()
print("Valore nulos:", valores_nulos)

#informações
print(planilha.info())

#inserindo as colunas em variáveis
brancos = planilha ['DOC_EX_BRANCA']
negros = planilha ['DOC_EX_PRETA']
pardos = planilha ['DOC_EX_PARDA']
indigenas = planilha ['DOC_EX_INDÍGENA']

#inserindo em uma só varavel
etnias = [brancos.tolist(), negros.tolist(), pardos.tolist(), indigenas.tolist()]
etnias = pd.DataFrame({'Brancos': brancos, 'Negros': negros, 'Pardos': pardos, 'Indígenas': indigenas})
print(etnias)

#quantidade de pessoas paraca cada etnia
quantidade = 181.344, 7.166, 48.643, 417
print("Quantidade de pessoas de cada etnia: ", quantidade)

#valor total das colunas
quantidade = etnias.sum()

#formatação
quantidade = quantidade.apply(lambda x: f'{x:,}')
print(quantidade)

etnias = ['Brancos', 'Negros', 'Pardos', 'Indígenas']
quantidade = [181344, 7166, 48643, 417]

# Cores para as barras
cores = ['#ffc870', '#723422', '#f8872e', '#A52A2A']

plt.title('Quantidades por etnias')
plt.bar(etnias, quantidade, color=cores)
plt.xlabel('Etnia')
plt.ylabel('Quantidade')
plt.legend()
plt.grid(axis='y', color='black', linestyle='--')

# Mostrar os valores em cima das barras
for i, v in enumerate(quantidade):
    plt.text(i, v, str(v), ha='center', va='bottom')
plt.show()

#Gerar o gráfico de pie
#"pctdistance=" serve para posicionar as porcentagens
plt.pie(quantidade, labels=etnias, autopct='%1.2f%%', pctdistance=0.83, colors=cores)

# Gerar um círculo no meio
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Porcentagem de Etnias')
plt.show()

#inserindo as colunas em variáveis
feminino = planilha ['DOC_EX_FEMI']
masculino = planilha ['DOC_EX_MASC']

genero = feminino, masculino
print(genero)

genero = [feminino.tolist(), masculino.tolist()]
genero = pd.DataFrame({'Coluna feminina': feminino, 'Coluna masculina': masculino})
print(genero)

#valor total das colunas
quantidades = genero.sum()

#formatação
quantidades = quantidades.apply(lambda x: f'{x:,}')
print(quantidades)

generos = ['Feminina', 'Masculino']
quantidades = [153.878, 176.629]  # Valores sem as casas decimais
cor = ['#FFC0CB', '#7FFFD4']

plt.title('Quantidades por gênero')
plt.bar(generos, quantidades, color=cor)
plt.xlabel('Gênero')
plt.ylabel('Quantidades')
plt.legend()
plt.grid(axis='y', color='black', linestyle='--')  # Apenas linhas horizontais

# Adicione os valores como rótulos nas barras
for i, v in enumerate(quantidades):
    plt.text(i, v, str(v), ha='center', va='bottom')
plt.show()

#Gerar o gráfico de pie
#"pctdistance=" serve para posicionar as porcentagens
genero = ['Feminina', 'Masculino']
quantidades = [153878, 176629]

plt.title('Porcentagem de gêneros')
plt.pie(quantidades, labels=genero, autopct='%1.2f%%', pctdistance=0.83, colors=cor)

# Gerar um círculo no meio
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.show()

#Função para adicionar subtítulo com estilo
def add_subtitle(pdf, subtitle):
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 18, subtitle, ln=True, align='c')

#Função para adicionar conteúdo com estilo
def add_content(pdf, content):
    pdf.set_font("Arial", size=13)
    pdf.multi_cell(0, 7, content, align='c', ln=True)

#Função para adicionar imagens
def add_images(pdf, image_paths):
    for image_path in image_paths:
        pdf.add_page()
        pdf.image(image_path, x=0, y=0, w=200)
#Criar um objeto PDF no formato retrato (P)
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()

#Adicionar o título principal
pdf.set_font("Arial", style="B", size=16)
pdf.cell(0, 15, "Cadastro IES 2020", align='C', ln=True)

add_subtitle(pdf, "Gráfico 1: Quantidade de docentes em atividade por etnia")
grafico_1 = (
    "Para o tema da atividade, li a documentação e o gráfico para selecionar quais tipos de dados e gráficos relevantes"
    " iria analisar, em seguida decidi relatar sobre a quantidade e porcentagem de pessoas ativas categorizadas por etnias."
    " Para isso, validei se no documento 'CADASTRO_IES_2020.CSV' olhando as informações e excluindo os valores nulos, fiz uma limpeza nos mesmos."
    " Coloquei os valores das colunas ['DOC_EX_BRANCA'], ['DOC_EX_PRETA'], ['DOC_EX_PARDA'], ['DOC_EX_INDÍGENA'] em variáveis"
    "das categorias brancos, negros, pardos e indígenas. Optei também por incluir em uma única chamada 'etnias' e com isso"
    "validei os valores de cada categoria das colunas citadas e importei para a variável 'quantidades' em seguida, gerei o gráfico de barras."
)
add_content(pdf, grafico_1)

add_subtitle(pdf, "Gráfico 2: Porcentagem de docentes em atividade por etnia" )
grafico_2 = (
    "Ao longo do processo, considerei a importância de mostrar a porcentagem de docentes ativos de cada etnia. "
    " Optei por criar um gráfico de pizza, pois é adequado para exibir porcentagens como iria trabalhar com apenas duas colunas,"
    "fiz o gráfico pizza."
)
add_content(pdf, grafico_2)

add_subtitle(pdf, "Gráfico 3: Quantidade de docentes em atividade por genero")
grafico_3 = (
    "Para incluir mais informações nos dados, decidi criar gráficos em relação aos gêneros sexuais. O processo foi mais simples,"
    "já que precisei de apenas duas colunas ['DOC_EX_FEMI'] e ['DOC_EX_MASC'] fiz o mesmo processo de colocar os valores das colunas"
    "nas variáveis assim gerei o gráfico de barras."
)
add_content(pdf, grafico_3)

add_subtitle(pdf, "Gráfico 4: Porcentagem de docentes em atividade por genero")
grafico_4 = (
  "Para criar o gráfico de pizza dos generos foi algo simples, ja que fiz o mesmo processo do gráfico 2,"
  "o diferencial é que usei apenas duas colunas ['DOC_EX_FEMI'] e ['DOC_EX_MASC']. "
)
add_content(pdf, grafico_4)

#adcionar imagens
image_paths = ['grafico1.png', 'grafico2.png', 'grafico3.png', 'grafico4.png']
add_images(pdf, image_paths)
pdf.output("Cadastro IES 2020.pdf")

print('PDF criado com sucesso!')
