import dataflows

OverseasFlows = dataflows.Flow(
    dataflows.load('../Archive/Input2/table2.csv'),
    dataflows.validate(),
    dataflows.printer(),
    dataflows.dump_to_path('../data/out2')


)

if __name__ == '__main__':
    OverseasFlows.process()