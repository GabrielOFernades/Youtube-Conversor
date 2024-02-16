from pytube import YouTube

opcao = 1

while opcao != 0:

    opcao = int(input("Deseja baixar em qual formato?\n"
                      "[0] - Encerrar\t[1] - Mp3\t[2] - Mp4\nResposta: "))

    if opcao != 0:
        link = input("Digite o link: ")
        conversor = YouTube(link)

        video = conversor.streams.get_highest_resolution()
        audio = conversor.streams.get_audio_only()

        if opcao == 1:
            audio.download()
            print("Audio baixado com sucesso")
        elif opcao == 2:
            video.download()
            print("Video baixado com sucesso")

        else:
            print("Nenhuma opcao selecionada")
