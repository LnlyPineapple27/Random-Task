

#ifndef _console_header
#define _console_header
#include<iostream>
#include<string>
#include<fstream>
#include<sstream>
#include<Windows.h>
#include <conio.h>
#include<ctime>
#define Color_Back			0
#define Color_DarkBlue		1
#define Color_DarkGreen		2
#define Color_DarkCyan		3
#define Color_DarkRed		4
#define Color_DarkPink		5
#define Color_DarkYellow	6
#define Color_DarkWhite		7
#define Color_Grey			8
#define Color_Blue			9
#define Color_Green			10
#define Color_Cyan			11
#define Color_Red			12
#define Color_Pink			13
#define Color_Yellow		14
#define Color_White			15

#define default_Color		7


#define KEY_UP		72
#define KEY_DOWN	80
#define KEY_LEFT	75
#define KEY_RIGHT	77
#define key_none	-1
#define KEY_ENTER   13
#define KEY_ESC     27
#define KEY_SPACE   32
#define KEY_BACKSPACE 8
#define KEY_TAB 9
//--------------------------------------------------------
//exepct LOC anyone don't touch anything between this line and this line + 9 line
//
#define LOG_POINT_Y1 11
#define LOG_POINT_Y2 24
#define LOG_POINT_X 41
#define ID_BLOCK_X 60
#define ID_BLOCK_Y 12
#define PASS_BLOCK_X 60
#define PASS_BLOCK_Y 15 
#define PROCESS_TIME 150
#define CONSOLE_MID_X 75
#define CONSOLE_MID_Y 15
//
//--------------------------------------------------------


//--------------------------------------------------------

#include <windows.h>

//--------------------------------------------------------

int inputKey();

//-------------------------Screen-------------------------
void clrscr();

//screen: goto [x,y]
void gotoXY(int column, int line);

//screen: get [x]
int whereX();

//screen: get [y]
int whereY();

void TextColor(int color);
//end----------------------Screen----------------------end

void resizeConsole(int width, int height);
//====================== DatPT's Private Modification=========================
enum KEYHIT {
	UP,
	DOWN,
	LEFT,
	RIGHT,
	ENTER,
	ESC,
	BACKSPACE,
	TAB,
	NUM,
	LETTER
};

KEYHIT keyTrack(char key);

void Exit();

#endif