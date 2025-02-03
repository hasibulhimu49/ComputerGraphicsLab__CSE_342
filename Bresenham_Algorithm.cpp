#include <iostream>
#include <graphics.h>

void Bresenham(int x1, int y1, int x2, int y2) {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, (char*)"");

    int dx = x2 - x1;
    int dy = y2 - y1;
    int p = 2 * dy - dx;
    int x = x1, y = y1;

    while (x <= x2) {
        putpixel(x, y, WHITE);
        x++;
        if (p < 0) {
            p += 2 * dy;
        } else {
            y++;
            p += 2 * (dy - dx);
        }
        delay(10);
    }

    getch();
    closegraph();
}

int main() {
    int x1 = 100, y1 = 100, x2 = 400, y2 = 300;
    Bresenham(x1, y1, x2, y2);
    return 0;
}
