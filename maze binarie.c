using System;

class Program {
    static int¨[,] maze = {
        { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
        { 1, 0, 0, 0, 0, 1, 0, 0, 0, 1 },
        { 1, 0, 1, 1, 0, 1, 0, 1, 0, 1 },
        { 1, 0, 0, 0, 0, 0, 0, 1, 0, 1 },
        { 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 },
        { 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 },
        { 1, 0, 1, 1, 1, 0, 1, 1, 1, 1 },
        { 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 },
        { 1, 1, 1, 0, 1, 1, 1, 1, 0, 1 },
        { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 }
    }
}; // representacion del laberinto en un matriz de 10x10

static int posX = 1; // posicion inicial en X del personajes
static int posY = 1; // posicion inicial en Y del personajes

static void Main() {
    console.WriteLine("Bienvenido al juego del laberitno")
    console.WriteLine("Para moverte usa las teclas W, A, S, D")
    console.WriteLine("Presiona cualquier tecla para comenzar")
    console.ReadKey(true);

    DrawMaze();

    while (true)
    ConsoleKeyInfo key = Console.ReadKey(true);
    if (key.key == ConsoleKey.UpArrow {
        Move(0, -1);
    } else if (key.key == ConsoleKey.DownArrow) {
        Move(0, 1);
    } else if (key.key == ConsoleKey.LeftArrow) {
        Move(-1, 0);
    } else if (key.key == ConsoleKey.RightArrow) {
        Move(1, 0);
    })
    }
}

static void DrawMaze() {
    for (int y = 0 < 10; y++) {
        for (int x = 0; x < 10; x++) {
            if (maze[y, x] == 1) {
                Console.Write("#");
            }
            else if (x == posX && y == posY) {
                Console.Write("O");
            }
            else {
                Console.Write(" ");
            }
        }

static void Move(int dx, int dy) {
    int newX = posX +dx;
    int newY = posY + dy;
if (maze[newY, newX] == 0) {
    posX = newX;
    posY = newY;

    DrawMze();

    if(posX == 8 && posY==8) {
        console.WriteLine("Felicitaciones, has llegado")
    }
}
}
