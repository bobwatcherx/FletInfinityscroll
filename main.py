from flet import *
import threading


class State:
	i = 0

# DEFINED STATED
s = State()
sem = threading.Semaphore()



def main(page:Page):


	def myscroll(e:OnScrollEvent):
		# YOU SEE SCROLL VALUE IN PRINT
		print(e)
		# YOU SEE IN print VALUE OF pixels 
		# pixels is you scroll down value
		# and max_scroll_extent is you scroll but end scroll

		if e.pixels >=e.max_scroll_extent - 100:
			if sem.acquire(blocking=False):
				try:
					# AND IF you Scrollbar to End
					# i add new Data in down 
					for b in range(0,10):
						body.controls.append(
						Container(
							bgcolor="white",
							border_radius=30,
							margin=margin.only(left=30,right=30),
							padding=10,
							content=Text(f"you data - {s.i}",size=20)

							)
						)
						s.i +=1
						body.update()
				finally:
					sem.release()




	body = Column(
		width=page.window_width,
		height=500,
		scroll="always",
		on_scroll_interval=0,
		on_scroll=myscroll

		)

	# NOW I LOOp from 0 to 20 
	# in body

	for x in range(0,20):
		body.controls.append(
			Container(
				bgcolor="white",
				border_radius=30,
				margin=margin.only(left=30,right=30),
				padding=10,
				content=Text(f"you data - {s.i}",size=20)

				)
			)

		s.i += 1

	page.add(
		Column([
		Text("Infinity scroll",weight="bold",size=30),
		Container(
			bgcolor="blue",
			padding=10,
			content=body
			)
			])

		)

flet.app(target=main)
