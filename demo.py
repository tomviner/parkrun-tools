import parkrun
import stackprinter

stackprinter.set_excepthook()

infile = r'hh-2019-05-11-tabs.txt'
results = parkrun.importResults(infile, skiprows=12, skipfooter=37, report=True)

parkrun.print_stats(results)
