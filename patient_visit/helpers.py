import os
import datetime

from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from config.settings import BASE_DIR


def add_to_first_page(canvas, doc):
	canvas.saveState()
	pdfmetrics.registerFont(
		TTFont('Roboto-ThinItalic', os.path.join(BASE_DIR, 'styles', 'fonts', 'Roboto-ThinItalic.ttf')))
	canvas.setFont('Roboto-ThinItalic', 9)
	page_number_text = "%d" % (doc.page)
	visit = f'{doc.title}'
	generated_at = f'Wygenerowano: {datetime.datetime.now().strftime("%d.%m.%Y, %H:%M")}'
	logo = os.path.join(BASE_DIR, 'styles', 'images', 'stethoscope.png')
	canvas.drawImage(logo, 0.7 * inch, 10.75 * inch, width=80, height=40)
	canvas.drawString(0.75 * inch, 0.75 * inch, generated_at)
	canvas.drawString(3.5 * inch, 11 * inch, visit)
	canvas.drawString(7 * inch, 0.75 * inch, page_number_text)
	canvas.restoreState()


def add_to_later_pages(canvas, doc):
	canvas.saveState()
	pdfmetrics.registerFont(
		TTFont('Roboto-ThinItalic', os.path.join(BASE_DIR, 'styles', 'fonts', 'Roboto-ThinItalic.ttf')))
	canvas.setFont('Roboto-ThinItalic', 9)
	page_number_text = "%d" % (doc.page)
	visit = f'Wizyta {doc.title}'
	generated_at = f'Wygenerowano: {datetime.datetime.now().strftime("%d.%m.%Y, %H:%M")}'
	canvas.drawString(0.75 * inch, 0.75 * inch, generated_at)
	canvas.drawString(3.5 * inch, 11 * inch, visit)
	canvas.drawString(7 * inch, 0.75 * inch, page_number_text)
	canvas.restoreState()