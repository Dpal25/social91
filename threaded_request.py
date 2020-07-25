import sys
from Parser import Parser
from Calculator import PriceAccumulator
from Sender import Sender

if __name__ == '__main__':
    P = Parser(sys.argv[1])
    S = Sender()
    C = PriceAccumulator()

    # Start threaded request
    S.run(P.get_data(), C)
