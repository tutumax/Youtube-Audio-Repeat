import os


def baixar_audio_youtube(url, arquivo_saida):
    os.system(
        f'yt-dlp -f bestaudio --extract-audio --audio-format mp3 -o "temp_audio.%(ext)s" "{url}"')
    print("Arquivos na pasta:", os.listdir())
    if os.path.exists("temp_audio.mp3"):
        return "temp_audio.mp3"
    elif os.path.exists("temp_audio.m4a"):
        os.system('ffmpeg -y -i temp_audio.m4a temp_audio.mp3')
        return "temp_audio.mp3"
    else:
        raise Exception("Falha ao baixar o áudio.")


def repetir_audio(arquivo_audio, vezes, arquivo_saida):
    with open("inputs.txt", "w") as f:
        for _ in range(vezes):
            f.write(f"file '{arquivo_audio}'\n")
    os.system(
        f'ffmpeg -y -f concat -safe 0 -i inputs.txt -c copy "{arquivo_saida}"')
    os.remove("inputs.txt")


if __name__ == "__main__":
    url = input("Cole o url do vídeo do YouTube: ")
    vezes = input("Quantas vezes você quer repetir o áudio? ")
    arquivo_saida = "audio_repetido.mp3"
    temp_audio = baixar_audio_youtube(url, arquivo_saida)
    repetir_audio(temp_audio, vezes, arquivo_saida)
    os.remove(temp_audio)
    print(f"Áudio baixado e repetido {vezes} vezes em: {arquivo_saida}")


