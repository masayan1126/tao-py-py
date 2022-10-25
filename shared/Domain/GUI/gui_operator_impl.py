from __future__ import annotations
from dataclasses import dataclass
from time import sleep
import pyautogui as pgui
import pyperclip
from shared.Domain.GUI.gui_operator import GUIOperator


@dataclass
class GUIOperatorImpl:
    def click(
        self,
        x: int,
        y: int,
        duration: int,
        wait_time: float = None,
        loop_count: int = 1,
    ) -> GUIOperator:

        if loop_count > 1:
            for i in range(loop_count):
                pgui.click(x=x, y=y, duration=duration)
        else:
            pgui.click(x=x, y=y, duration=duration)

        if wait_time:
            self.wait(wait_time)

        return self

    def pressKey(self, key_name: str) -> None:
        pgui.press(key_name)

    def scroll(self, amount: int) -> None:
        pgui.scroll(amount)

    def shortcut(
        self,
        key1: str,
        key2: str = None,
        key3: str = None,
        wait_time: float = None,
        loop_count: int = 1,
    ) -> None:

        if loop_count > 1:
            if key2 and key3:
                for i in range(loop_count):
                    pgui.hotkey(
                        key1, key2, key3, interval=0.25
                    )  # Macだとintervalで間隔を指定しないと動作しない
            elif key2:
                for i in range(loop_count):
                    pgui.hotkey(key1, key2, interval=0.25)
            elif key2 is None:
                for i in range(loop_count):
                    pgui.hotkey(key1, interval=0.25)

        else:
            if key2 and key3:
                pgui.hotkey(
                    key1, key2, key3, interval=0.25
                )  # Macだとintervalで間隔を指定しないと動作しない
            elif key2:
                pgui.hotkey(key1, key2, interval=0.25)
            elif key2 is None:
                pgui.hotkey(key1, interval=0.25)

        if wait_time:
            self.wait(wait_time)

    def copy(self, string: str, wait_time: float = None) -> None:
        pyperclip.copy(string)

        if wait_time:
            self.wait(wait_time)

    def get_position(self) -> tuple[int]:
        return pgui.position()

    def wait(self, wait_time: float) -> None:
        sleep(wait_time)
