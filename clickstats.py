import click
from collections import Counter

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
prompt = "Enter the next number in the list. Press 'q' when finished: "

@click.version_option(version='1.0.4')

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--mean', is_flag=True, help="Calculate the mean.")
@click.option('--mode', is_flag=True, help="Calculate the mode.")
@click.option('--range', is_flag=True, help="Calculate the range.")
@click.option('--median', is_flag=True, help="Calculate the median.")
@click.option('--midrange', is_flag=True, help="Calculate the range")
#make --rounded_to option nested and indivudual for each function
@click.option('--rounded_to', '-rt', default=2, help='Round mean to this number of decimal places. (default=2)')
def calculate(**kwargs):
	numlist = get_values(prompt)
	click.echo(sorted(numlist))
	if kwargs['mean']:
		rounded_to = kwargs['rounded_to']
		mean = float(sum(numlist) / max(len(numlist), 1))
		rounded_mean = round(mean, rounded_to)
		click.echo("The calculated mean is: " + str(rounded_mean))
	if kwargs['mode']:
		get_mode(numlist)
	if kwargs['range']:
		rnge = sorted(numlist)[len(numlist) - 1] - sorted(numlist)[0]
		rounded_rnge = round(rnge, rounded_to)
		click.echo("The calculated range is: " + str(rounded_rnge))
	if kwargs['median']:
		get_median(numlist)
	if kwargs['midrange']:
		get_midrange(numlist)

		
def get_values(prompt):
	numlist = []
	while True:
		try:
			num = input(prompt)
			if num == 'q':
				break
			num = float(num)
		except ValueError:
			print("Please enter a valid number")
			continue
		else:
			numlist.append(num)
			continue	
	return numlist

	
def get_mode(numlist):
	data = dict(Counter(numlist))
	mode = [k for k, v in data.items() if v == max(list(data.values()))]
	if len(mode) == len(numlist):
		click.echo("No mode found")
	else:
		click.echo("The mode(s) is/are: " + ', '.join(map(str, mode)))


def get_median(numlist):
	length = len(numlist)
	numlist.sort()
	if length % 2 == 0:
		median1 = numlist[length//2]
		median2 = numlist[length//2 - 1]
		median = (median1 + median2)/2
	else:
		median = round(numlist[length//2], 1)
	click.echo("Median is: " + str(median))

def get_midrange(numlist):
	numlist = sorted(numlist)
	min = numlist[0]
	max = numlist[len(numlist) - 1]
	mi, ma = numlist[0], numlist[len(numlist) - 1]
	midrange = (min + max) / 2
	click.echo("The calculated midrange is " + str(midrange))
	click.echo("The min is " + str(mi) + " and the max is " + str(ma))
	
