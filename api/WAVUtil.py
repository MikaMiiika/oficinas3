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

    print("String de HEX: ")
    print(stringHex)

    listHex = stringHex.split(",")  # Último elemento sempre será uma vírgula.
    lastIndex = len(listHex) - 1

    if listHex[lastIndex] == "":
        del listHex[lastIndex]

    listHexInInteger = hexStringToHexInteger(listHex)

    print(bytes(listHexInInteger))
    return bytes(listHexInInteger)


def hexStringToHexInteger(listHex):
    list = [int(x) for x in listHex]
    print("List de Integer: ")
    print(list)
    return list

def main():
    # wavFile = readWavFile('sample.wav')  #  Lê o áudio .wav e cria um objeto python do tipo wave
    # numberFrames = wavFile.getnframes()  #  Determina a quantidade total de frames do arquivo de áudio
    # wavFileInBytes = wavFile.readframes(1)  # Lê todos os frames do áudio e retorna uma string de bytes
    # wavFileAgain = bytesToWAV(wavFileInBytes, 'teste1', 1, 1, 22050)  #  Recebe uma string de bytes e cria um objeto python wave
    # string = struct.unpack('b', wavFileInBytes)
    # print(string)
    # print(str(wavFileInBytes))
    list = "187,167,246,158,"
    lista = tratarAudioPomodoro(list)
    print("Bytes da Lista: ")
    print(lista)
    # t = bytesToWAV(lista, 'teste2')
    # print(t)

main()
