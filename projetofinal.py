import os
from random import shuffle
from time import sleep


def resposta_certa():
    while True:
        resposta = input('Qual a sua resposta? ').lower().strip()
        if resposta in ('a', 'b', 'c', 'd'):
            return resposta
        print("\nResposta inválida. Por favor, escolha uma das opções: a, b, c ou d.\n")


def salvar_ranking():
    with open("ranking_geral.txt", "w", encoding="utf-8") as arquivo:
        for i, jogador in enumerate(sorted(ranking, key=lambda point: point['pontuacao'], reverse=True), start=1):
            linha = f"{jogador['player']} sua pontuação foi: {jogador['pontuacao']},00 R$ e sua colocação foi o {i}º lugar\n"
            arquivo.write(linha)


def carregar_ranking():
    global ranking
    ranking = []
    try:
        with open("ranking_geral.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.split(" sua pontuação foi: ")
                nome = partes[0]
                pontos_str = partes[1].split(",00 R$")[0]
                try:
                    pontos = int(pontos_str)
                    ranking.append({"player": nome, "pontuacao": pontos})
                except ValueError:
                    continue
    except FileNotFoundError:
        ranking = []


def limpar_tela():
  os.system("cls" if os.name == "nt" else "clear")

def menu():
  while True:
      limpar_tela()
      print(" " * 5, "SHOW DO MILHÃO", " " * 10)
      print("=" * 10, "MENU", "=" * 10)
      print("1. Jogar")
      print("2. Ver Ranking")
      print("3. Sair")
      print("=" * 26)


      while True:
          opcao = input("Escolha uma opção: ").strip()
          if opcao == "1":
              jogar()
              break
          elif opcao == "2":
              ver_ranking()
              break
          elif opcao == "3":
              print("Encerrando o programa. Até logo!")
              exit()
          else:
              print("Opção inválida. Tente novamente.")

def jogar():

  nome = input("Digite seu nome de usuário: ")
  lucros = [0, 100, 250, 500, 1000, 1500, 2000, 2500, 5000, 10000, 15000, 25000, 50000, 100000, 150000, 250000,
            500000, 1000000]
  acumulado = 0
  acertos = 0


  perguntas_faceis = [
      {
          "pergunta": "qual é a capital do brasil?",
          "opções": ["a) rio de janeiro", "b) são paulo", "c) brasília", "d) salvador"],
          "resposta": "c"
      },
      {
          "pergunta": "qual planeta é conhecido como o planeta vermelho?",
          "opções": ["a) vênus", "b) marte", "c) júpiter", "d) saturno"],
          "resposta": "b"
      },
      {
          "pergunta": "quem escreveu o romance dom casmurro?",
          "opções": ["a) machado de assis", "b) josé de alencar", "c) jorge amado", "d) clarice lispector"],
          "resposta": "a"
      },
      {
          "pergunta": "quantos jogadores, contando com o goleiro, compõem um time de futebol em campo?",
          "opções": ["a) 10", "b) 11", "c) 12", "d) 13"],
          "resposta": "b"
      },
      {
          "pergunta": "o que significa a sigla ‘onu’?",
          "opções": ["a) organização das nações unidas", "b) organização nacional universitária",
                     "c) ordem nacional unida", "d oração das nações unidas"],
          "resposta": "a"
      },
      {
          "pergunta": "qual elemento químico tem o símbolo ‘o’",
          "opções": ["a) ouro", "b) oxigênio", "c) ósmio", "d) ônix"],
          "resposta": "b"
      },
      {
          "pergunta": "em que continente está localizado o egito?",
          "opções": ["a) ásia", "b) áfrica", "c) europa", "d) américa do sul"],
          "resposta": "b"
      },
      {
          "pergunta": "quantos dias tem um ano bissexto?",
          "opções": ["a) 364", "b) 365", "c) 366", "d) 367"],
          "resposta": "c"
      },
      {
          "pergunta": "qual é a língua mais falada no mundo em número de falantes nativos?",
          "opções": ["a) inglês", "b) espanhol", "c) mandarim (chinês)", "d) árabe"],
          "resposta": "c"
      },
      {
          "pergunta": "quem pintou a obra ‘mona lisa’?",
          "opções": ["a) michelangelo", "b) leonardo da vinci", "c) raphael", "d) vincent van gogh"],
          "resposta": "b"
      },
      {
          "pergunta": "qual é o maior animal terrestre vivo?",
          "opções": ["a) baleia-azul", "b) elefante africano", "c) girafa", "d) rinoceronte-branco"],
          "resposta": "b"
      },
      {
          "pergunta": "qual é o maior oceano da terra?",
          "opções": ["a) atlântico", "b) índico", "c) pacífico", "d) ártico"],
          "resposta": "c"
      },
      {
          "pergunta": "quem escreveu a peça teatral hamlet?",
          "opções": ["a) william shakespeare", "b) victor hugo", "c) charles dickens", "d) machado de assis"],
          "resposta": "a"
      },
      {
          "pergunta": "quantos ossos possui o corpo humano adulto (aproximadamente)?",
          "opções": ["a) 205", "b) 206", "c) 208", "d) 210"],
          "resposta": "b"
      },
      {
          "pergunta": "em qual país nasceu o jogador de futebol pelé?",
          "opções": ["a) argentina", "b) brasil", "c) portugal", "d) uruguai"],
          "resposta": "b"
      },
      {
          "pergunta": "qual é o país mais populoso do mundo?",
          "opções": ["a) estados unidos", "b) índia", "c) china", "d) rússia"],
          "resposta": "b"
      },
      {
          "pergunta": "qual é a capital da alemanha?",
          "opções": ["a) munique", "b) berlim", "c) paris", "d) viena"],
          "resposta": "b"
      },
      {
          "pergunta": "quem foi a primeira pessoa a pisar na lua?",
          "opções": ["a) yuri gagarin", "b) neil armstrong", "c) buzz aldrin", "d) alan shepard"],
          "resposta": "b"
      },
      {
          "pergunta": "qual é a fórmula química da água?",
          "opções": ["a) h2o", "b) co2", "c) o2", "d) h2o2"],
          "resposta": "a"
      },
      {
          "pergunta": "quantas cores há tradicionalmente no arco-íris?",
          "opções": ["a) 5", "b) 6", "c) 7", "d) 8"],
          "resposta": "c"
      }
  ]
  perguntas_medias = [
      {
          "pergunta": "qual é a moeda oficial do japão?",
          "opções": ["a) iene", "b) dólar", "c) yuan", "d) euro"],
          "resposta": "a"
      },
      {
          "pergunta": "quem assumiu a presidência do brasil em 1985, após o fim da ditadura?",
          "opções": ["a) tancredo neves", "b) josé sarney", "c) fernando collor", "d) itamar franco"],
          "resposta": "b"
      },
      {
          "pergunta": "em que ano foi promulgada a atual constituição federal do brasil?",
          "opções": ["a) 1985", "b) 1988", "c) 1990", "d) 1992"],
          "resposta": "b"
      },
      {
          "pergunta": "qual destes países não faz parte do mercosul?",
          "opções": ["a) chile", "b) argentina", "c) brasil", "d) uruguai"],
          "resposta": "a"
      },
      {
          "pergunta": "quem compôs a música do hino nacional brasileiro?",
          "opções": ["a) heitor villa-lobos", "b) francisco manuel da silva", "c) antônio carlos jobim",
                     "d) camargo guarnieri"],
          "resposta": "b"
      },
      {
          "pergunta": "qual é o menor país do mundo em área territorial?",
          "opções": ["a) mônaco", "b) san marino", "c) vaticano", "d) liechtenstein"],
          "resposta": "c"
      },
      {
          "pergunta": "quem escreveu o livro o pequeno príncipe?",
          "opções": ["a) antoine de saint-exupéry", "b) victor hugo", "c) júlio verne", "d) alexandre dumas"],
          "resposta": "a"
      },
      {
          "pergunta": "qual é o maior deserto do mundo em extensão?",
          "opções": ["a) antártica", "b) saara", "c) gobi", "d) kalahari"],
          "resposta": "a"
      },
      {
          "pergunta": "qual é o elemento químico mais abundante no universo?",
          "opções": ["a) hidrogênio", "b) oxigênio", "c) hélio", "d) carbono"],
          "resposta": "a"
      },
      {
          "pergunta": "qual foi o primeiro filme brasileiro indicado ao oscar de melhor filme estrangeiro?",
          "opções": ["a) o pagador de promessas", "b) central do brasil", "c) cidade de deus", "d) tropa de elite"],
          "resposta": "a"
      },
      {
          "pergunta": "quem inventou a lâmpada incandescente?",
          "opções": ["a) nikola tesla", "b) thomas edison", "c) alexander graham bell", "d) benjamin franklin"],
          "resposta": "b"
      },
      {
          "pergunta": "qual destes planetas não possui anéis?",
          "opções": ["a) saturno", "b) júpiter", "c) urano", "d) marte"],
          "resposta": "d"
      },
      {
          "pergunta": "em que cidade fica a sede das nações unidas (onu)?",
          "opções": ["a) genebra", "b) nova iorque", "c) paris", "d) washington, d.c."],
          "resposta": "b"
      },
      {
          "pergunta": "qual o valor aproximado da velocidade da luz no vácuo?",
          "opções": ["a) 300.000 km/s", "b) 150.000 km/s", "c) 30.000 km/s", "d) 300.000 km/h"],
          "resposta": "a"
      },
      {
          "pergunta": "em que ano o homem pisou na lua pela primeira vez?",
          "opções": ["a) 1959", "b) 1969", "c) 1979", "d) 1989"],
          "resposta": "b"
      },
      {
          "pergunta": "em qual país foi realizada a copa do mundo de 1994?",
          "opções": ["a) brasil", "b) estados unidos", "c) frança", "d) japão"],
          "resposta": "b"
      },
      {
          "pergunta": "qual destes países não tem litoral?",
          "opções": ["a) paraguai", "b) peru", "c) chile", "d) argentina"],
          "resposta": "a"
      },
      {
          "pergunta": "quem é o cientista conhecido por formular a teoria da relatividade?",
          "opções": ["a) isaac newton", "b) albert einstein", "c) galileo galilei", "d) stephen hawking"],
          "resposta": "b"
      },
      {
          "pergunta": "o que significa a sigla ‘www’?",
          "opções": ["a) world wide web", "b) web world wide", "c) wide world web", "d) word wide web"],
          "resposta": "a"
      },
      {
          "pergunta": "qual destes elementos é um metal alcalino-terroso?",
          "opções": ["a) sódio (na)", "b) cálcio (ca)", "c) ferro (fe)", "d) ouro (au)"],
          "resposta": "b"
      },
      {
          "pergunta": "qual é a capital da austrália?",
          "opções": ["a) sydney", "b) melbourne", "c) canberra", "d) brisbane"],
          "resposta": "c"
      },
      {
          "pergunta": "em que ano foi lançado o primeiro iphone pela apple?",
          "opções": ["a) 2005", "b) 2007", "c) 2008", "d) 2010"],
          "resposta": "b"
      },
      {
          "pergunta": "qual é o maior planeta do sistema solar?",
          "opções": ["a) saturno", "b) júpiter", "c) urano", "d) netuno"],
          "resposta": "b"
      },
      {
          "pergunta": "o que significa o nome da marca esportiva ‘nike’ na mitologia grega?",
          "opções": ["a) amor", "b) força", "c) sabedoria", "d) vitória"],
          "resposta": "d"
      }
  ]
  perguntas_dificeis = [
      {
          "pergunta": "qual é a montanha mais alta do brasil?",
          "opções": ["a) pico da neblina", "b) pico 31 de março", "c) pedra da neblina", "d) serra do imeri"],
          "resposta": "a"
      },
      {
          "pergunta": "quantos elementos químicos existem atualmente na tabela periódica reconhecidos oficialmente?",
          "opções": ["a) 113", "b) 118", "c) 92", "d) 104"],
          "resposta": "b"
      },
      {
          "pergunta": "quem é conhecido como o 'pai da aviação'?",
          "opções": ["a) karl benz", "b) alberto santos dumont", "c) orville wright", "d) leonardo da vinci"],
          "resposta": "b"
      },
      {
          "pergunta": "qual o nome da partícula carregada positivamente presente no núcleo de um átomo?",
          "opções": ["a) nêutron", "b) próton", "c) elétron", "d) positron"],
          "resposta": "b"
      },
      {
          "pergunta": "quem compôs a música ‘garota de ipanema’?",
          "opções": ["a) heitor villa-lobos", "b) antônio carlos jobim", "c) chico buarque", "d) gilberto gil"],
          "resposta": "b"
      },
      {
          "pergunta": "em qual país está localizada a cordilheira do himalaia?",
          "opções": ["a) nepal", "b) china", "c) índia", "d) paquistão"],
          "resposta": "a"
      },
      {
          "pergunta": "o que significa a sigla ‘dna’?",
          "opções": ["a) doença nuclear atômica", "b) dinamismo neuronal axial", "c) ácido desoxirribonucleico",
                     "d) derrame nervoso agudo"],
          "resposta": "c"
      },
      {
          "pergunta": "qual destes cientistas foi contemporâneo de albert einstein?",
          "opções": ["a) niels bohr", "b) marie curie", "c) isaac newton", "d) galileu galilei"],
          "resposta": "a"
      },
      {
          "pergunta": "em que ano o brasil proclamou sua independência de portugal?",
          "opções": ["a) 1815", "b) 1822", "c) 1825", "d) 1830"],
          "resposta": "b"
      },
      {
          "pergunta": "que fenômeno astronômico ocorre quando a lua fica entre a terra e o sol, bloqueando a luz solar?",
          "opções": ["a) eclipse lunar", "b) eclipse solar", "c) aurora boreal", "d) dilúvio lunar"],
          "resposta": "b"
      },
      {
          "pergunta": "quem escreveu o livro o príncipe?",
          "opções": ["a) nicolau maquiavel", "b) jean-jacques rousseau", "c) thomas hobbes", "d) john locke"],
          "resposta": "a"
      },
      {
          "pergunta": "qual é o maior país em área territorial que não possui litoral?",
          "opções": ["a) cazaquistão", "b) mongólia", "c) paraguai", "d) zimbábue"],
          "resposta": "a"
      },
      {
          "pergunta": "na mitologia nórdica, qual é o deus do trovão?",
          "opções": ["a) zeus", "b) thor", "c) odin", "d) loki"],
          "resposta": "b"
      },
      {
          "pergunta": "qual foi o livro mais vendido no mundo depois da bíblia?",
          "opções": ["a) o peregrino", "b) o pequeno príncipe", "c) dom quixote",
                     "d) harry potter e a pedra filosofal"],
          "resposta": "c"
      },
      {
          "pergunta": "em que ano foi inaugurada a estátua da liberdade?",
          "opções": ["a) 1776", "b) 1886", "c) 1911", "d) 1931"],
          "resposta": "b"
      },
      {
          "pergunta": "quem pintou o teto da capela sistina?",
          "opções": ["a) leonardo da vinci", "b) rafael sanzio", "c) michelangelo buonarroti", "d) donatello"],
          "resposta": "c"
      },
      {
          "pergunta": "qual é a fórmula química da sacarose?",
          "opções": ["a) c6h12o6", "b) c12h22o11", "c) c2h6o", "d) c6h6"],
          "resposta": "b"
      },
      {
          "pergunta": "em que continente fica o país burkina faso?",
          "opções": ["a) ásia", "b) áfrica", "c) europa", "d) américa do sul"],
          "resposta": "b"
      },
      {
          "pergunta": "o que significa a sigla ‘http’?",
          "opções": ["a) hypertext transfer protocol", "b) hyperlink transmission type protocol",
                     "c) high tech transfer protocol", "d) high transmission text protocol"],
          "resposta": "a"
      },
      {
          "pergunta": "quantas vezes a seleção brasileira foi campeã da copa do mundo fifa?",
          "opções": ["a) 4", "b) 5", "c) 6", "d) 3"],
          "resposta": "b"
      }
  ]
  pergunta_final = [
      {
          "pergunta": "qual é o ponto da terra localizado a maior distância do centro do planeta?",
          "opções": ["a) monte everest (himalaia)", "b) monte k2 (himalaia)", "c) monte chimborazo (andes)",
                     "d) monte kilimanjaro (áfrica)"],
          "resposta": "c"
      },
      {
          "pergunta": "qual é a língua oficial do suriname?",
          "opções": ["a) português", "b) inglês", "c) espanhol", "d) holandês"],
          "resposta": "d"
      },
      {
          "pergunta": "qual região do planeta é considerada o deserto mais seco da terra?",
          "opções": ["a) antártida", "b) deserto do saara", "c) deserto de atacama", "d) ártico"],
          "resposta": "a"
      },
      {
          "pergunta": "qual é a maior planície alagável do mundo?",
          "opções": ["a) planície do pantanal", "b) floresta amazônica", "c) everglades", "d) delta do okavango"],
          "resposta": "a"
      }
  ]

  list_facil = perguntas_faceis[:]
  shuffle(list_facil)


  for x in range(0, 6):
      easy = list_facil[x]


      print(easy['pergunta'])
      for y in easy['opções']:
          print(y)


      z = resposta_certa()

      if z == easy['resposta']:
          acertos += 1
          acumulado = lucros[acertos]
          print('Analisando...')
          sleep(0.8)

          while True:
              proximo_valor = lucros[acertos + 1] if acertos + 1 < len(lucros) else lucros[acertos]
              escolhas = input(
                  f'\nParabéns {nome}, você passou! Pode escolher entre parar e levar R$ {lucros[acertos]},00 ou continuar e tentar ganhar R$ {proximo_valor},00. (p/parar | c/continuar): '
              ).lower().strip()

              if escolhas in ('c', 'continuar'):
                  print('Muito bem, vamos lá!')
                  break
              elif escolhas in ('p', 'parar'):
                  print(f'\nParabéns pelos seus R$ {lucros[acertos]},00, sr(a) {nome}')
                  ranking.append({'player': nome, 'pontuacao': acumulado})
                  salvar_ranking()
                  input("\nPressione ENTER para voltar ao menu.")
                  return
              else:
                  print('Opção inválida. Tente novamente.')

      else:
          acumulado = lucros[0]
          print('Analisando...')
          sleep(0.8)
          print('\nPerdeeeeeeeeeeu tudo')
          print(f'Parabéns pelos seus R$ {acumulado},00, sr(a) {nome}')
          ranking.append({'player': nome, 'pontuacao': acumulado})
          salvar_ranking()
          input("\nPressione ENTER para voltar ao menu.")
          return menu()

  list_media = perguntas_medias[:]
  shuffle(list_media)

  for x in range(0, 6):
      medio = list_media[x]

      print(medio['pergunta'])
      for y in medio['opções']:
          print(y)

      z = resposta_certa()

      if z == medio['resposta']:
          acertos += 1
          acumulado = lucros[acertos]
          print('Analisando...')
          sleep(0.8)

          while True:
              proximo_valor = lucros[acertos + 1] if acertos + 1 < len(lucros) else lucros[acertos]
              escolhas = input(
                  f'\nParabéns {nome}, você passou! Pode escolher entre parar e levar R$ {lucros[acertos]},00 ou continuar e tentar ganhar R$ {proximo_valor},00. (p/parar | c/continuar): '
              ).lower().strip()

              if escolhas in ('c', 'continuar'):
                  print('Muito bem, vamos lá!')
                  break
              elif escolhas in ('p', 'parar'):
                  print(f'\nParabéns pelos seus R$ {lucros[acertos]},00, sr(a) {nome}')
                  ranking.append({'player': nome, 'pontuacao': acumulado})
                  salvar_ranking()
                  input("\nPressione ENTER para voltar ao menu.")
                  return menu()
              else:
                  print('Opção inválida. Tente novamente.')

      else:
          acumulado = lucros[0]
          print('Analisando...')
          sleep(0.8)
          print('\nPerdeeeeeeeeeeu tudo')
          print(f'Parabéns pelos seus R$ {acumulado},00, sr(a) {nome}')
          ranking.append({'player': nome, 'pontuacao': acumulado})
          salvar_ranking()
          input("\nPressione ENTER para voltar ao menu.")
          return menu()

  print(f'\nTotal ganho: R$ {acumulado},00')


  list_dificil = perguntas_dificeis[:]
  shuffle(list_dificil)

  for x in range(0,5):
      dificil = list_dificil[x]

      print(dificil['pergunta'])
      for y in dificil['opções']:
          print(y)

      z = resposta_certa()


      if z == dificil['resposta']:
          acertos += 1
          acumulado = lucros[acertos]
          print('Analisando...')
          sleep(0.8)


          while True:
              proximo_valor = lucros[acertos + 1] if acertos + 1 < len(lucros) else lucros[acertos]
              escolhas = input(
                  f'\nParabéns {nome}, você passou! Pode escolher entre parar e levar R$ {lucros[acertos]},00 ou continuar e tentar ganhar o MILHÃO!!! (p/parar | c/continuar): '
              ).lower().strip()

              if escolhas in ('c', 'continuar'):
                  print('Muito bem, vamos lá!')
                  break
              elif escolhas in ('p', 'parar'):
                  print(f'\nParabéns pelos seus R$ {lucros[acertos]},00, sr(a) {nome}')
                  ranking.append({'player': nome, 'pontuacao': acumulado})
                  salvar_ranking()
                  input("\nPressione ENTER para voltar ao menu.")
                  return menu()
              else:
                  print('Opção inválida. Tente novamente.')

      else:
          acumulado = lucros[0]
          print('Analisando...')
          sleep(0.8)
          print('\nPerdeeeeeeeeeeu tudo')
          print(f'Parabéns pelos seus R$ {acumulado},00, sr(a) {nome}')
          ranking.append({'player': nome, 'pontuacao': acumulado})
          salvar_ranking()
          input("\nPressione ENTER para voltar ao menu.")
          return menu()

  list_final = pergunta_final[:]
  shuffle(list_final)

  final = list_final[0]

  print(final['pergunta'])
  for y in final['opções']:
      print(y)


  z = resposta_certa()

  if z == final['resposta']:
      acertos += 1
      acumulado = lucros[-1]
      sleep(1.0)
      print('Analisando...')
      print('PARABÉNS!!! VOCÊ É O GRANDE CAMPEÃAAAO!!!!')
      ranking.append({'player': nome, 'pontuacao': lucros[-1]})
      salvar_ranking()
      input("\nPressione ENTER para voltar ao menu.")
      return menu()

  else:
      acumulado = lucros[0]
      print('Analisando...')
      sleep(1.0)
      print('\nPerdeeeeeeeeeeu tudo, que peninha...')
      print(f'Parabéns pelos seus R$ {acumulado},00, sr(a) {nome}')
      ranking.append({'player': nome, 'pontuacao': acumulado})
      salvar_ranking()
      input("\nPressione ENTER para voltar ao menu.")
      return menu()


def ordem_colocacoes(jogador):
  return jogador['pontuacao']


def ver_ranking():
    limpar_tela()
    print("==== RANKING ====\n")


    if not ranking:
        print("Nenhum jogador participou ainda.")
    else:
        rank_geral = sorted(ranking, key=ordem_colocacoes, reverse=True)
        for i, jogador in enumerate(rank_geral[:10], start=1): 
            print(f"{jogador['player']} sua pontuação foi: {jogador['pontuacao']},00 R$ e sua colocação foi o {i}º lugar")


    input("\nPressione ENTER para voltar ao menu.")

carregar_ranking()
menu()