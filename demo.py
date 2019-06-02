import stackprinter

import parkrun


stackprinter.set_excepthook()

inputs = {
    'hh': 'hh-2019-05-11-tabs.txt',
    'tw': 'tw-2019-06-01-tabs.txt',
}

for infile in inputs.values():
    results = parkrun.importResults(
        infile, skiprows=12, skipfooter=38, report=True
    )

    parkrun.print_stats(results)

    # parkrun.time_hist(results, style='ggplot').show()
    parkrun.ageGrade_hist(results, style='ggplot').show()
