def shift():
            x1, y1, x2, y2 = self.canvas2.bbox("marquee")
            if (x2 < 0 or y1 < 0):  # reset the coordinates
                x1 = self.canvas2.winfo_width()
                y1 = 20
                self.canvas2.coords("marquee", x1, y1)
            else:
                self.canvas2.move("marquee", -20, 0)
            self.canvas2.after(1000 // self.fps, shift)
            ############# Main program ###############

        self.canvas2 = tk.Canvas(root, bg='black')
        self.canvas2.pack(fill="both", expand=1)
        if self.paused == True:
            self.text5 = "(::)Advanced Music player with cool features(::)"
        else:
            self.text5 = "(::)Advanced Music player with cool features(::)"
        self.text3 = self.canvas2.create_text(0, -2000, text=self.text5, font=('consolas', 15, 'bold','italic'),
                                              fill='white', tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = self.canvas2.bbox("marquee")
        width = 620
        height = 1
        self.canvas2['width'] = width
        self.canvas2['height'] = height
        self.fps = 2  # Change the fps to make the animation faster/slower
        shift()
