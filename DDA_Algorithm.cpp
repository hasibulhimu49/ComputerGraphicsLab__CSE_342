#include <iostream>
#include <graphics.h>
#include <cmath>

void DDA(int x1, int y1, int x2, int y2) {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, (char*)"");

    int dx = x2 - x1;
    int dy = y2 - y1;
    int steps = std::max(abs(dx), abs(dy));

    float Xinc = dx / (float)steps;
    float Yinc = dy / (float)steps;

    float X = x1, Y = y1;
    for (int i = 0; i <= steps; i++) {
        putpixel(round(X), round(Y), WHITE);
        X += Xinc;
        Y += Yinc;
        delay(10);
    }

    getch();
    closegraph();
}

int main() {
    int x1 = 100, y1 = 100, x2 = 400, y2 = 300;
    DDA(x1, y1, x2, y2);
    return 0;
}
