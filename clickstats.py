import click
from collections import Counter

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
prompt = "Enter the next number in the list. Press 'q' when finished: "

@click.version_option(version='1.0.4')

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--mean', is_flag=True, help="Calculate the mean.")
@click.option('--mode', is_flag=True, help="Calculate the mode.")
@click.option('--range', is_flag=True, help="Calculate the range.")
#make --rounded_to option nested and indivudual for each function
@click.option('--rounded_to', '-rt', default=2, help='Round mean to this number of decimal places. (default=2)')
def calculate(**kwargs):
	numlist = get_values(prompt)
	click.echo(numlist)
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
	#get_mode = dict(data)
	mode = [k for k, v in data.items() if v == max(list(data.values()))]
	if len(mode) == len(numlist):
		click.echo("No mode found")
	else:
		click.echo("The mode(s) is/are: " + ', '.join(map(str, mode)))
	

if __name__ == '__main__':
	calculate()
