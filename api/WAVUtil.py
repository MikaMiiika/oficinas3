import wave
import struct

#  Recebe uma string de bytes que representa um áudio .wav.
#  Para que o áudio seja reconstruído corretamente os parâmetros devem ser fornecidos:
#  Channels: 1 se Mono; 2 se Stereo;
#  Sample Width ou Bit Depth: Normalmente 2 para Mono e 4 para Stereo. Podem haver exceções.
#  Frame Rate ou Sample Rate: Taxa de amostragem do áudio. Normalmente 44.1kHz
def bytesToWAV(wavInbytes, fileName, channels=1, sampleWidth=2, frameRate=44100):
    fullFileName = "sounds/" + fileName + ".wav"
    wavFile = wave.open(fullFileName, 'wb')
    wavFile.setnchannels(channels)
    wavFile.setsampwidth(sampleWidth)
    wavFile.setframerate(frameRate)
    wavFile.setcomptype('NONE', 'Not Compressed')  # Considera o áudio como não comprimido

    wavFile.writeframesraw(wavInbytes)
    return fullFileName

#  Carrega um arquivo .wav em memória e cria um objeto python wave do tipo READ.
def readWavFile(path):
    return wave.open(path, 'rb')


def tratarAudioPomodoro(stringHex):
    if stringHex is None:
        return []

    listHex = stringHex.split(",")  # Último elemento sempre será uma vírgula.
    lastIndex = len(listHex) - 1

    if listHex[lastIndex] == "":
        del listHex[lastIndex]

    hexBytes = hexStringToHexBytes(listHex)
    return hexBytes


def hexStringToHexBytes(listHex):
    list = b''
    for x in listHex:
        # list += struct.pack('H', int(x, 16))
        if(len(x) == 3):
            x = "0" + x

        list += bytes.fromhex(x)
    return list


def criarArquivoWAV(bytes, frequencia, fullFileName):
    bytes = tratarAudioPomodoro(bytes)
    return bytesToWAV(bytes, fullFileName, 1, 2, frequencia)

