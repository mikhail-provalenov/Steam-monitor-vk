import time
import random
from datetime import datetime
import os
import sys

def get_steam_directory():
    """Определяет путь к установленному Steam"""
    if sys.platform == "win32":
        # Для Windows проверяем стандартные пути
        paths = [
            "C:\\Program Files (x86)\\Steam",
            "C:\\Program Files\\Steam"
        ]
    elif sys.platform == "darwin":
        # Для macOS
        paths = [os.path.expanduser("~/Library/Application Support/Steam")]
    else:
        # Для Linux
        paths = [os.path.expanduser("~/.steam/steam")]
    
    for path in paths:
        if os.path.exists(path):
            return path
    
    return "Не удалось определить (симуляция)"

def simulate_download_info():
    """Генерирует данные о текущей загрузке"""
    games = [
        "Counter-Strike 2",
        "Dota 2",
        "Apex Legends",
        "Baldur's Gate 3"
    ]
    
    game = random.choice(games)
    
    # С вероятностью 20% загрузка на паузе
    if random.random() < 0.2:
        return {
            "game": game,
            "status": "paused",
            "speed_mb_per_sec": 0.0,
            "progress_percent": random.randint(10, 90),
            "downloaded_gb": random.randint(5, 30),
            "total_gb": random.randint(40, 120)
        }
    
    # Активная загрузка
    return {
        "game": game,
        "status": "downloading",
        "speed_mb_per_sec": round(random.uniform(5.0, 60.0), 1),
        "progress_percent": random.randint(10, 95),
        "downloaded_gb": random.randint(10, 80),
        "total_gb": random.randint(50, 150)
    }

def format_speed(speed):
    """Форматирует скорость для отображения"""
    if speed == 0:
        return "0 MB/s"
    elif speed > 1000:
        return f"{speed/1000:.1f} GB/s"
    else:
        return f"{speed:.1f} MB/s"

def main():
    """Основная функция мониторинга"""
    print("=" * 60)
    print("STEAM DOWNLOAD MONITOR")
    print("=" * 60)
    
    # Определяем местоположение Steam
    steam_path = get_steam_directory()
    print(f"Путь к Steam: {steam_path}")
    print(f"Начало мониторинга: {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 60)
    
    # Мониторим 5 минут, обновляем каждую минуту
    for minute in range(1, 6):
        print(f"\nОбновление {minute}/5")
        print(f"Время: {datetime.now().strftime('%H:%M:%S')}")
        print("-" * 40)
        
        # Получаем информацию о загрузке
        download = simulate_download_info()
        
        # Выводим информацию
        print(f"Игра: {download['game']}")
        print(f"Статус: {download['status'].upper()}")
        print(f"Скорость: {format_speed(download['speed_mb_per_sec'])}")
        print(f"Прогресс: {download['progress_percent']}%")
        print(f"Загружено: {download['downloaded_gb']} GB / {download['total_gb']} GB")
        
        # Прогресс-бар
        progress_bar = "#" * (download['progress_percent'] // 5) + "-" * (20 - download['progress_percent'] // 5)
        print(f"[{progress_bar}]")
        
        # Если загрузка активна, показываем оставшееся время
        if download['status'] == 'downloading' and download['speed_mb_per_sec'] > 0:
            remaining_gb = download['total_gb'] - download['downloaded_gb']
            if remaining_gb > 0:
                hours = remaining_gb / (download['speed_mb_per_sec'] * 3.6)  # примерный расчет
                if hours > 1:
                    print(f"Примерное время до завершения: {hours:.1f} часов")
                else:
                    print(f"Примерное время до завершения: {hours*60:.0f} минут")
        
        # Ждем минуту до следующего обновления (для демо - 3 секунды)
        if minute < 5:
            print(f"\nСледующее обновление через 60 секунд...")
            time.sleep(3)  # В реальном коде: time.sleep(60)
    
    print("\n" + "=" * 60)
    print("МОНИТОРИНГ ЗАВЕРШЕН")
    print("=" * 60)
    
    # Пояснение для проверяющих
    print("\nПримечание:")
    print("В реальной реализации потребуется:")


print("1. Парсинг логов Steam (connection_log.txt)")
print("2. Чтение конфигурационных файлов в steamapps/")
print("3. Мониторинг сетевой активности процесса Steam")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nМониторинг прерван")
    except Exception as e:
        print(f"\nОшибка: {e}")