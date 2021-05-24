from datetime import datetime
from moon.terminal_ui import TerminalUi
from moon.custom_image import CustomImage
from moon.dialamoon import Moon



moon = Moon()
moon.set_moon_phase()
moon.save_to_disk('moon')
print(moon.moon_datetime_info)

ui = TerminalUi()
ui.set_moon_phase() #defaults to today's date
print(ui.moon_datetime_info)
ui.show()
