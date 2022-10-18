import inquirer
from rich.console import Console
from rich.table import Table

MONDAY = ((6, 6), 0.7)
WEDNESDAY = ((7, 5), 0.75)
FRIDAY = ((8, 4), 0.8)
SATURDAY = ((10, 3), 0.85)

def validate_one_rep_max(answers, current):
	if not current.isnumeric():
		raise errors.ValidationError("", reason="Enter a number dumbwit")
	return True

def round_nearest_multiple(number_to_round, base):
	return base * round(number_to_round / base)

print("Welcome to Smolov Jr.")

questions = [
	inquirer.Text("one_rep_max", message="What is your one rep max (KG)?", validate=validate_one_rep_max),
	inquirer.List("increments",
		message = "What increment would you like to use per week (KG)?",
		choices = [2.5, 5, 7.5, 10],
		),
]

answers = inquirer.prompt(questions)
one_rep_max = int(answers["one_rep_max"])
increments = answers["increments"]

print(f"Alright, your one rep max is {one_rep_max} kg and you have chosen a weekly increment of {str(increments)} kg.")
print("Here is your 3 week long hell: \n")

for i in range(3):
	table = Table(title="Week " + str(i + 1))

	rows = [
		["Monday", MONDAY[0][0], MONDAY[0][1], round_nearest_multiple(one_rep_max * MONDAY[1] + i * increments, 2.5)],
		["Wednesday", WEDNESDAY[0][0], WEDNESDAY[0][1], round_nearest_multiple(one_rep_max * WEDNESDAY[1] + i * increments, 2.5)],
		["Friday", FRIDAY[0][0], FRIDAY[0][1], round_nearest_multiple(one_rep_max * FRIDAY[1] + i * increments, 2.5)],
		["Saturday", SATURDAY[0][0], SATURDAY[0][1], round_nearest_multiple(one_rep_max * SATURDAY[1] + i * increments, 2.5)],
	]

	rows = [
		[str(x) for x in rows[0]],
		[str(x) for x in rows[1]],
		[str(x) for x in rows[2]],
		[str(x) for x in rows[3]],
	]

	columns = ["Day", "Sets", "Reps", "Weight [KG]"]
	
	for column in columns:
		table.add_column(column)

	for row in rows:
		table.add_row(*row, style="bright_red")

	console = Console()
	console.print(table)
	print("\n")