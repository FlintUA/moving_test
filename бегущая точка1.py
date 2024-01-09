import neopixel
import utime

# Укажите количество светодиодов и пин, к которому подключена лента WS2812B
NUM_PIXELS = 180
PIN = 23  # Пример: используемый GPIO на Raspberry Pi Pico

# Коэффициент яркости (от 0.0 до 1.0, где 0.0 - минимальная яркость, 1.0 - максимальная)
BRIGHTNESS = 0.1

# Инициализация светодиодной ленты с коэффициентом яркости
pixels = neopixel.Neopixel(NUM_PIXELS, 1, PIN, "GRB")

def moving_dot(color_dot, color_background, delay):
    for i in range(NUM_PIXELS):
        pixels.fill(color_background)  # Заливаем фон желтым цветом
        pixels[i] = color_dot          # Устанавливаем точку на текущей позиции
        pixels.show()
        utime.sleep_ms(50)

try:
    while True:
        moving_dot((255, 0, 0), (255, 130, 0), 500)  # Красная точка по желтому фону
except KeyboardInterrupt:
    pixels.fill((0, 0, 0))  # Выключаем все светодиоды перед выходом
    pixels.show()