def main():
    # wavFile = readWavFile('sample.wav')  #  Lê o áudio .wav e cria um objeto python do tipo wave
    # numberFrames = wavFile.getnframes()  #  Determina a quantidade total de frames do arquivo de áudio
    # wavFileInBytes = wavFile.readframes(numberFrames)  # Lê todos os frames do áudio e retorna uma string de bytes
    # wavFileAgain = bytesToWAV(wavFileInBytes, 'teste1', 1, 1, 22050)  #  Recebe uma string de bytes e cria um objeto python wave
    # print(str(wavFileInBytes))

    list = "13b,13a,139,138,136,135,136,13a,138,13b,13d,13d,13c,13d,13e,13d,13d,13e,13f,13e,13e,13e,13f,13e,13d,13d,13c,13c,13b,13b,13b,13b,13b,13c,13c,13d,13d,13f,13e,13f,13f,13f,13f,13f,13f,13f,13f,13f,13f,13f,13e,13d,13c,13c,13b,13b,13b,13a,139,139,139,138,138,136,136,135,135,136,138,138,139,139,13a,139,13c,13c,13c,13c,13c,13c,13c,13c,13b,13b,13a,139,13a,13a,13a,13a,13b,13c,13c,13d,13d,13d,13d,13d,13d,13c,13c,13c,13c,13b,13b,13b,13a,139,139,139,139,139,138,138,136,135,136,135,134,133,133,133,133,133,133,133,133,133,133,134,134,134,134,134,134,134,134,134,134,134,134,135,134,134,135,135,135,135,135,136,136,136,136,138,138,138,138,136,138,136,136,138,138,138,138,138,138,138,136,136,136,136,136,136,135,135,135,135,135,135,135,135,135,135,135,136,136,136,136,136,136,138,138,136,138,138,139,138,139,139,139,139,139,139,139,139,139,138,138,138,138,136,136,136,136,136,136,136,136,136,136,136,136,138,138,138,139,139,139,13a,13a,13b,13b,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13a,13a,139,139,138,138,138,138,138,136,138,138,136,136,136,136,136,136,135,136,136,136,138,138,139,13a,13b,13b,13b,13b,13c,13c,13b,13c,13b,13b,13b,13b,139,13a,13a,139,13a,13a,13b,13b,13a,13b,13b,13a,13b,13b,13b,13a,13a,13a,13a,139,139,139,136,138,136,135,136,136,136,135,136,136,136,138,138,139,139,13a,13b,13b,13c,13c,13c,13c,13d,13e,13f,13f,13f,13f,13f,13f,13e,13d,13d,13c,13c,13c,13b,13c,13b,13b,13a,13a,13a,13a,13b,13a,13b,13a,13a,13a,13a,13b,13b,13b,13b,13c,13c,13c,13c,13c,13c,13d,13d,13d,13d,13e,13d,13d,13d,13d,13c,13c,13c,13b,13b,13b,13c,13b,13b,13a,13b,13b,13b,13b,13b,13c,13b,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13d,13d,13d,13d,13d,13d,13c,13c,13c,13c,13c,13c,13c,13c,13d,13d,13d,13d,13d,13d,13d,13d,13d,13d,13d,13d,13d,13d,13d,13d,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13d,13c,13d,13d,13d,13d,13e,13e,13d,13d,13e,13d,13d,13d,13c,13c,13c,13c,13c,13c,13c,13c,13c,13d,13d,13d,13d,13c,13c,13c,13c,13c,13d,13d,13e,13d,13d,13d,13d,13d,13d,13c,13d,13d,13c,13d,13d,13d,13d,13d,13d,13d,13d,13d,13c,13c,13c,13b,13b,13b,13b,139,139,139,139,139,13a,13a,13b,13a,13a,13b,13b,13b,13c,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13a,13b,13a,139,13a,13a,13a,13a,13a,13b,13a,13a,13b,13b,13b,13b,13c,13c,13c,13c,13c,13d,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13d,13c,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13d,13c,13c,13c,13d,13c,13c,13c,13c,13c,13c,13c,13c,13d,13c,13d,13d,13d,13d,13d,13c,13c,13c,13d,13c,13c,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13b,13b,13b,13c,13c,13b,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13b,13b,13b,13a,13b,13b,13b,13c,13b,13c,13c,13b,13b,13b,13a,13b,13a,13b,13b,13b,13c,13b,13c,13c,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13c,13c,13c,13c,13c,13c,13c,13b,13b,13b,13c,13b,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13d,13c,13d,13c,13c,13c,13c,13c,13c,13c,13d,13c,13c,13c,13c,13c,13c,13d,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13d,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13d,13c,13d,13d,13c,13c,13d,13d,13d,13c,13d,13d,13d,13d,13d,13d,13d,13d,13d,13d,13e,13d,13d,13d,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13d,13c,13c,13c,13d,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13b,13c,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13c,13c,13c,13c,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13a,13b,13b,13b,13b,13c,13c,13c,13b,13c,13c,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13b,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13d,13c,13c,13c,13d,13c,13c,13c,13b,13c,13b,13c,13b,13b,13c,13c,13c,13b,13b,13c,13b,13c,13c,13c,13c,13c,13c,13c,13d,13d,13c,13d,13d,13c,13c,13c,13c,13d,13c,13c,13c,13c,13d,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13b,13c,13b,13c,13b,13b,13b,13b,13b,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13d,13c,13d,13d,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13c,13c,13b,13b,13b,13c,13c,13c,13c,13c,13c,13c,13b,13c,13b,13c,13b,13c,13c,13c,13c,13b,13b,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13d,13c,13c,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13c,13b,13c,13c,13b,13b,13b,13b,13b,13b,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13d,13c,13c,13c,13c,13d,13c,13c,13d,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13c,13d,13b,13c,13b,13c,13b,13b,13c,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13c,13c,13b,13b,13b,13c,13c,13c,13c,13c,13b,13c,13c,13c,13b,13b,13c,13b,13c,13c,13b,13b,13c,13c,13c,13c,13c,13c,13c,13b,13c,13b,13c,13c,13c,13b,13b,13c,13c,13c,13c,13b,13b,13c,13b,13b,13b,13b,13b,13b,13c,13b,13b,13b,13c,13b,13b,13b,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13b,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13b,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13c,13b,13c,13c,13c,13c,13b,13b,13b,13b,13b,13c,13b,13c,13c,13c,13b,13b,13b,13b,13b,13b,13b,13b,13c,13c,13c,13c,13c,13b,13c,13c,13b,13b,13b,13b,13b,13c,13b,13c,13c,13c,13c,13c,13b,13c,13c,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13d,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13c,13d,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13b,13c,13c,13c,13c,13c,13b,13b,13c,13c,13c,13b,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13c,13b,13c,13d,13e,13d,13c,13c,13c,13a,138,13b,13d,13e,13f,140,13d,13e,13a,13b,138,135,13d,138,13c,146,13f,13e,"
    print("Hex Recebido: " + list)
    lista = tratarAudioPomodoro(list)
    print("Bytes de Saída:" + str(lista))
    t = bytesToWAV(lista, 'teste2', 1, 2, 2000)
    print("Path do Audio: " + t)


# main()
