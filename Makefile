.PHONY: sq

square:
	manim  -ql project.py square -i  
	mv media/videos/project/400p15/square_ManimCE_v0.18.1.gif ./assets/images/square.gif

rectangle:
	manim  -ql project.py rectangle -i  
	mv media/videos/project/400p15/rectangle_ManimCE_v0.18.1.gif ./assets/images/rectangle.gif