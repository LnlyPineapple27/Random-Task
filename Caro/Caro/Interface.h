#pragma once
#include "Board.h"\
#define H_OFFSET 3
#define W_OFFSET 10
struct Map {
	unsigned int m_x, m_y;//real map
};
class Interface 
{
private:
	unsigned int _height, _width;
	char _p1, _p2;
	int _color;
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
	void drawXO();
};

