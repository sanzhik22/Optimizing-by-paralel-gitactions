import dataflows

OverseasFlow = dataflows.Flow(
    dataflows.load('../Archive/Input1/overseas-trade.csv'),
    dataflows.validate(),
    dataflows.printer(),
    dataflows.dump_to_path('../data/out1')


)

if __name__ == '__main__':
    OverseasFlow.process()