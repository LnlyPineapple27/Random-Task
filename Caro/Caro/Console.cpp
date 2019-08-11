#include <stdio.h>
#include <conio.h>
#include "console.h"


int inputKey()
{

	int key = _getch();

	if (key == 224)	// special key
	{
		key = _getch();
		return key;
	}

	return key;

}


//-------------------------Screen-------------------------
void clrscr()
{
	CONSOLE_SCREEN_BUFFER_INFO	csbiInfo;
	HANDLE	hConsoleOut;
	COORD	Home = { 0,0 };
	DWORD	dummy;

	hConsoleOut = GetStdHandle(STD_OUTPUT_HANDLE);
	GetConsoleScreenBufferInfo(hConsoleOut, &csbiInfo);

	FillConsoleOutputCharacter(hConsoleOut, ' ', csbiInfo.dwSize.X * csbiInfo.dwSize.Y, Home, &dummy);
	csbiInfo.dwCursorPosition.X = 0;
	csbiInfo.dwCursorPosition.Y = 0;
	SetConsoleCursorPosition(hConsoleOut, csbiInfo.dwCursorPosition);
}


//screen: goto [x,y]
void gotoXY(int column, int line)
{
	COORD coord;
	coord.X = column;
	coord.Y = line;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}


//screen: get [x]
int whereX()
{
	CONSOLE_SCREEN_BUFFER_INFO csbi;
	if (GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &csbi))
		return csbi.dwCursorPosition.X;
	return -1;
}


//screen: get [y]
int whereY()
{
	CONSOLE_SCREEN_BUFFER_INFO csbi;
	if (GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &csbi))
		return csbi.dwCursorPosition.Y;
	return -1;
}


void TextColor(int color)
{
	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), color);
}

void resizeConsole(int width, int height)
{
	HWND console = GetConsoleWindow();
	RECT r;
	GetWindowRect(console, &r);
	MoveWindow(console, r.left, r.top, width, height, TRUE);
}


KEYHIT keyTrack(char key) {
	if (key == KEY_ENTER || key == KEY_SPACE)
		return ENTER;
	else if (key == KEY_UP || key == 'w' || key == 'W')
		return UP;
	else if (key == KEY_DOWN || key == 's' || key == 'S')
		return DOWN;
	else if (key == KEY_LEFT || key == 'a' || key == 'A')
		return LEFT;
	else if (key == KEY_RIGHT || key == 'd' || key == 'D')
		return RIGHT;
	else if (key >= '0' && key <= '9')//48 to 57 in ASCII
		return NUM;
	else if (key == KEY_ESC)
		return ESC;
	else if (key == KEY_BACKSPACE)
		return BACKSPACE;
	else if (key == KEY_TAB)
		return TAB;
	else
		return LETTER;
};

void Exit() {
	clrscr();
	gotoXY(65, 23);
	TextColor(Color_Yellow);
	printf_s("Thanks for using our BookStore-MS");
	Sleep(300);
	//system("color 008");
	clrscr();
	TextColor(Color_Cyan);
	gotoXY(82, 24); 
	printf_s("Good_Bye");
	TextColor(Color_Red);
	printf_s(" <3");
	Sleep(800);
	TextColor(Color_Green);
	clrscr();
	//ExitProcess(0);
};