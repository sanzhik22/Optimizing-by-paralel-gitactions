import dataflows

OverseasFlows = dataflows.Flow(
    dataflows.load('../Archive/Input3/business-operations.csv'),
    dataflows.validate(),
    dataflows.printer(),
    dataflows.dump_to_path('../data/out3')


)

if __name__ == '__main__':
    OverseasFlows.process()