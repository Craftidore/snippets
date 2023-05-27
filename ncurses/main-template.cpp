#include <curses.h>
#include <ncurses.h>
#include <string>

// Globals; Do not change!
int maxx, maxy;

int main(int argc, char* argv[]) {
    initscr(); // start ncurses mode
    cbreak(); // Doesn't wait for <CR> to pass in input. You will want to manually handle <C-c> and <C-z>
    noecho(); // Don't echo pressed keys into the terminal
    keypad(stdscr, true); // permits use of arrow keys, function keys, etc.

    bool keepgoing = true;
    while(keepgoing) {
        // your code here!
    }

    printw("Press any character to quit.");
    refresh();
    getch();
    endwin();
    return 0;
}
