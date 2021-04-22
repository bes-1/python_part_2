# link to blocks: https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=dz1_1_python.drawio#R7VxZc9s2EP4tfdBM%2ByAPAfDSo2ipaaZpx63bSfyUASlYYkoRCkTZUn59ARAUwUOHrYO6XmBgcS12Fwt8S8gtdD%2Bef2B4MvqDDkjUgsZg3kK9FoSu7fJUEBYpwXRhShiycJCSQE54DH8QRTQUdRYOyLTQMKE0SsJJkRjQOCZBUqBhxuhrsdkzjYqzTvCQVAiPAY6q1M%2FhIBmpZUEnp%2F9GwuEomxnYnbRmjLPGaiXTER7QV42E%2Bi10zyhN0tx4fk8iIbtMLn1kGDBqt7%2B%2F%2FPXP%2FMn65v7tsnY62K9v6bJcAiNx8u6hXzofv05%2Bf%2Fjw8vlfz%2F5kffyzD8M2QGptySITGBlw%2BakiZcmIDmmMo35O9RidxQMihjV4KW%2FzidIJJwJO%2FEaSZKGMAc8SykmjZBypWjIPky%2Bi%2B52lSk9aTW%2BuRpaFRVaIE7bQOonik16Xd5OlrF%2B6PrGokj1sEKZqN6UzFpA1ElTGkWA2JMmadnBpMXynETomnEnej5EIJ%2BFLkTmsbH64bJfrlWeUat%2BgZsXkC45maqYWF06nJ1LPaHHRu06W56kn037FNHLFC129jsKEPE6wFM8rdx5FJaspCUvI%2FB2ir4pKjbLcj8ohIVV8zXc3yJqMtJ1tGwcSLjBve2i3PQS33EOoyT0E6%2FeQTL00tWRqytSVuyqjQ0Or8rIGPO1lKW%2FsyWY8A7S%2BfZk3srxsrJpBrcqSeSTzSGvsSfq9Nlc6b1dtdy6oFuQCMfz0T1CxZX7sTUSWaxtHEYnokOExN4oJYSGXLGHluoe8YpOPeA7nJLszHNJngE7RZwBQ4zTcYzoNq1GfoXmM3H%2Bcl89AW%2FoMs0mf4TapZXBFWnaa1DKqngzQjhLhIxkpqN%2F%2BPhNowXumcdJ%2BxuMw4oLsCn8ObTyeSIEiZKYq9hkO46lAIjSmlQay072qnUoPuxye54bqr2SDV8e1fPg4%2BG8oDa4d0IiylBk29H%2BGlrWcoZT%2FpWYicRJa2dmlHXHyePH8JfeSHc4CP2YMPp3ij0s9ZbHINidLARap1yJTIbigIjhfCc64yW6N7Pxa2eE3yqyMfkZ07M%2BmzSEf4II7aBUuMrDuItNx7qzqVWYJivbv%2F%2BxzAUCHPq52vWyorg805OzkiNct3l7t8q00PR5Vr1yZXcbwQms2EQ2mq%2Bdx6qfJTSMdMDeU5RLfbztmLarq7gZtFNrqaeBriaqQTDvayDragtpclqJfJCAqxVAaD6LY9ejazGBqSQdcHElRcjgKh7G4WXCxSEkLoYUBjrqqYhwOBqnnIdPwB%2FblUMIpqG3Bx7W8ltUTY3FnMz2GEkrO3KpqAdUo4WCOHICKoG%2Bo9E0HgLMlXgFGvWUcB7CARg%2FsS8ClW%2BvZalLPzg2YrgGmPyk4tZGZIwkFx4PNAOWG9d480dEWvAmTN82htPjgDPgUG2GLAMdtL5zqXvCVpe1Dg6cWhUHZLT3DTqcQgunUw6feWiB7ESAKlT7t1YEo85ggClY%2F%2BlxkrGtnCLPfYNe%2BAlLZbt5%2FRGrZPU0drVl%2Fq8%2F%2B5WE7FUO7hNBU%2BX2PaTQdmwIrnn5cdHAKgWJwCjUdnIJnGZyy3JYWtmgbdwZwWutjF7KkbczjeHNr24iG22REAzb61u69kasO1I3g%2FG0ANvoQL2PzFtaqC2utQFdYVHFWBDeGrxeCcwFeZummb54C8AI1MVb92%2BMFIy%2FLOrEbAqpexa70HcLOh3Q9NjNRw9jMrd1s%2B8dm8IbN6kFB6YmIVeeCj4rN4DViM9Msel6zac8Lq%2BZ%2BpZ5356txw0%2FAzPp5DvoGDK5%2BQF34QHAMV89TUPwtjz5d5Qc7ytWv%2BKBxgSeA7Z7cCVADB6%2FkBm53TuwcQM7pnAPG2nOgoYdFm0MrdjPnR3qwHezmDle87%2BxWLtHphq0%2BUDvJ3x47B%2Fw2wYv5%2FxZI9ZD%2FgwbU%2Fx8%3D

'''
По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
равнобедренным или равносторонним.
'''

a = int(input("Введите длину стороны a = "))
b = int(input("Введите длину стороны b = "))
c = int(input("Введите длину стороны c = "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
elif a != b and a != c and b != c:
    print("Треугольник разносторонний")
elif a == b == c:
    print("Треугольник равносторонний")
else:
    print("Треугольник равнобедренный")

