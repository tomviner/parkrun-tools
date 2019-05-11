import parkrun
import stackprinter

stackprinter.set_excepthook()

infile = r'hh-2019-05-11.txt'
results = parkrun.importResults(infile,report=True)

parkrun.print_stats(results)

