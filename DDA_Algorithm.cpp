#include <iostream>
#include <cmath> // For abs() function
using namespace std;

void drawLineDDA(float x1, float y1, float x2, float y2) {
    float dx = x2 - x1;
    float dy = y2 - y1;

    // Calculate the number of steps required
    int steps = max(abs(dx), abs(dy));

    // Calculate increments
    float xIncrement = dx / steps;
    float yIncrement = dy / steps;

    float x = x1;
    float y = y1;

    cout << "DDA Line Drawing Algorithm Points:\n";

    // Generate and print the points on the line
    for (int i = 0; i <= steps; i++) {
        cout << "(" << round(x) << ", " << round(y) << ")\n";
        x += xIncrement;
        y += yIncrement;
    }
}

int main() {
    float x1 = 32, y1 = 35, x2 = 41, y2 = 41;
    drawLineDDA(x1, y1, x2, y2);
    return 0;
}
