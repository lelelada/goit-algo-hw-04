import turtle

def koch_snowflake(t, order, size):
    """
    Рекурсивно малює фрактал "Сніжинка Коха".
    :param t: Об'єкт черепашки (turtle).
    :param order: Поточний рівень рекурсії.
    :param size: Довжина сторони трикутника.
    """
    if order == 0:
        t.forward(size)
    else:
        # Рекурсивний виклик для кожної з чотирьох частин
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def main():
    """
    Основна функція для налаштування середовища та запуску малювання.
    """
    try:
        recursion_level = int(input("Введіть рівень рекурсії (наприклад, 3): "))
        if recursion_level < 0:
            print("Рівень рекурсії не може бути від'ємним.")
            return

        # Налаштування вікна та черепашки
        screen = turtle.Screen()
        screen.title("Сніжинка Коха")
        screen.bgcolor("white")
        
        t = turtle.Turtle()
        t.speed(0)  # Максимальна швидкість
        t.penup()
        t.goto(-150, 90)  # Початкова позиція
        t.pendown()
        t.color("blue")
        t.pensize(2)
        
        # Малюємо 3 сторони сніжинки
        for _ in range(3):
            koch_snowflake(t, recursion_level, 300)
            t.right(120)

        # Приховати черепашку після завершення
        t.hideturtle()
        
        # Залишити вікно відкритим
        screen.mainloop()

    except ValueError:
        print("Будь ласка, введіть ціле число для рівня рекурсії.")

if __name__ == "__main__":
    main()