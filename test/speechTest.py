import unittest


class SpeechTest(unittest.TestCase):
    def test_Programacao(self):
        """Can it convert the audio to Programacao?"""
        self.assertEqual(convertSpeech("programacao.wav", "pt-BR"), "programação")

if __name__ == '__main__':
    unittest.main()
