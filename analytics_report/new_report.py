# Python libraries
from fpdf import FPDF
from datetime import datetime, timedelta

# Local imports 
from daily_counts import plot_daily_count_states, plot_daily_count_countries
from time_series_analysis import plot_states, plot_countries
from create_case_maps import plot_usa_case_map, plot_global_case_map
from helper import get_state_names, get_country_names, Mode

WIDTH = 210
HEIGHT = 297

def create_title(day, pdf):
	pdf.set_font('Arial', 'B', 16)
	pdf.ln(60)
	pdf.write(5, f"Analytics Report")
	pdf.ln(10)
	pdf.set_font('Arial', '', 16)
	pdf.write(4, f'{day}')
	pdf.ln(5)

def create_report(day, filename="report.pdf"):
	pdf = FPDF()
	states = ['Massachusetts', 'New Hampshire']
	# First page
	pdf.add_page()
	pdf.image('./resources/letterhead_cropped.png', 0, 0, WIDTH)
	#pdf.set_font('Arial', 'B', 16)
	#pdf.cell(40,10, 'Hello World!')
	create_title(day, pdf)

	plot_usa_case_map("./usa_cases.png", day=day)
	prev_days = 250
	plot_states(states, days=prev_days, filename="./cases.png", end_date=day)
	plot_states(states, days=prev_days, mode=Mode.DEATHS, filename="./deaths.png", end_date=day)

	pdf.image("./usa_cases.png", 5, 90, WIDTH-20)
	pdf.image("./cases.png", 5, 200, WIDTH/2-10)
	pdf.image("./deaths.png", WIDTH/2, 200, WIDTH/2-10)



	pdf.add_page()

	# Second page
	# Add image to pdf
	plot_daily_count_states(states, day=day, filename="./cases_day.png")
	plot_daily_count_states(states, day=day, mode=Mode.DEATHS, filename="./deaths_day.png")
	pdf.image("./cases_day.png", 5, 20, WIDTH/2-10)
	pdf.image("./deaths_day.png", WIDTH/2, 20, WIDTH/2-10)

	prev_days = 7
	plot_states(states, days=prev_days, filename="./cases2.png", end_date=day)
	plot_states(states, days=prev_days, mode=Mode.DEATHS, filename="./deaths2.png", end_date=day)
	pdf.image("./cases2.png", 5, 110, WIDTH/2-10)
	pdf.image("./deaths2.png", WIDTH/2, 110, WIDTH/2-10)

	prev_days = 30
	plot_states(states, days=prev_days, filename="./cases3.png", end_date=day)
	plot_states(states, days=prev_days, mode=Mode.DEATHS, filename="./deaths3.png", end_date=day)
	pdf.image("./cases3.png", 5, 200, WIDTH/2-10)
	pdf.image("./deaths3.png", WIDTH/2, 200, WIDTH/2-10)


	pdf.add_page()

	plot_global_case_map("./global_cases.png", day=day)

	countries = ['US', 'India', 'Brazil']
	prev_days = 7
	plot_countries(countries, days=prev_days, filename="./cases4.png", end_date=day)
	plot_countries(countries, days=prev_days, mode=Mode.DEATHS, filename="./deaths4.png", end_date=day)

	pdf.image("./global_cases.png", 5, 20, WIDTH-20)
	pdf.image("./cases4.png", 5, 130, WIDTH/2-10)
	pdf.image("./deaths4.png", WIDTH/2, 130, WIDTH/2-10)


	pdf.output(filename)


if __name__ == '__main__':
	# 11/03/22
	day = (datetime.today() - timedelta(days=1)).strftime("%m/%d/%y").replace("/0", "/").lstrip("0")
	#day = "10/10/20"
	create_report(day)
