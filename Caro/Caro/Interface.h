#pragma once
#include "Board.h"

struct Map {
	int m_x, m_y;//real map
};
class Interface 
{
private:
	int _height, _width;
	char _p1, _p2;
	int _color1, _color2;
	Board* _board;
	Map _cursor;
	int _count;
private:
	Loca getLoca();
	void printCursor(Map NextPlace);
	void eraseCursor(Map prevPlace);
public:
	Interface();
	~Interface();

public:
	void DrawBoard();
	void Start();
	void doTask();
	void showLoca();
	int drawXO();
};

