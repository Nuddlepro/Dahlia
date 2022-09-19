from .mode import Mode
import gui as gui
import lib as lib


class Title(Mode):
    def __init__(self, app, display) -> None:
        self.bg_color = [34, 26, 41]
        super().__init__(app, display)

    def init_gui(self):
        self.gui_list = []
        x_center = lib.WIDTH // 2
        gui.TextBox(
            self.gui_list,
            x_center - 200,
            lib.HEIGHT // 2 - 250,
            400,
            300,
            "DAHLIA",
            "title",
            [0, 0, 0, 0],
        )
        y_pos = lib.HEIGHT // 2 + 100
        gui.Button(
            self.gui_list,
            x_center - 80,
            y_pos,
            140,
            30,
            "Play",
            font=12,
            color=lib.wet_blue,
            func=self.play,
            border_radius=10,
        )
        y_pos += 40
        gui.Button(
            self.gui_list,
            x_center - 80,
            y_pos,
            140,
            30,
            "Levels",
            font=12,
            color=lib.wet_blue,
            func=lambda: self.app.set_mode("level_viewer"),
            border_radius=10,
        )
        y_pos += 40

        gui.Button(
            self.gui_list,
            x_center - 80,
            y_pos,
            140,
            30,
            "Settings",
            font=12,
            color=lib.wet_blue,
            func=lambda: self.app.set_mode("settings"),
            border_radius=10,
        )
        y_pos += 40

        gui.Button(
            self.gui_list,
            x_center - 80,
            y_pos,
            140,
            30,
            "Quit",
            font=12,
            color=lib.wet_blue,
            func=self.app.quit,
            border_radius=10,
        )

    def play(self):
        print("play")
        self.app.selected_level = "level"
        self.app.load_level(self.app.selected_level)

    def active_update(self, dt, mouse, mouse_button, mouse_pressed):
        self.display.fill(self.bg_color)
        super().active_update(dt, mouse, mouse_button, mouse_pressed)
